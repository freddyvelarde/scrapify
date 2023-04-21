import data from "../../../data/endpointsApi";
import { useEffect, useState } from "react";
import { ProductList } from "./ProductList";
import { Data } from "@/interfaces/data";

interface C {
  data: Data[];
  product: string;
}

interface Categories {
  productsByCategory: C[];
  message: string;
}

export function CategoryProductList() {
  const [categories, setCategories] = useState<Categories>({
    productsByCategory: [],
    message: "",
  });

  const fetchProductsByCategory = async () => {
    try {
      const productsByCategory = await fetch(data.categories);
      const response = await productsByCategory.json();
      setCategories({
        productsByCategory: response,
        message: "products fetched",
      });
      console.log("ready...");
    } catch (error) {
      setCategories({
        productsByCategory: [],
        message: "error getting products by categories",
      });
      console.error(error);
    }
  };
  useEffect(() => {
    fetchProductsByCategory();
  }, []);

  return (
    <div>
      <button
        onClick={() => {
          for (const cat of categories.productsByCategory) {
            console.log(cat.product);
            console.log(cat.data);
          }
        }}
      >
        Fetch products
      </button>
      <hr />
      {categories.productsByCategory.map((category, index) => (
        <div key={index}>
          <h1>{category["product"]}</h1>
          <ProductList products={category.data} />
        </div>
      ))}
    </div>
  );
}
