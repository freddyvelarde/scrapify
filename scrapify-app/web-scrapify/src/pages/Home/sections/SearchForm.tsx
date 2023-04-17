interface SearchProps {
  handleInputChange: React.ChangeEventHandler<HTMLInputElement>;
  handleFormSubmit: React.FormEventHandler<HTMLFormElement>;
}

export default function SearchForm({
  handleInputChange,
  handleFormSubmit,
}: SearchProps) {
  return (
    <form action="" onSubmit={handleFormSubmit}>
      <input type="text" onChange={handleInputChange} className="text-color1" />
      <button>search</button>
    </form>
  );
}
