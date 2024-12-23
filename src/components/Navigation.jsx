// src/components/Navigation.jsx
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
}