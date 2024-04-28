# Description

App solving the task for 2024 SpotOn's recruitment

# Tech Stack

![ReactJS](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![Tailwindcss](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-000000?style=for-the-badge&logo=shadcnui&logoColor=white)

# Run Development Server


## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python 3.
* You have a Windows/Linux/Mac machine.
* You have pnpm package manager
* You have env for api calls

```bash
git clone https://github.com/CALLmeDOMIN/SpotOn
```

## Running backend

```bash
cd SpotOn/server
```

### Installing packages
Linux and macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Running the development server

```bash
uvicorn main:app --reload
```

## Running frontend

<span style="color: red;">Ensure you have your **env** plugged</span>

For this create `.env` file in the `client/` directory and add `SPOONACULAR_API_KEY=` like in `.env.template` file

```bash
cd Spoton/client
pnpm install
pnpm dev
```

Open [http://localhost:5173](http://localhost:3000) with your browser to see the result.

You should be good to go.


## Author

[@CALLmeDOMIN](https://github.com/CALLmeDOMIN)


## License

This project is licensed under [MIT](./LICENSE) license.