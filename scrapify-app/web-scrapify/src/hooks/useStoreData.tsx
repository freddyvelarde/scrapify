import { Data } from "@/interfaces/data";
import { useState } from "react";

interface StoreData {
  data: Data[];
  message: string;
}

export default function useStoreData() {
  const [storeData, setStoreData] = useState<StoreData>({
    data: [],
    message: "",
  });

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

  return { storeData, getStoreData };
}
