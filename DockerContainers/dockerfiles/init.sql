SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for test
-- ----------------------------


DROP TABLE IF EXISTS `author`;
CREATE TABLE `author` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    primary key (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `quote`;
CREATE TABLE `quote` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `text` varchar(1500) NOT NULL,
    primary key (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `tags`;
CREATE TABLE `tags` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `tag` varchar(100) NOT NULL,
    `link` varchar(50) NOT NULL,
    primary key (`id`)

) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `quote_tag`;
CREATE TABLE `quote_tag`(
    `quote_id` int(11) NOT NULL,
    `tag_id` int(11) NOT NULL,
    CONSTRAINT `quote_fk`
        FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT `tag_fk`
        FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    primary key (`quote_id`, `tag_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `quote_author`;
CREATE TABLE `quote_author`(
    `quote_id` int(11) NOT NULL,
    `author_id` int(11) NOT NULL,
    CONSTRAINT `quote_fk`
        FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT `author_fk`
        FOREIGN KEY (`author_id`) REFERENCES `author` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    primary key (`quote_id`, `author_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;
