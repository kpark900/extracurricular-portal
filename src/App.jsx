import React from 'react'
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

export default App