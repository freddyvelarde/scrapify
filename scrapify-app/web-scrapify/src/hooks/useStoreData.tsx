import { Data } from "@/interfaces/data";
import data from "../data/endpointsApi";
import { useState } from "react";

interface StoreData {
  data: Data[];
  message: string;
  dataObtained: boolean;
}

export default function useStoreData() {
  const [storeData, setStoreData] = useState<StoreData>({
    data: [],
    message: "",
    dataObtained: false,
  });

  const getStoreData = async (item: string) => {
    try {
      if (item.length < 1) {
        return setStoreData({ data: [], message: "type some product", dataObtained: false });
      }
      const request = await fetch(`${data.products}${item}`);
      const jsonResponse = await request.json();
      setStoreData({ data: jsonResponse, message: "products:", dataObtained: true });
      console.log("ready...");
    } catch (error) {
      console.log(error);
      setStoreData({ data: [], message: "error getting data", dataObtained: false });
    }
  };

  return { storeData, getStoreData };
}
