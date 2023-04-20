import { useState } from "react";
import HeadComponent from "@/components/Head";
import SearchForm from "./sections/SearchForm";
import useStoreData from "@/hooks/useStoreData";
import { ProductList } from "./sections/ProductList";

export default function Products() {
  const [searchValue, setSearchValue] = useState("");
  const { getStoreData, storeData } = useStoreData();

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setSearchValue(e.target.value);

  const handleFormSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    getStoreData(searchValue);
  };

  return (
    <div className="">
      <HeadComponent title="Scrapify" />
      <SearchForm
        handleInputChange={handleInputChange}
        handleFormSubmit={handleFormSubmit}
      />
      <ProductList products={storeData.data} />
    </div>
  );
}
