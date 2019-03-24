SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `transactions`;
DROP TABLE IF EXISTS `blocks`;
DROP TABLE IF EXISTS `tokens`;


CREATE TABLE `blocks` (
  `number` int(11) NOT NULL,
  `hash` varchar(256) NOT NULL,
  `gas_limit` decimal(50,18) NOT NULL DEFAULT 0.000000000000000000,
  `gas_used` decimal(50,18) NOT NULL DEFAULT 0.000000000000000000,
  `size` int(11) NOT NULL DEFAULT 0,
  `ts` bigint(20) NOT NULL DEFAULT 0,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `transactions` (
  `id1` bigint(20) NOT NULL,
  `id2` bigint(20) NOT NULL,
  `id3` bigint(20) NOT NULL,
  `id4` bigint(20) NOT NULL,
  `block_number` int(11) NOT NULL,
  `eth_value` decimal(50,18) NOT NULL DEFAULT 0.000000000000000000,
  `from_addr` varchar(128) NOT NULL,
  `to_addr` varchar(128) NOT NULL,
  `contract` varchar(128) NOT NULL DEFAULT '0x0',
  `token_value` decimal(50,18) NOT NULL DEFAULT 0.000000000000000000,
  `succeed` tinyint(1) NOT NULL DEFAULT 0,
  `gas` decimal(50,18) NOT NULL DEFAULT 0.000000000000000000,
  `gas_price` decimal(50,18) NOT NULL DEFAULT 0.000000000000000000,
  `ts` bigint(20) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id1`,`id2`,`id3`,`id4`),
  KEY `fk_bid` (`block_number`) USING BTREE,
  CONSTRAINT `fk_bid` FOREIGN KEY (`block_number`) REFERENCES `blocks` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

 CREATE TABLE `tokens` (
  `id1` bigint(20) NOT NULL,
  `id2` bigint(20) NOT NULL,
  `id3` bigint(20) NOT NULL,
  `name` varchar(24) NOT NULL DEFAULT '',
  `decimals` smallint(6) NOT NULL DEFAULT 18,
  PRIMARY KEY (`id1`,`id2`,`id3`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `trade_tokens` (
  `id` int(11) NOT NULL,
  `address` varchar(128) NOT NULL DEFAULT '' COMMENT 'this is the hash address of the token contract,' ||
   ' for number of tokens we support will not be large, we do not split it into integers',
  `name` varchar(24) NOT NULL DEFAULT '',
  `decimals` smallint(6) NOT NULL DEFAULT 18,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `ex_pairs` (
  `pair_id` int(11) NOT NULL,
  `pair_name` varchar(96) NOT NULL,
  `left_tkid` int(11) NOT NULL,
  `right_tkid` int(11) NOT NULL,
  `price` decimal(50,18) NOT NULL DEFAULT 0.000000000000000000,
  PRIMARY KEY (`pair_id`),
  KEY `fk_ltkid` (`left_tkid`),
  KEY `fk_rtkid` (`right_tkid`),
  CONSTRAINT `fk_ltkid` FOREIGN KEY (`left_tkid`) REFERENCES `trade_tokens` (`id`),
  CONSTRAINT `fk_rtkid` FOREIGN KEY (`right_tkid`) REFERENCES `trade_tokens` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `agencies` (
  `recharge_address` varchar(128) NOT NULL,
  `name` varchar(64) NOT NULL DEFAULT '',
  `fee_rate` smallint(6) NOT NULL DEFAULT 0 COMMENT 'number of percentage this agency shall charge from every transaction',
  `fee_address` varchar(128) NOT NULL DEFAULT '',
  PRIMARY KEY (`recharge_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;