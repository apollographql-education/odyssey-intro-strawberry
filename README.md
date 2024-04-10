# (Odyssey Course) Intro to GraphQL with Python & Strawberry

Welcome to the starter code for **Intro to GraphQL with Python & Strawberry**. You can find the [course lessons and instructions](https://apollographql.com/tutorials/intro-strawberry) on Odyssey, [Apollo](https://apollographql.com)'s learning platform.

## How to use this repo

The course will walk you step by step on what to do. This codebase is the starting point of your journey!

This project uses Python. In order to build the project locally, run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

To start the server, from the root directory, run:

```bash
uvicorn main:app --reload
```

Right now, the server returns a simple "Hello World" message from `http://localhost:8000`.

The `final` branch of this repo contains the final stage of the course, with all of the steps and code completed! If you get stuck, you can refer to it and compare your code.

## Getting Help

This repo is _not regularly monitored_.

For any issues or problems concerning the course content, please refer to the [Odyssey topic in our community forums](https://community.apollographql.com/tags/c/help/6/odyssey). You can also [join the Apollo Discord](https://discord.gg/graphos).