function Header(){
    return (
    <header>
        <nav className="nav">
            <img src="react_logo.png" className="nav-img"/>
            <ul className="nav-items">
                <li>Pricing</li>
                <li>About</li>
                <li>Contact</li>
            </ul>
        </nav>
    </header>
    )
}

function Footer(){
    return (
    <footer>
        <small>© 2022 Sawiński development. All rigths reserved</small>
    </footer>
    )
}

function MainContent(){
    return(
    <div>
        <h1>Why you should learn React</h1>
        <ol>
            <li>React is fun</li>
            <li>React is declarative</li>
            <li>React is composable</li>
            <li>React is highly paid XD</li>
        </ol>
    </div>
    )
}

function InfoPage(){ 
    return (
    <div>
        <Header/>
        <MainContent />
        <Footer />
    </div>
    )
}

ReactDOM.render(<InfoPage />, document.getElementById('root'));
