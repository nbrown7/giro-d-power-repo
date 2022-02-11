import Button from'./Button.js'

const Body = (props) => {
    const onClick = () => {
        console.log('Click');
    }
  return (
    <div>
        <h2 className = 'naenae'>Press this button to calculate FTP</h2>
        <Button name='Click for power!' onClick = {onClick}/>
    </div>
  )
}

export default Body