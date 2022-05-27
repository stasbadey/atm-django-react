import {useState} from "react";
import axios from "axios";
import {format} from "react-string-format";
import {Link} from "react-router-dom"
import classes from "./CSSModules/RefillCardInput.module.css"

const refillCardURL = 'http://localhost:8000/refill/?amount={0}'

function sendRefillRequest(cardNumber, pin, amount) {
    axios.get(format(refillCardURL, amount), {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'cardNumber': cardNumber,
            'PIN': pin
        }
    }).then(s => {
        if(s.status !== 204)
            console.error('Exception occurred!')
    })
}

const RefillCardInput = ({cardNumber, pin}) => {
    const [amount, setAmount] = useState(0);

    function incrementAmount() {
        setAmount(amount + 1);
    }

    function decrementAmount() {
        setAmount(amount - 1);
    }

    return (
        
      <div className={classes.container}>
          <button className={classes.refillBtn} onClick={decrementAmount}>-</button>
          <span className={classes.refillAmount}>{amount}</span>
          <button className={classes.refillBtn} onClick={incrementAmount}>+</button>
          <button className={classes.submitBtn} type={"submit"} onClick={() => sendRefillRequest(cardNumber, pin, amount)}><Link className={classes.link} to='/header'>Submit</Link></button>
      </div>
    );
}

export default RefillCardInput;