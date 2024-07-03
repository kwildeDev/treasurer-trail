CREATE TABLE `Transaction` (
  `transaction_id` bigint PRIMARY KEY,
  `transaction_date` date,
  `description` text,
  `amount` decimal(12,2),
  `party_id` bigint,
  `category` varchar(255),
  `user` bigint,
  `transaction_type` char(5)
);

CREATE TABLE `Account` (
  `account_id` bigint PRIMARY KEY,
  `account_name` varchar(50),
  `description` text,
  `account_type` varchar(50),
  `balance` decimal(12,2)
);

CREATE TABLE `Party` (
  `party_id` bigint PRIMARY KEY,
  `party_name` varchar(255),
  `party_type` varchar(50),
  `contact_details` text
);

CREATE TABLE `JournalEntries` (
  `journal_entry_id` bigint PRIMARY KEY,
  `transaction` bigint,
  `entry_date` date,
  `account` bigint,
  `debit_amount` decimal(12,2),
  `credit_amount` decimal(12,2)
);

ALTER TABLE `Transaction` ADD FOREIGN KEY (`party_id`) REFERENCES `Party` (`party_id`);

ALTER TABLE `JournalEntries` ADD FOREIGN KEY (`transaction`) REFERENCES `Transaction` (`transaction_id`);

ALTER TABLE `JournalEntries` ADD FOREIGN KEY (`account`) REFERENCES `Account` (`account_id`);
