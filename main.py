import eel
import json
import portfolio_generator as pfg
from selenium import webdriver
import webbrowser
from shutil import copy as cp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import json
import os
import time
import webbrowser

eel.init('gui', allowed_extensions=['.js', '.html'])

@eel.expose                         
def information_submit(x):
    user_info = json.loads(x)
    temp_info = json.dumps(x, ensure_ascii=False, indent=4)
    print(temp_info)
    information = {
        "name": user_info['name'],
        "contact": [
            {"id": 0, "name": "Email", "href": user_info['email'], "isEmail": True},
            {"id": 1, "name": "Github", "href": '제작 중'},
            {"id": 2, "name": "Blog", "href": '제작 중'}
        ],
        "additional_info": '추가 정보는 public/markdown에서 편집하세요 😊'
    }

    resume_data = {
        "resumeTitle": {"title": f'{user_info['name']}의 자기소개서, 포트폴리오'},
        "information": information,
        "workExperience": user_info['career'],
        "project": user_info['projects'],
        "activity": user_info['experience'],
        "education": user_info['education'],
        "certificate": user_info['certifications'],
    }

    # JSON 파일로 저장
    with open("portfolio_data.json", "w", encoding="utf-8") as f:
        json.dump(resume_data, f, ensure_ascii=False, indent=2)
    

    print("\n✅ 포트폴리오 데이터가 'portfolio_data.json' 파일에 저장되었습니다!")
    cp("portfolio_data.json", "./portfolio/portfolio_data.json")
    
    pfg.markdown_editor() ## markdown introduce.md file 수정
    # 서버 실행
    server_process = pfg.run_server()
    if not server_process:
        print("서버 실행에 실패하여 작업을 종료합니다.")
        return

    # 웹 페이지 저장
    try:
        url = "http://localhost:3000/"
        pfg.save_page_as_html(url)
        pfg.open_html_on_desktop()
    finally:
        # 서버 프로세스 종료
        print("[서버 종료 중...]")
        server_process.terminate()
        print("[서버가 종료되었습니다.]")

    print("포트폴리오가 완성되었습니다. 해당 파일을 열어보세요: http://localhost:3000/")

if __name__ == "__main__":
    eel.start('index.html')