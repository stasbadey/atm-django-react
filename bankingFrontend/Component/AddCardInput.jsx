import axios from "axios";
import { Link } from "react-router-dom";
import { format } from 'react-string-format';
import classes from './CSSModules/AddCardInput.module.css'

let addCardURL = 'http://localhost:8000/add/';

function sendCard(cardNumber, pin) {
    console.log(cardNumber)
    const data = {
        'cardNumber': cardNumber,
        'PIN': pin,
        'expirationDate': format('{0}-{1}', new Date().getMonth(), new Date().getFullYear())
    }

    axios.post(addCardURL, data, {
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(s => {
        if(s.status !== 204)
            console.error("Exception occurred!")
    })
}

const AddCardInput = ({cardNumber, setCardNumber, pin, setPin}) => {
    console.log(cardNumber)
    console.log(pin)
    return (
     <>
        <div className={classes.container}>
            <p className={classes.cardNumber}>
                <strong>Card number</strong>
                <input className={classes.cardNumberInput} value={cardNumber} maxLength={16} type={"number"} name={"card number"} onInput={s => setCardNumber(s.target.value)}/>
            </p>
            <p className={classes.pin}>
                <strong>PIN</strong>
                <input className={classes.pinInput} value={pin} maxLength={4} type={"password"}  name={"PIN"} onInput={s => setPin(s.target.value)}/>
            </p>
        </div>
        <button className={classes.submitBtn} type={"submit"} onClick={() => {
                if(cardNumber !== '' && pin !== '') {
                    sendCard(cardNumber, pin);
                }
            }}><Link className={classes.btnLink} to='/header'>Submit</Link></button>
      </>
    );
}

export default AddCardInput;