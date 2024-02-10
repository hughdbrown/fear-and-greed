# Description
Short test of CNN fear and greed data.

# Data
Can be pulled from:
```
https://production.dataviz.cnn.io/index/fearandgreed/graphdata/<DATE>
```
where DATE is `yyyy-mm-dd`. You have to do this in a browser.

```
❯ curl https://production.dataviz.cnn.io/index/fearandgreed/graphdata/2020-07-15
I'm a teapot. You're a bot.%
```

The data quality seems quite poor until January of 2021.

# Setup
Run `setup.sh`. It makes a python virtualenv for the project and populates it with python dependencies.
