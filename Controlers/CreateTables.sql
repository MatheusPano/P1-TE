create table tb_user(
id  serial primary key,
usuario varchar(20),
senha varchar(20),
email varchar(50),
telefone varchar(12),
sexo varchar(1),
data_nascimento date,
created date
);

create table tb_mural (
id SERIAL primary key,
nome varchar(20),
created date
);

create table tb_lembrete(
id SERIAL primary key,
id_mural int,
nome varchar(20),
descrição varchar(200),
created date,
constraint fk_mural foreign key(id_mural) references tb_mural(id) 
);

drop table tb_user;
select * from tb_user tu;
insert into tb_user(usuario, senha, email, telefone, sexo, data_nascimento, created)
values ('Ari', 'senha', 'ari@email.com', '9991447511', 'M', '2002-08-15', '2022-11-27');
