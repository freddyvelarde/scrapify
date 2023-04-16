import HeadComponent from "@/components/Head";
import { useState } from "react";

export default function Home() {
  const [searchValue, setSearchValue] = useState("");

  const handlerOnClick = (e: React.ChangeEvent<HTMLInputElement>) =>
    setSearchValue(e.target.value);

  const getStoreData = async (item: string) => {
    const request = await fetch(`http://localhost/api/scrapper/search/${item}`);
    const jsonResponse = await request.json();
    console.log(jsonResponse);
  };

  const handlerOnSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    getStoreData(searchValue);

    // console.log(searchValue);
  };

  return (
    <div className="bg-color2">
      <HeadComponent title="Scrapify" />

      <form action="" onSubmit={handlerOnSubmit}>
        <input type="text" onChange={handlerOnClick} className="text-color1" />
        <button>search</button>
      </form>
    </div>
  );
}
