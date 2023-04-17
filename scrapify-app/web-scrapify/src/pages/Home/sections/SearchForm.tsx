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
      className="mx-3  py-5 flex justify-between  sm:justify-center sm:py-8"
      onSubmit={handleFormSubmit}
    >
      <input
        type="text"
        onChange={handleInputChange}
        className="text-color1 text-sm md:text-base w-full sm:w-96"
      />
      <button className="ml-2 bg-color5 text-sm text-color1 px-2 rounded-md sm:text-base">
        search
      </button>
    </form>
  );
}
