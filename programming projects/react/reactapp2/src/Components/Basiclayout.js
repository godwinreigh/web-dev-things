import React from 'react'
import '../App.css'

class Basiclayout extends React.Component {
    render() {
        return (
            <div className="layout-container">
                <div className="navbar-container">
                    <nav className="navbar">
                        <h1 className="branding">LOGO</h1>
                        <ul className="ul">
                            <li className="list"><a href="#">Home</a></li>
                            <li className="list"><a href="#">About</a></li>
                            <li className="list"><a href="#">Contacts</a></li>
                        </ul>
                    </nav>
                </div>
            </div>
        );
    }
}
export default Basiclayout;