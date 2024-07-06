#!/bin/bash

echo -n "Enter the name of a command: "
read _command

case $_command in

  create_v_env)
    echo -n "create_v_env"
    pip install virtualenv && virtualenv .venv
    # Or
    # python3 -m venv .venv
    ;;

  activate_v_env)
    echo -n "activate_v_env"
    .venv\Scripts\activate
    # Or
    # source .venv/bin/activate
    ;;

  deactivate_v_env)
    echo -n "deactivate_v_env"
    deactivate
    ;;

  install)
    echo -n "install"
    pip install -r requirements/base.txt
    ;;

  packs)
    echo -n "packs"
    pip list
    ;;

  dev)
    echo -n "dev"
    cd app ; uvicorn main:app --host 127.0.0.1 --port 8000 --reload ; cd .. 
    ;;

  cleanCache)
    echo -n "clean cache"
    find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf
    ;;

  *)
    echo -n "unknown"
    ;;
esac


    ## To automatically generate a migration script based on your model changes, run:
    # alembic revision --autogenerate -m "Create tables"
    ## To apply the generated migrations to your database, execute:
    # alembic upgrade head


    # # ALEMBIC
    # Display the current revision for a database: alembic current.
    # View migrations history: alembic history --verbose.
    # Revert all migrations:alembic downgrade base.
    # Revert migrations one by one: alembic downgrade -1.
    # Apply all migrations:alembic upgrade head.
    # Apply migrations one by one: alembic upgrade +1.
    # Display all raw SQL: alembic upgrade head --sql.
    # Reset the database: alembic downgrade base && alembic upgrade head.