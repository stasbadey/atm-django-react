import React from 'react'
import { Link } from 'react-router-dom'
import classes from './CSSModules/Header.module.css'

function Header() {
  return (
    <div className={classes.header}>
        <div className={classes.headerOptions}>
            <div className={classes.headerOption}>
                <Link className={classes.headerOptionLink} to='/updatecash'>Пополнить карту</Link>
            </div>
            <div className={classes.headerOption}>
                <Link className={classes.headerOptionLink} to='/checkbalance'>Проверить баланс</Link>
            </div>
            <div className={classes.headerOption}>
                <Link className={classes.headerOptionLink} to='/transfer'>Перевсти деньги</Link>
            </div>
            <div className={classes.headerOption}>
                <Link className={classes.headerOptionLink} to='/withdrow'>Вывести средства</Link>
            </div>
        </div>
    </div>
  )
}

export default Header