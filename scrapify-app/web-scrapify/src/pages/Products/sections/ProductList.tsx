import { Data } from "@/interfaces/data";

interface ProductListProps {
  products: Data[];
}

export function ProductList({ products }: ProductListProps) {
  return (
    <div className="mx-5 flex flex-wrap justify-around">
      {products.map((product, index) => (
        <div key={index} className="bg-color2 my-3 w-96 h-96 rounded-sm">
          <img
            src={product.image}
            alt={product.title}
            className="h-2/5 w-full object-cover"
          />
          <div className="m-2 flex flex-col justify-between h-2/4">
            <p className="mb-2">{product.title}</p>
            <p>price: {product.price}</p>
            <a
              href={product.product}
              className="bg-color1 p-3"
              rel="noopener noreferrer"
              target="_blank"
            >
              Check it out
            </a>
          </div>
        </div>
      ))}
    </div>
  );
}
