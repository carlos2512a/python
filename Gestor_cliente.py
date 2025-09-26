alter table cliente
add CONSTRAINT fk_cliente_tipo
FOREIGN key (cli_tipo_id)
REFERENCES tipo(TIPO_ID)
on DELETE CASCADE
ON UPDATE CASCADE;
