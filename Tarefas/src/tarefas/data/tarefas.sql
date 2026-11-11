CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

CREATE TABLE IF NOT EXISTS `tarefa` (
    `id_tarefa` INT NOT NULL AUTO_INCREMENT,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusao` DATETIME NULL,
    PRIMARY KEY (`id_tarefa`)
);
