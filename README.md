# SANEA-
Projeto de sistema de denúncias Sanea + em Python
# 🚰 Sanea+

Sistema desenvolvido em Python para registro e gerenciamento de denúncias relacionadas a problemas de saneamento.

O projeto tem como objetivo permitir que usuários registrem ocorrências envolvendo água, esgoto, lixo e outros problemas relacionados à infraestrutura e ao saneamento básico.

---

## 📌 Sobre o projeto

O Sanea+ foi desenvolvido como uma aplicação executada pelo terminal.

O sistema permite registrar denúncias contendo informações como:

- Descrição do problema
- Local da ocorrência
- Tipo do problema
- Data e hora do registro
- Status da denúncia

Os dados são armazenados em um arquivo JSON, permitindo que as informações permaneçam salvas mesmo após o encerramento do programa.

---

## ⚙️ Funcionalidades

O sistema possui as seguintes funcionalidades:

- 📝 Registrar uma nova denúncia
- 📋 Listar todas as denúncias cadastradas
- 🔄 Alterar o status de uma denúncia
- 🗑️ Remover uma denúncia
- 💾 Salvar os dados automaticamente em JSON
- 🕒 Registrar automaticamente a data e hora da ocorrência

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **JSON**
- **Datetime**
- **Manipulação de arquivos**

---

## 📂 Armazenamento dos dados

As denúncias são armazenadas no arquivo:

```text
denuncias.json
