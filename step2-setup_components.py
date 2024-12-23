# File: setup_components.py
# Version: 1.0.0
# Created on: 2024-12-23
# Description: Script to set up React component files and styles

import os
from pathlib import Path

def create_directory_structure():
    """Create the required directory structure"""
    directories = [
        'src/components',
        'src/styles'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

def create_navigation_component():
    """Create Navigation component"""
    content = """// src/components/Navigation.jsx
export default function Navigation() {
  return (
    <nav className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <img src="/api/placeholder/32/32" alt="Logo" className="h-8 w-8" />
            <span className="ml-2 text-xl font-semibold">비교과 프로그램</span>
          </div>
          <div className="flex items-center space-x-4">
            <a href="#" className="text-gray-600 hover:text-gray-900">홈</a>
            <a href="#" className="text-gray-600 hover:text-gray-900">대시보드</a>
            <a href="#" className="text-gray-600 hover:text-gray-900">프로그램 목록</a>
          </div>
        </div>
      </div>
    </nav>
  );
}"""
    
    with open('src/components/Navigation.jsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created Navigation.jsx")

def update_app_component():
    """Update App component"""
    content = """import React from 'react'
import Navigation from './components/Navigation'

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navigation />
      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold">비교과 프로그램 포털</h1>
          <p className="mt-2 text-gray-600">2025년 프로그램 안내 및 성과 분석</p>
        </div>
        
        {/* Quick Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8">
          <div className="bg-white p-4 rounded-lg shadow-sm">
            <div className="text-sm text-gray-600">총 프로그램</div>
            <div className="text-2xl font-bold">20개</div>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-sm">
            <div className="text-sm text-gray-600">참여 학생</div>
            <div className="text-2xl font-bold">100명</div>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-sm">
            <div className="text-sm text-gray-600">평균 만족도</div>
            <div className="text-2xl font-bold">4.2/5.0</div>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-sm">
            <div className="text-sm text-gray-600">취업 연계율</div>
            <div className="text-2xl font-bold">87.5%</div>
          </div>
        </div>
      </main>
      
      <footer className="bg-white mt-12 py-8">
        <div className="max-w-7xl mx-auto px-4 text-center text-sm text-gray-500">
          <p>© 2025 비교과 프로그램 포털. All rights reserved.</p>
          <p className="mt-2">최종 업데이트: 2025년 12월 21일</p>
        </div>
      </footer>
    </div>
  )
}

export default App"""
    
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated App.jsx")

def create_tailwind_css():
    """Create Tailwind CSS file"""
    content = """@tailwind base;
@tailwind components;
@tailwind utilities;"""
    
    with open('src/styles/tailwind.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created tailwind.css")

def update_main_jsx():
    """Update main entry point"""
    content = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './styles/tailwind.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)"""
    
    with open('src/main.jsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated main.jsx")

def create_tailwind_config():
    """Create Tailwind configuration"""
    content = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}"""
    
    with open('tailwind.config.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created tailwind.config.js")

def create_postcss_config():
    """Create PostCSS configuration"""
    content = """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}"""
    
    with open('postcss.config.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created postcss.config.js")

def main():
    """Main execution function"""
    print("Starting component setup...")
    
    # Create directory structure
    create_directory_structure()
    print("\nDirectories created successfully")
    
    # Create/update component files
    create_navigation_component()
    update_app_component()
    create_tailwind_css()
    update_main_jsx()
    print("\nComponent files created/updated successfully")
    
    # Create configuration files
    create_tailwind_config()
    create_postcss_config()
    print("\nConfiguration files created successfully")
    
    print("\nSetup complete! Next steps:")
    print("1. Install additional dependencies:")
    print("   npm install -D tailwindcss postcss autoprefixer")
    print("2. Restart your development server:")
    print("   npm run dev")

if __name__ == "__main__":
    main()