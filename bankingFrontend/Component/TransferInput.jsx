import {useState} from "react";
import TransferCardInput from "./TransferCardInput";
import axios from "axios";
import classes from './CSSModules/TransferInput.module.css'
import { Link } from "react-router-dom";

const transferURL = 'http://localhost:8000/transfer/';

const TransferInput = ({cardNumber, pin}) => {
    const [participantCardNumber, setParticipantCardNumber] = useState('');
    const [transferAmount, setTransferAmount] = useState(0);
    const [responseData, setResponseData] = useState(null);

    return (
        <div className={classes.container}>
            <label className={classes.transferLabel}>{responseData}</label>
            <div>
                <input className={classes.transferLabel} value={participantCardNumber} onInput={s => setParticipantCardNumber(s.target.value)} name={'participant card number'}/>
                <TransferCardInput transferAmount={transferAmount} setTransferAmount={setTransferAmount}/>
                <button className={classes.submitBtn} type={"submit"} onClick={() => {
                    const data = {
                        'amount': transferAmount,
                        'cardToTransfer': participantCardNumber
                    }
                    return axios.post(transferURL, data, {
                        headers: {
                            'Content-Type': 'application/json',
                            'cardNumber': cardNumber,
                            'PIN': pin
                        }
                    }).then(s => {
                        setResponseData(s.data.updatedChecksum);

                        return s.data;
                    })
                        .catch(err => console.error(err));
                }}><Link className={classes.link} to='/header'>Submit</Link></button>
            </div>
        </div>
    );
}

export default TransferInput;