-- 556099 - Felipe Melo de Sousa
-- 556629 - Leonardo Matheus Teixeira
-- 557252 - Marcos Vinicius Pereira de Oliveira

-- EXERCÍCIOS DA MATÉRIA DE DATABASE

-- Primeira Consulta
SELECT 
    tf.nome AS TIPOFONTE,
    COUNT(ps.id_projeto) AS QUANTIDADEPROJETOS
FROM 
    PF0645.projetos_sustentaveis ps
JOIN 
    PF0645.tipo_fontes tf ON ps.id_tipo_fonte = tf.id_tipo_fonte
GROUP BY 
    tf.nome
HAVING 
    COUNT(ps.id_projeto) > 2
ORDER BY 
    tf.nome;

-- Segunda Consulta
SELECT 
    id_projeto, 
    descricao, 
    custo
FROM 
    PF0645.projetos_sustentaveis
WHERE 
    id_tipo_fonte = 1
    OR id_tipo_fonte = 2
ORDER BY 
    descricao ASC;

-- Terceira Consulta
SELECT
    id_projeto, 
    descricao, 
    status
FROM 
    PF0645.projetos_sustentaveis
WHERE 
    custo > 500000 
    AND status = 'Em andamento'
ORDER BY 
    id_projeto ASC;

-- Quarta Consulta
SELECT 
    r.nome AS regiao,
    ROUND(AVG(p.custo), 2) AS mediacusto
FROM 
    PF0645.projetos_sustentaveis p
JOIN 
    PF0645.regioes_sustentaveis r ON p.id_regiao = r.id_regiao
GROUP BY 
    r.nome
ORDER BY 
    mediacusto DESC;

-- Quinta Consulta
SELECT 
    r.nome AS regiao,
    t.nome AS tipofonte,
    COUNT(p.id_projeto) AS quantidadetotalprojetos,
    ROUND(AVG(e.emissao), 2) AS mediaemissaocarbono
FROM 
    PF0645.projetos_sustentaveis p
JOIN 
    PF0645.regioes_sustentaveis r ON p.id_regiao = r.id_regiao
JOIN 
    PF0645.tipo_fontes t ON p.id_tipo_fonte = t.id_tipo_fonte
JOIN 
    PF0645.emissoes_carbono e ON p.id_tipo_fonte = e.id_tipo_fonte
GROUP BY 
    r.nome, t.nome
HAVING 
    AVG(e.emissao) > 5000
ORDER BY 
    r.nome ASC, 
    t.nome ASC;



