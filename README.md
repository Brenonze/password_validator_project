
# Validador de Senhas (Password Validator)

Pequena aplicação para validar senhas com um conjunto de regras de negócio e uma suíte de testes unitários usando **pytest**.

## Regras de Negócio Testadas

1. A senha deve ter pelo menos 8 caracteres (`too_short`).
2. Não pode conter espaços em branco (`contains_whitespace`).
3. Deve conter pelo menos uma letra maiúscula (`missing_uppercase`).
4. Deve conter pelo menos uma letra minúscula (`missing_lowercase`).
5. Deve conter pelo menos um dígito (`missing_digit`).
6. Deve conter pelo menos um caractere especial (`missing_special`).
7. Não pode ser uma senha comum (ex.: `password`, `12345678`) (`common_password`).
8. Se a senha for `None` retorna `password_missing`.
9. Se a senha não for string retorna `password_type_invalid`.

## Como executar a aplicação e os testes

1. Crie e ative um ambiente virtual (opcional):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.\.venv\Scripts\activate # Windows (PowerShell)
```

2. Instale dependências:
```bash
pip install -r requirements.txt
```

3. Executar a suíte de testes com cobertura:
```bash
pytest --cov=app --cov-report=term --cov-report=html
```

O relatório de cobertura HTML será gerado em `htmlcov/index.html`.

## Artefatos incluídos

- Código fonte em `app/`
- Testes em `tests/`
- Relatório de cobertura gerado em `coverage.txt` e `htmlcov/`
