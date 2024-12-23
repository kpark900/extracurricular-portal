# File: setup_project.py
# Version: 1.0.0
# Created on: 2024-12-23
# Description: Script to set up React project directory structure and files

import os
import json
from pathlib import Path

def create_directory_structure():
    """Create the required directory structure"""
    directories = [
        'src',
        'src/components',
        'src/styles',
        'public',
        '.github/workflows'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

def create_package_json():
    """Create package.json file"""
    package_json = {
        "name": "extracurricular-portal",
        "private": True,
        "version": "1.0.0",
        "type": "module",
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
        },
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0"
        },
        "devDependencies": {
            "@vitejs/plugin-react": "^4.0.0",
            "vite": "^5.0.0"
        }
    }
    
    with open('package.json', 'w', encoding='utf-8') as f:
        json.dump(package_json, f, indent=2)
    print("Created package.json")

def create_vite_config():
    """Create vite.config.js file"""
    vite_config = """// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/extracurricular-portal/',
  build: {
    outDir: 'dist',
    sourcemap: true
  }
});"""
    
    with open('vite.config.js', 'w', encoding='utf-8') as f:
        f.write(vite_config)
    print("Created vite.config.js")

def create_index_html():
    """Create index.html file"""
    index_html = """<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>비교과 프로그램 포털</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>"""
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("Created index.html")

def create_react_files():
    """Create React component files"""
    # Create main.jsx
    main_jsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)"""
    
    with open('src/main.jsx', 'w', encoding='utf-8') as f:
        f.write(main_jsx)
    print("Created src/main.jsx")
    
    # Create App.jsx
    app_jsx = """import React from 'react'

function App() {
  return (
    <div>
      <h1>비교과 프로그램 포털</h1>
    </div>
  )
}

export default App"""
    
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(app_jsx)
    print("Created src/App.jsx")

def create_github_workflow():
    """Create GitHub Actions workflow file"""
    workflow = """name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm test

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      - run: npm ci
      - run: npm run build
      - uses: actions/configure-pages@v3
      - uses: actions/upload-pages-artifact@v2
        with:
          path: './dist'

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2"""
        
    workflow_path = '.github/workflows/01-deploy.yml'
    with open(workflow_path, 'w', encoding='utf-8') as f:
        f.write(workflow)
    print(f"Created {workflow_path}")

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/dist

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*"""
    
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    print("Created .gitignore")

def main():
    """Main execution function"""
    print("Starting project setup...")
    
    # Create directory structure
    create_directory_structure()
    print("\nDirectory structure created successfully")
    
    # Create configuration files
    create_package_json()
    create_vite_config()
    create_index_html()
    print("\nConfiguration files created successfully")
    
    # Create React files
    create_react_files()
    print("\nReact files created successfully")
    
    # Create GitHub workflow
    create_github_workflow()
    print("\nGitHub workflow created successfully")
    
    # Create .gitignore
    create_gitignore()
    print("\n.gitignore created successfully")
    
    print("\nSetup complete! Next steps:")
    print("1. Run 'npm install' to install dependencies")
    print("2. Run 'npm run dev' to start development server")
    print("3. Open http://localhost:3000 to view your app")

if __name__ == "__main__":
    main()