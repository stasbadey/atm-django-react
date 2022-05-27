import TransferCardInput from "./TransferCardInput";
import {useState} from "react";
import axios from "axios";
import {format} from "react-string-format";
import {Link} from "react-router-dom"
import classes from "./CSSModules/WithdrawLabel.module.css"

const withdrawURL = 'http://localhost:8000/withdraw/?withdrawCash={0}';

const WithdrawLabel = ({cardNumber, pin}) => {
    const [transferAmount, setTransferAmount] = useState(0)
    const [updatedAmount, setUpdatedAmount] = useState(null)

    return (
      <div className={classes.container}>
          <label className={classes.withdrawAmount}>{updatedAmount}</label>
          <TransferCardInput transferAmount={transferAmount} setTransferAmount={setTransferAmount}/>
          <button className={classes.submitBtn} type={"submit"} onClick={() => {
              axios.get(format(withdrawURL, transferAmount), {
                  headers: {
                      'Content-Type': 'application/x-www-form-urlencoded',
                      'cardNumber': cardNumber,
                      'PIN': pin
                  }
              }).then(s => {
                  setUpdatedAmount(JSON.parse(s.data.amount));
                  return s.data;
              })
                  .catch(err => console.error(err));
          }}><Link className={classes.link} to='/header'>Submit</Link></button>
      </div>
    );
}

export default WithdrawLabel;