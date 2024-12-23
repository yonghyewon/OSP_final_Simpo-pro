import SectionTitle from "../SectionTitle";
import AwardItem from "./AwardItem";

import { DataProps } from "@/types";

const Award = ({ award }: Pick<DataProps, "award">) => {
  // award가 배열인지 확인하고, 배열이 아니면 빈 배열로 처리
  const awardArray = Array.isArray(award) ? award : [];

  return (
    <div>
      <SectionTitle>Award</SectionTitle>
      <div className="flex flex-col gap-24">
        {[...awardArray].reverse().map((award) => (
          <AwardItem key={award.id} {...award} />
        ))}
      </div>
    </div>
  );
};

export default Award;
