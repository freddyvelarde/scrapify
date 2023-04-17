interface SearchProps {
  handleInputChange: React.ChangeEventHandler<HTMLInputElement>;
  handleFormSubmit: React.FormEventHandler<HTMLFormElement>;
}

export default function SearchForm({
  handleInputChange,
  handleFormSubmit,
}: SearchProps) {
  return (
    <form
      action=""
      className="p-7 flex justify-center items-center"
      onSubmit={handleFormSubmit}
    >
      <input
        type="text"
        onChange={handleInputChange}
        className="text-color1 text-sm md:text-base"
      />
      <button className="ml-2 bg-color5 text-sm text-color1 px-2 rounded-md md:text-base">
        search
      </button>
    </form>
  );
}
