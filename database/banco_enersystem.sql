-- CRIAÇÃO DO BANCO DE DADOS PARA FAZER O CRUD DO PYTHON DO PROJETO ENERSYSTEM (2ª FIAP GLOBAL SOLUTION DE 2024 - TURMA 1TDSPW)

-- SEQUENCES para AUTO_INCREMENT
CREATE SEQUENCE seq_empresa START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_tipo_energia START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_usuario START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_plano_energia START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_consumo_usuario START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_missao START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_missao_concluida START WITH 1 INCREMENT BY 1;

-- Tabela de Empresas
CREATE TABLE tb_enersystem_empresa (
    id_empresa NUMBER PRIMARY KEY,
    nome_empresa VARCHAR2(100) NOT NULL,
    estado VARCHAR2(2) NOT NULL,
    id_tipo_energia NUMBER NOT NULL,
    custo_kwh NUMBER(5, 2),
    FOREIGN KEY (id_tipo_energia) REFERENCES tb_enersystem_tipo_energia(id_tipo_energia)
);

-- Tabela de Tipos de Energia
CREATE TABLE tb_enersystem_tipo_energia (
    id_tipo_energia NUMBER PRIMARY KEY,
    tipo_energia VARCHAR2(50) NOT NULL,
    pegada_carbono NUMBER(6, 3)
);

-- Tabela de Usuários
CREATE TABLE tb_enersystem_usuario (
    id_usuario NUMBER PRIMARY KEY,
    nome_usuario VARCHAR2(100) NOT NULL,
    email VARCHAR2(100) NOT NULL UNIQUE,
    senha VARCHAR2(100) NOT NULL,
    estado VARCHAR2(2) NOT NULL,
    id_empresa_atual NUMBER,
    FOREIGN KEY (id_empresa_atual) REFERENCES tb_enersystem_empresa(id_empresa)
);

-- Tabela de Planos de Energia Disponíveis
CREATE TABLE tb_enersystem_plano_energia (
    id_plano NUMBER PRIMARY KEY,
    nome_plano VARCHAR2(100) NOT NULL,
    id_empresa NUMBER NOT NULL,
    tipo_plano VARCHAR2(50) NOT NULL,
    custo_mensal NUMBER(8, 2),
    pegada_carbono NUMBER(6, 3),
    descricao CLOB,
    FOREIGN KEY (id_empresa) REFERENCES tb_enersystem_empresa(id_empresa)
);

-- Tabela de Consumo de Energia por Usuário
CREATE TABLE tb_enersystem_consumo_usuario (
    id_consumo NUMBER PRIMARY KEY,
    id_usuario NUMBER NOT NULL,
    mes VARCHAR2(10),
    consumo_kwh NUMBER(8, 2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES tb_enersystem_usuario(id_usuario)
);

-- Tabela de Missões e Recompensas
CREATE TABLE tb_enersystem_missao (
    id_missao NUMBER PRIMARY KEY,
    descricao_missao CLOB NOT NULL,
    pontos NUMBER NOT NULL,
    frequencia VARCHAR2(20)
);

-- Tabela de Missões Concluídas por Usuário
CREATE TABLE tb_enersystem_missao_concluida (
    id_missao_concluida NUMBER PRIMARY KEY,
    id_usuario NUMBER NOT NULL,
    id_missao NUMBER NOT NULL,
    data_conclusao DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES tb_enersystem_usuario(id_usuario),
    FOREIGN KEY (id_missao) REFERENCES tb_enersystem_missao(id_missao)
);

-- Inserções com valores explícitos em Oracle
INSERT INTO tb_enersystem_tipo_energia (id_tipo_energia, tipo_energia, pegada_carbono) VALUES 
(seq_tipo_energia.NEXTVAL, 'Renovável', 0.0);
INSERT INTO tb_enersystem_tipo_energia (id_tipo_energia, tipo_energia, pegada_carbono) VALUES 
(seq_tipo_energia.NEXTVAL, 'Não-Renovável', 0.5);

-- Exemplo de dados para tb_enersystem_empresa
INSERT INTO tb_enersystem_empresa (id_empresa, nome_empresa, estado, id_tipo_energia, custo_kwh) VALUES 
(seq_empresa.NEXTVAL, 'Energias do Futuro', 'SP', 1, 0.35);
INSERT INTO tb_enersystem_empresa (id_empresa, nome_empresa, estado, id_tipo_energia, custo_kwh) VALUES 
(seq_empresa.NEXTVAL, 'Soluções Verdes', 'RJ', 1, 0.40);
INSERT INTO tb_enersystem_empresa (id_empresa, nome_empresa, estado, id_tipo_energia, custo_kwh) VALUES 
(seq_empresa.NEXTVAL, 'Eletricity', 'MG', 2, 0.55);

-- Exemplo de dados para tb_enersystem_plano_energia
INSERT INTO tb_enersystem_plano_energia (id_plano, nome_plano, id_empresa, tipo_plano, custo_mensal, pegada_carbono, descricao) VALUES 
(seq_plano_energia.NEXTVAL, 'Plano Verde Residencial', 1, 'Residencial', 100.00, 0.0, 'Plano residencial de energia renovável com tarifa fixa mensal.');
INSERT INTO tb_enersystem_plano_energia (id_plano, nome_plano, id_empresa, tipo_plano, custo_mensal, pegada_carbono, descricao) VALUES 
(seq_plano_energia.NEXTVAL, 'Plano Sustentável Comercial', 2, 'Comercial', 500.00, 0.0, 'Plano comercial com tarifas sustentáveis.');

-- Exemplo de dados para tb_enersystem_missao
INSERT INTO tb_enersystem_missao (id_missao, descricao_missao, pontos, frequencia) VALUES 
(seq_missao.NEXTVAL, 'Economizar energia durante o horário de pico', 100, 'Diária');
INSERT INTO tb_enersystem_missao (id_missao, descricao_missao, pontos, frequencia) VALUES 
(seq_missao.NEXTVAL, 'Escolher um plano de energia renovável', 200, 'Única');
