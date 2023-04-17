import { Data } from "@/interfaces/data";

interface ProductListProps {
  products: Data[];
}

export function ProductList({ products }: ProductListProps) {
  return (
    <div>
      {products.map((product, index) => (
        <div key={index}>
          <hr />
          <p>title: {product.title}</p>
          <img src={product.image} alt={product.title} />
          <a href={product.product} rel="noopener noreferrer" target="_blank">
            product
          </a>
          <p>price: {product.price}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}
