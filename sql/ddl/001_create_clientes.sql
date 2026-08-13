CREATE TABLE IF NOT EXISTS public.clientes (
    id_cliente BIGSERIAL PRIMARY KEY,
    nome_cliente VARCHAR(150) NOT NULL,
    tipo_pessoa CHAR(1) NOT NULL,
    segmento VARCHAR(50),
    faturamento_anual NUMERIC(18,2),
    status_cliente VARCHAR(20) NOT NULL
);

INSERT INTO public.clientes (
    nome_cliente,
    tipo_pessoa,
    segmento,
    faturamento_anual,
    status_cliente
)
VALUES
    ('Atlas Comércio Ltda', 'J', 'COMÉRCIO', 2500000.00, 'ATIVO'),
    ('Minas Tecnologia S.A.', 'J', 'TECNOLOGIA', 7800000.00, 'ATIVO'),
    ('João da Silva', 'F', 'VAREJO', 120000.00, 'ATIVO'),
    ('Empresa Horizonte Ltda', 'J', 'SERVIÇOS', 4300000.00, 'INATIVO');