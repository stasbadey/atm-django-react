import axios from "axios";
import {useState} from "react";
import classes from './CSSModules/CheckMoneyLabel.module.css'
import {Link} from "react-router-dom"

const checkAmountURL = 'http://localhost:8000/check-amount/';

const CheckMoneyLabel = ({cardNumber, pin}) => {
    const [amount, setAmount] = useState(0);

    return (
        <div className={classes.container}>
            <label className={classes.checkAmount}>{amount}</label>
            <div>
                <button className={classes.checkBtn} type={"submit"} onClick={() => {
                    axios.get(checkAmountURL, {
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'cardNumber': cardNumber,
                            'PIN': pin
                        }}).then(s => {
                        setAmount(s.data.amount);

                        return s.data;
                    })}}><Link className={classes.link} to='/header'>Submit</Link></button>
            </div>
        </div>
    );
}

export default CheckMoneyLabel;