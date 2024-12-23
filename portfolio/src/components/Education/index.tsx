import SectionTitle from "../SectionTitle";
import EducationItem from "./EducationItem";

import { DataProps } from "@/types";

const Education = ({ education }: Pick<DataProps, "education">) => {
  // education이 배열인지 확인하고, 배열이 아니면 빈 배열로 처리
  const educationArray = Array.isArray(education) ? education : [];

  return (
    <div>
      <SectionTitle>Education</SectionTitle>
      <div className="flex flex-col gap-24">
        {[...educationArray].reverse().map((education) => (
          <EducationItem key={education.id} {...education} />
        ))}
      </div>
    </div>
  );
};

export default Education;