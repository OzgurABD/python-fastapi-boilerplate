#!/bin/bash

echo -n "Enter the name of a command: "
read _command

case $_command in

  createPVE)
    echo -n "createPVE"
    pip install virtualenv && virtualenv .venv
    ;;

  activatePVE)
    echo -n "activatePVE"
    .venv\Scripts\activate
    ;;

  deactivatePVE)
    echo -n "deactivatePVE"
    deactivate
    ;;

  *)
    echo -n "unknown"
    ;;
esac


    # pip list
    # pip install -r requirements/base.txt


    # # ALEMBIC
    # Display the current revision for a database: alembic current.
    # View migrations history: alembic history --verbose.
    # Revert all migrations:alembic downgrade base.
    # Revert migrations one by one: alembic downgrade -1.
    # Apply all migrations:alembic upgrade head.
    # Apply migrations one by one: alembic upgrade +1.
    # Display all raw SQL: alembic upgrade head --sql.
    # Reset the database: alembic downgrade base && alembic upgrade head.