import AddCardInput from "./Component/AddCardInput";
import {useState} from "react";
import RefillCardInput from "./Component/RefillCardInput";
import CheckMoneyLabel from "./Component/CheckMoneyLabel";
import TransferInput from "./Component/TransferInput";
import WithdrawLabel from "./Component/WithdrawLabel";
import {Route, Link, Routes, BrowserRouter} from "react-router-dom";
import Header from "./Component/Header";

function App() {
  const [cardNumber, setCardNumber] = useState('');
  const [pin, setPin] = useState('')

  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
            <Route path="/" element={<AddCardInput />} />
            <Route path='/header' element={<Header />} />
            <Route path='/updatecash' element={<RefillCardInput />} />
            <Route path='/checkbalance' element={<CheckMoneyLabel />} />
            <Route path='/transfer' element={<TransferInput />} />
            <Route path='/withdrow' element={<WithdrawLabel />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
