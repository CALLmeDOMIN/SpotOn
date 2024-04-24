import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const fetchData = async () => {
  const res = await axios.get("/api");
  return res.data;
};

function App() {
  const query = useQuery({ queryKey: ["data"], queryFn: fetchData });

  if (query.isLoading) {
    return <h1>Loading...</h1>;
  }

  if (query.isError) {
    return <h1>Error: {JSON.stringify(query.error.message)}</h1>;
  }

  return (
    <>
      <h1 className="text-3xl font-bold underline">Hello world!</h1>
      <p className="text-lg">Data: {JSON.stringify(query.data)}</p>
    </>
  );
}

export default App;
