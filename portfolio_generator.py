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

npm_path = "C:/Program Files/nodejs/npm.cmd"  # npm 경로 수정 필요

# 서버 실행 함수
def run_server():
    try:
        print("[서버 실행 중...]")
        p = subprocess.Popen([npm_path, "run", "dev"], cwd="./portfolio")
        time.sleep(5)  # 서버가 실행될 때까지 대기 (필요 시 시간 조정)
        return p
    except Exception as e:
        print(f"서버 실행 중 오류 발생: {e}")
        return None
    
# 인적사항 입력
def get_information():
    print("\n[인적사항 입력]")
    name = input("이름을 입력하세요: ")
    email = input("이메일을 입력하세요: ")
    github = input("깃허브 주소를 입력하세요: ")
    blog = input("블로그 주소를 입력하세요: ")
    additional_info = input("추가 설명을 입력하세요 (선택 사항): ")

    return {
        "name": name,
        "contact": [
            {"id": 0, "name": "Email", "href": email, "isEmail": True},
            {"id": 1, "name": "Github", "href": github},
            {"id": 2, "name": "Blog", "href": blog}
        ],
        "additional_info": additional_info
    }

# 직장 경력 입력
def get_work_experience():
    print("\n[직장 경력 입력]")
    work_experience = []
    while True:
        try:
            count = int(input("작성할 직장 경력의 개수를 입력하세요: "))
            if count == 0:
                return work_experience  # 0이면 그냥 넘어가기
            if count < 1:
                print("1개 이상의 경력을 입력해야 합니다.")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
    
    for i in range(count):
        print(f"\n경력 {i+1}")
        name = input("직장명을 입력하세요: ")
        position = input("담당 직무를 입력하세요: ")
        description = input("직장에 관한 간단한 설명을 입력하세요:")
        start = input("시작 기간 (예: 2022.01): ")
        end = input("종료 기간 (현재 재직중이라면 'now'를 입력하세요): ")
        additional_info = input("추가 설명을 입력하세요 (선택 사항): ")

        work_experience.append({
            "id": i,
            "name": name,
            "position": position,
            "period": [start, end],
            "description": description,
            "additional_info": additional_info
        })

    return work_experience

# 프로젝트 경험 입력
def get_projects():
    print("\n[프로젝트 경험 입력]")
    projects = []
    while True:
        try:
            count = int(input("작성할 프로젝트 개수를 입력하세요: "))
            if count == 0:
                return projects  # 0이면 그냥 넘어가기
            if count < 1:
                print("1개 이상의 프로젝트를 입력해야 합니다.")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
    
    for i in range(count):
        print(f"\n프로젝트 {i+1}")
        name = input("프로젝트명을 입력하세요: ")
        description = input("프로젝트에 대한 설명을 입력하세요: ")
        web_url = input("웹 페이지 링크 (없으면 엔터): ")
        repo_url = input("깃허브 레포지토리 링크 (없으면 엔터): ")
        is_team = input("팀 프로젝트인가요? (y/n): ").lower() == 'y'
        start = input("시작 기간 (예: 2022.07): ")
        end = input("종료 기간 (예: 2022.09): ")
        stack = input("사용 기술을 콤마로 구분해 입력하세요 (예: React.js, JavaScript): ").split(", ")
        additional_info = input("추가 설명을 입력하세요 (선택 사항): ")

        projects.append({
            "id": i,
            "name": name,
            "description": description,
            "webUrl": web_url if web_url else None,
            "repoUrl": repo_url if repo_url else None,
            "isTeam": is_team,
            "period": [start, end],
            "stack": stack,
            "additional_info": additional_info
        })

    return projects

# 활동 입력
def get_activities():
    print("\n[활동 입력]")
    activities = []
    while True:
        try:
            count = int(input("작성할 활동 개수를 입력하세요: "))
            if count == 0:
                return activities  # 0이면 그냥 넘어가기
            if count < 1:
                print("1개 이상의 활동을 입력해야 합니다.")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
    
    for i in range(count):
        print(f"\n활동 {i+1}")
        name = input("활동명을 입력하세요: ")
        description = input("활동에 대한 간략한 설명을 입력하세요: ")
        start = input("시작 기간 (예: 2022.06): ")
        end = input("종료 기간 (예: 2022.08): ")
        additional_info = input("추가 설명을 입력하세요 (선택 사항): ")

        activities.append({
            "id": i,
            "name": name,
            "period": [start, end],
            "description": description,
            "additional_info": additional_info
        })

    return activities

# 교육 입력
def get_education():
    print("\n[교육 입력]")
    education = []
    while True:
        try:
            count = int(input("작성할 교육 개수를 입력하세요: "))
            if count == 0:
                return education  # 0이면 그냥 넘어가기
            if count < 1:
                print("1개 이상의 교육을 입력해야 합니다.")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
    
    for i in range(count):
        print(f"\n교육 {i+1}")
        name = input("교육명을 입력하세요: ")
        description = input("교육에 대한 간략한 설명을 입력하세요: ")
        start = input("시작 기간 (예: 2013.02): ")
        end = input("종료 기간 (예: 2020.02): ")
        additional_info = input("추가 설명을 입력하세요 (선택 사항): ")

        education.append({
            "id": i,
            "name": name,
            "period": [start, end],
            "description": description,
            "additional_info": additional_info
        })

    return education

