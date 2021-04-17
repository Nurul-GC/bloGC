# este arquivo contem as indicações para a auto-criação da pasta
# './migrations'
# onde estarão as configurações gerais da db

# abra o terminal e navegue ate a pasta actual
cd ..
# e defina primeiro a constante
export FLASK_APP='index.py'
# para o projecto actual e em seguida execute o comando
flask db init

# The `flask db migrate` command
# does not make any changes to the database
# it just generates the migration script.
# To apply the changes to the database
# the `flask db upgrade` command must be used.
