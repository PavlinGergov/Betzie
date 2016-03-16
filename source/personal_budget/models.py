from django.db import models


class Month(models.Model):
    MONTH_CHOICES = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )

    name = models.CharField(max_length=100, choices=MONTH_CHOICES)
    year = models.IntegerField()

    def get_month_balance(self):
        incomes = self.income_set.all()
        outcomes = self.outcome_set.all()

        income_sum = sum([income.value for income in incomes])
        outcome_sum = sum([outcome.value for outcome in outcomes])

        return income_sum - outcome_sum

    def __str__(self):
        return "{}, {}".format(self.name, self.year)


class Income(models.Model):
    INCOME_CATEGORY_CHOICES = (
        ('Paycheck', 'Paycheck'),
        ('Bonus', 'Bonus'),
        ('Other', 'Other'),
    )

    category = models.CharField(max_length=100, choices=INCOME_CATEGORY_CHOICES)
    month = models.ForeignKey(Month)
    name = models.CharField(max_length=100, null=True)
    value = models.IntegerField(null=True)


class Outcome(models.Model):
    OUTCOME_CATEGORY_CHOICES = (
        ('Food', 'Food'),
        ('Drinks', 'Drinks'),
        ('Entertainment', 'Entertainment'),
        ('Personal', 'Personal'),
        ('Health', 'Health'),
        ('Home', 'Home'),
        ('Clothes & Stuff', 'Clothes & Stuff'),
        ('Gifts', 'Gifts'),
        ('Taxes', 'Taxes'),
        ('Other', 'Other'),
    )

    category = models.CharField(max_length=100, choices=OUTCOME_CATEGORY_CHOICES)
    month = models.ForeignKey(Month)
    name = models.CharField(max_length=100)
    value = models.IntegerField()