# 자격증 입력
def get_certificates():
    print("\n[자격증 입력]")
    certificates = []
    while True:
        try:
            count = int(input("작성할 자격증 개수를 입력하세요: "))
            if count == 0:
                return certificates  # 0이면 그냥 넘어가기
            if count < 1:
                print("1개 이상의 자격증을 입력해야 합니다.")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
    
    for i in range(count):
        print(f"\n자격증 {i+1}")
        name = input("자격증명을 입력하세요: ")
        date = input("취득일 (예: 2019.07.28): ")
        organizer = input("주관 기관을 입력하세요: ")
        additional_info = input("추가 설명을 입력하세요 (선택 사항): ")

        certificates.append({
            "id": i,
            "name": name,
            "date": date,
            "organizer": organizer,
            "additional_info": additional_info
        })

    return certificates

# 수상 경력 입력
def get_awards():
    print("\n[수상 입력]")
    awards = []
    while True:
        try:
            count = int(input("작성할 수상 개수를 입력하세요: "))
            if count == 0:
                return awards  # 0이면 그냥 넘어가기
            if count < 1:
                print("1개 이상의 수상을 입력해야 합니다.")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
    
    for i in range(count):
        print(f"\n수상 {i+1}")
        name = input("수상명을 입력하세요: ")
        date = input("수상일 (예: 2019.07.28): ")
        organizer = input("수여 기관을 입력하세요: ")
        description = input("수상에 대한 간략한 설명을 입력하세요: ")
        additional_info = input("추가 설명을 입력하세요 (선택 사항): ")

        awards.append({
            "id": i,
            "name": name,
            "date": date,
            "organizer": organizer,
            "description": description,
            "additional_info": additional_info
        })

    return awards


# 바탕화면에 HTML 파일 저장 함수
def save_page_as_html(url):
    # 바탕화면 경로
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    save_path = os.path.join(desktop_path, "saved_page.html")  # 저장될 파일 경로

    # Chrome 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 화면 없이 브라우저 실행
    chrome_options.add_argument("--disable-gpu")  # GPU 비활성화
    chrome_options.add_argument("--no-sandbox")  # 보안 문제 방지

    # 웹드라이버 초기화
    driver = webdriver.Chrome(options=chrome_options)

    # 웹사이트 열기
    try:
        print(f"[웹사이트 접속 중: {url}]")
        driver.get(url)
        time.sleep(10)  # 페이지 로드 대기 (필요 시 시간 조정)

        # 페이지 소스를 가져와 HTML로 저장
        html_source = driver.page_source
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(html_source)
        print(f"웹 페이지가 {save_path}에 저장되었습니다.")
    except Exception as e:
        print(f"웹 페이지 저장 중 오류 발생: {e}")
    finally:
        driver.quit()


# HTML 파일 열기 함수
def open_html_on_desktop():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "saved_page.html")

    if os.path.exists(file_path):
        webbrowser.open(f"file:///{file_path}")
        print(f"HTML 파일이 열렸습니다: {file_path}")
    else:
        print("saved_page.html 파일이 바탕화면에 존재하지 않습니다.")

# 포트폴리오 markdown 수정 함수
def markdown_editor():
    with open("portfolio_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        contents = data['information']['additional_info'] ## additional info 정보
    target_file = './portfolio/public/markdown/information/introduce.md' ## 수정할 마크다운 파일 위치 및 파일명
    
    with open(target_file, '+w', encoding="utf-8") as f:
        f.write(contents)

# 메인 함수
def main():
    print("포트폴리오 데이터를 작성해봅시다!\n")
    resume_data = {
        "resumeTitle": {"title": input("포트폴리오 최상단 제목을 입력하세요: ")},
        "information": get_information(),
        "workExperience": get_work_experience(),
        "project": get_projects(),
        "activity": get_activities(),
        "education": get_education(),
        "certificate": get_certificates(),
        "award": get_awards(),
    }

    # JSON 파일로 저장
    with open("portfolio_data.json", "w", encoding="utf-8") as f:
        json.dump(resume_data, f, ensure_ascii=False, indent=2)

    print("\n✅ 포트폴리오 데이터가 'portfolio_data.json' 파일에 저장되었습니다!")
    cp("portfolio_data.json", "./portfolio/portfolio_data.json")
    
    markdown_editor() ## markdown introduce.md file 수정
    
    # 서버 실행
    server_process = run_server()
    if not server_process:
        print("서버 실행에 실패하여 작업을 종료합니다.")
        return

    # 웹 페이지 저장
    try:
        url = "http://localhost:3000/"
        save_page_as_html(url)
        open_html_on_desktop()
    finally:
        # 서버 프로세스 종료
        print("[서버 종료 중...]")
        server_process.terminate()
        print("[서버가 종료되었습니다.]")

    print("포트폴리오가 완성되었습니다. 해당 파일을 열어보세요: http://localhost:3000/")
    


if __name__ == "__main__":
    main()