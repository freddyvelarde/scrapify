import { Data } from "@/interfaces/data";

interface ProductListProps {
  products: Data[];
}

export function ProductList({ products }: ProductListProps) {
  return (
    <div className="bg-color3 flex flex-wrap justify-evenly">
      {products.map((product, index) => (
        <div key={index} className="bg-color2 m-3 w-96 h-96">
          <p>title: {product.title}</p>
          <img src={product.image} alt={product.title} />
          <a href={product.product} rel="noopener noreferrer" target="_blank">
            product
          </a>
          <p>price: {product.price}</p>
        </div>
      ))}
    </div>
  );
}
