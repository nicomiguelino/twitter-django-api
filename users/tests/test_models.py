from django.contrib.auth import get_user_model


def assert_user(user, create_args, is_superuser):
    assert user.is_superuser == is_superuser
    assert user.tweets.count() == 0

    for field, value in create_args.items():
        assert getattr(user, field) == value


def test_create_superuser_account_success(db):
    create_args = {
        'username': 'mark.zuckerberg',
        'email': 'mark.zuckerberg@harvard.edu',
        'first_name': 'Mark',
        'last_name': 'Zuckerberg',
    }

    user = get_user_model().objects.create_superuser(**create_args)
    assert_user(user, create_args, is_superuser=True)


def test_create_user_account_success(db):
    create_args = {
        'username': 'eduardo.saverin',
        'email': 'eduardo.averin@harvard.edu',
        'first_name': 'Eduardo',
        'last_name': 'Saverin',
    }

    user = get_user_model().objects.create_user(**create_args)
    assert_user(user, create_args, is_superuser=False)
