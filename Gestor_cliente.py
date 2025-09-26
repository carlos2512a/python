alter table cliente
add CONSTRAINT fk_cliente_tipo
FOREIGN key (TIPO_ID)
REFERENCES tipo(TIP_ID)
on DELETE CASCADE
ON UPDATE CASCADE;
