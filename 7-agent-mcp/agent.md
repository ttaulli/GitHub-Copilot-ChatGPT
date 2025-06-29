Agent Mode

End of prompt engineering?
- Prompt is more about goals, not detailed descriptions

Creating an app

Prompt:  I want to create a web application that provides weather information for a given city.  I want to use a free API.  Also, what do you suggest for the tech stack?

In the terminal:  npx create-next-app@latest weather-app

npm run dev

Use Claude Sonnet 3.7

Prompt: I have setup NextJS app in the directory 7-agent-mcp/weather-app.  Replace the homepage with a modern looking form that allows users to enter a city name and submit it.  Use TailwindCSS for styling.  Use the openweathermap API to fetch and display the current weather for the entered city.  Add client-side validation to ensure the city name is not empty before submission. The API key will go into the .env.local file. 


Selection:
- Nextjs
- OpenWeatherMap API
- https://openweathermap.org/api
- Register and get the API
- API Key/Weather - df25ed7c0f6c5018ecb2a333681c4f55


MCP Demo

- Select Agent Mode from the dropdown menu.​
- You can find MCP servers here: https://github.com/modelcontextprotocol/servers
- Supabase provides a fully managed PostgreSQL database as part of each project you create. 
- Create an account: https://supabase.com/
- Click Start project
- Register an account
- Enter the name of the project/todo
- Enter password
- Select Table Editor
- Select Create a new table
- Name: tasks
- Click New column
- title: string
- completed: boolean
- Click save
- Click Insert to add new rows of data

- Obtain Your Supabase Personal Access Token
- Click on your profile avatar and select Account preferences.
- Select Access Tokens
- Select Generate new token
- Enter name for it
- Copy your token

- Instructions:  https://supabase.com/docs/guides/getting-started/mcp
- In VS Code, create a .vscode directory in your project root if it doesn't already exist
- Create a .vscode/mcp.json file if it doesn't already exist
- Add the following configuration:


{
  "inputs": [
    {
      "type": "promptString",
      "id": "supabase-access-token",
      "description": "Supabase personal access token",
      "password": true
    }
  ],
  "servers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server-supabase@latest", "--read-only", "--project-ref=<project-ref>"],
      "env": {
        "SUPABASE_ACCESS_TOKEN": "${input:supabase-access-token}"
      }
    }
  }
}

- Save the file
- You will see Start inside it
- Click it to run the mcp server
- Enter your access token for supabase
- Activate Chat
- In the tools icon, you will see you have 26
- Click it
- You can select/deselect the tools you want to use
- Prompt: What is the schema for the tasks table in the todo project?

- add MCP for github

{
  "inputs": [
    {
      "type": "promptString",
      "id": "supabase-access-token",
      "description": "Supabase personal access token",
      "password": true
    },
    {
      "type": "promptString",
      "id": "github-access-token",
      "description": "GitHub personal access token",
      "password": true
    }
  ],
  "servers": {
    "supabase": {
      "command": "npx",
      "args": [
        "-y",
        "@supabase/mcp-server-supabase@latest",
        "--read-only",
        "--project-ref=<project-ref>"
      ],
      "env": {
        "SUPABASE_ACCESS_TOKEN": "${input:supabase-access-token}"
      }
    },
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github@latest",
        "--repo=ttaulli/GitHub-Copilot-ChatGPT",
      ],
      "env": {
        "GITHUB_ACCESS_TOKEN": "${input:github-access-token}"
      }
    }
  }
}



- Use Claude Sonnet 3.7
- Create a todo app using the nextjs

- Prompt: In the todo nextjs project, replace the home page with a modern looking to do application. Use TailwindCSS for styling.  The to do items will be stored in the supabase database called todo.  The table is called tasks and has two columns: title (string) and completed (boolean).  The app should allow users to add new tasks, mark tasks as completed, and delete tasks.  Fetch the tasks from the supabase database and display them on the homepage.  Use environment variables for the supabase URL and anon key.


# Unit Tests
- Agent and unit testing
- GitHub Copilot can create test cases
- Can't do everything
- But provide a good start
- Different types of unit testing frameworks
- In your prompt, specify the framework
- Chat tends to have more tests than using in-line chat
- /tests and run it 
- tests.py


Prompt:  Please create a separate unit test tests.py. The test file should be in the same 7-agent-mcp directory and named test_tests.py. Make sure all import paths are correct for running the tests. Use unittest for the test framework.