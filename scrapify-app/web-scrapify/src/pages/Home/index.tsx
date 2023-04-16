import HeadComponent from "@/components/Head";
import { useState } from "react";

interface Data {
  image: string;
  price: string;
  product: string;
  title: string;
}

interface StoreData {
  data: Data[];
  message: string;
}

export default function HomeSection() {
  const [searchValue, setSearchValue] = useState("");
  const [storeData, setStoreData] = useState<StoreData>({
    data: [],
    message: "",
  });

  const handlerOnClick = (e: React.ChangeEvent<HTMLInputElement>) =>
    setSearchValue(e.target.value);

  const getStoreData = async (item: string) => {
    try {
      if (item.length < 1) {
        return setStoreData({ data: [], message: "type some product" });
      }
      const request = await fetch(
        `http://localhost/api/scrapper/search/${item}`
      );
      const jsonResponse = await request.json();
      setStoreData({ data: jsonResponse, message: "products:" });
      console.log("ready...");
    } catch (error) {
      console.log(error);
      setStoreData({ data: [], message: "error getting data" });
    }
  };

  const handlerOnSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    getStoreData(searchValue);
  };

  return (
    <div className="bg-color2">
      <HeadComponent title="Scrapify" />

      <form action="" onSubmit={handlerOnSubmit}>
        <input type="text" onChange={handlerOnClick} className="text-color1" />
        <button>search</button>
      </form>

      {storeData.data.map((product) => (
        <div>
          <hr />
          <p>title: {product.title}</p>
          <img src={product.image} alt={product.title} />
          <a href={product.product} target="_blank">
            product
          </a>
          <p>price: {product.price}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}
