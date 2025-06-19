CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    status TEXT
);

INSERT INTO transactions (transaction_id, status) VALUES
('TXN123', 'VALID'),
('TXN456', 'EXPIRED'),
('TXN789', 'BLACKLISTED');
