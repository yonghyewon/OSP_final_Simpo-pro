import SectionTitle from "../SectionTitle";
import ActivityItem from "./ActivityItem";

import { DataProps } from "@/types";

const Activity = ({ activity }: Pick<DataProps, "activity">) => {
  // activity가 배열인지 확인하고, 배열이 아니면 빈 배열로 처리
  const activityArray = Array.isArray(activity) ? activity : [];

  return (
    <div>
      <SectionTitle>Activities</SectionTitle>
      <div className="flex flex-col gap-24">
        {[...activityArray].reverse().map((activity) => (
          <ActivityItem key={activity.id} {...activity} />
        ))}
      </div>
    </div>
  );
};

export default Activity;
