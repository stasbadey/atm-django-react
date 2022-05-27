CREATE UNIQUE INDEX IF NOT EXISTS indx_card_number ON card(card_number) INCLUDE (pin);

--todo create domain with exp_date
CREATE DOMAIN date_checker AS TIMESTAMP
CHECK(EXTRACT(YEAR FROM VALUE)::INT > EXTRACT(YEAR FROM current_timestamp)::INT)
CREATE TABLE card(
    id              int GENERATED ALWAYS AS IDENTITY NOT NULL UNIQUE,
    card_number     varchar(255)                                    NOT NULL UNIQUE,
    pin             varchar(255)                                    NOT NULL UNIQUE,
    amount_of_cash  decimal        DEFAULT 0,
    expiration_date varchar(255)                                   NOT NULL CHECK(expiration_date >= to_char(current_timestamp, 'MM-YY'))
);
