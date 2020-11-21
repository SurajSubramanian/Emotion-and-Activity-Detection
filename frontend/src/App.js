import React from 'react'
import './App.css';
import Header from './Header';
import Upload from './Upload';
// import VideoElement from './Video';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    return (
        <div>
            <Header />
            <div className="container">
                <Upload />
            </div>
        </div>
    );
}

export default App;
