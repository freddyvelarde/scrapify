import Head from "next/head";

type HeadProps = {
  title: string;
};

function HeadComponent({ title }: HeadProps) {
  return (
    <Head>
      <title>{title}</title>
    </Head>
  );
}

export default HeadComponent;
