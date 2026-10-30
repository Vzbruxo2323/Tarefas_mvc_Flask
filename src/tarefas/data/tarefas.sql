CREATE DATABASE IS NOT `tarefas`

USE `tarefas`;



CRAETE TABLE IF NOT EXISTS `tarefa`(
    `id_tarefa` INT NOT NULL AUTO_INCRMENT PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusao` DATETIME NULL
);