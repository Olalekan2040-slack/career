import { Route, BrowserRouter, Routes } from 'react-router-dom';
import { AuthProvider } from './api/AuthContext';
import { useKeepAlive } from './api/useKeepAlive';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Landing from './pages/Landing';
import LeadCapture from './pages/LeadCapture';
import Assessment from './pages/Assessment';
import Results from './pages/Results';
import Signup from './pages/Signup';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';

function App() {
  useKeepAlive();

  return (
    <AuthProvider>
      <BrowserRouter>
        <div className="app-shell">
          <Navbar />
          <main className="app-main">
            <Routes>
              <Route path="/" element={<Landing />} />
              <Route path="/start" element={<LeadCapture />} />
              <Route path="/assessment" element={<Assessment />} />
              <Route path="/results/:resultId" element={<Results />} />
              <Route path="/signup" element={<Signup />} />
              <Route path="/login" element={<Login />} />
              <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
