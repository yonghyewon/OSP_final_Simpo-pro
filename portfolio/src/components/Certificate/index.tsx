import SectionTitle from "../SectionTitle";
import CertificateItem from "./CertificateItem";

import { DataProps } from "@/types";

const Certificate = ({ certificate }: Pick<DataProps, "certificate">) => {
  // certificate이 배열인지 확인하고, 배열이 아니면 빈 배열로 처리
  const certificateArray = Array.isArray(certificate) ? certificate : [];

  return (
    <div>
      <SectionTitle>Certificates</SectionTitle>
      <div className="flex flex-col gap-24">
        {[...certificateArray].reverse().map((certificate) => (
          <CertificateItem key={certificate.id} {...certificate} />
        ))}
      </div>
    </div>
  );
};

export default Certificate;
