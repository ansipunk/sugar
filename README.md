# Running

Fairly straightforward.

```sh
docker-compose build
docker-compose up -d db # Wait for database initialization
docker-compose up -d api # Start the application itself
docker-compose run api python manage.py migrate # Run migrations
```

# Coding challenge for a certain company

## Models

- `Wallet` (id, label, balance)
- `Transaction` (id, wallet_id (fk), txid, amount)

Where `txid` is a required unique string field, `amount` is a number with 18-digits
precision, `label` is a string field, `balance` is a summary of all transactions’s
amounts. Transaction amount may be negative. Wallet balance should NEVER be negative.

### Filters

#### Wallet

- `label` - equals to, within a set, not within a set
- `balance` - lower than, higher than, equals to, within a range, not within a range

#### Transaction

- `wallet_id` - equals to, within a set, not within a set
- `amount` - lower than, higher than, equals to, within a range, not within a range

### Sorting fields

#### Wallet

- `balance`

#### Transaction

- `amount`

API specification – `JSON:API` — A specification for building APIs in JSON (you are
free to use plugin https://django-rest-framework-json-api.readthedocs.io/en/stable/)

### Will be your advantage:

- [ ] Test coverage
- [ ] SQLAlchemy migrations is an option
          No reason for those as we use Django ORM and Django migrations.
	      Otherwise I'd use Alembic.
- [x] Any linter usage
- [x] Quick start app guide if you create your own docker-compose or Dockerfiles
- [x] Comments in non-standart places in code
- [x] Use database indexes if you think it's advisable
