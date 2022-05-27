import classes from './CSSModules/TransferCardInput.module.css'

const TransferCardInput = ({transferAmount, setTransferAmount}) => {
    function incrementAmount() {
        setTransferAmount(transferAmount + 1);
    }

    function decrementAmount() {
        setTransferAmount(transferAmount - 1);
    }

    return (
        <>
            <button className={classes.transferBtn} onClick={decrementAmount}>-</button>
            <span className={classes.transferAmount}>{transferAmount}</span>
            <button className={classes.transferBtn} onClick={incrementAmount}>+</button>
        </>
    );
}

export default TransferCardInput;