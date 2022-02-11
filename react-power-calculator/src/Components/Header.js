import PropTypes from 'prop-types'
import '../index.css';

const Header = (props) => {
  return (
    <header>
        <h1>Hello {props.name}, welcome to the Power Calculator</h1>
    </header>
  )
}

Header.defaultProps = {
    name: 'Noah',
}

Header.propTypes = {
    name:PropTypes.string,
}


export default Header