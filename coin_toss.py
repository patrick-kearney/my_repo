# fit binomial model in stan for coin toss

import stan
import pandas
import arviz as az


n_code = """
data {
    int<lower=0> n; // number of tosses
    int<lower=0> y; // number of heads
}
transformed data {}
parameters {
    real<lower=0, upper=1> p;
}
transformed parameters {}
model {
    p ~ beta(2, 2);
    y ~ binomial(n, p);
}
generated quantities {}
"""

coin_dat = {
             'n': 100,
             'y': 61,
            }

model_fit = stan.build(n_code, data= coin_dat)

fit = model_fit.sample(num_chains = 4, num_samples = 1000)
df = fit.to_frame()
print(df)
print(df.describe().T)

az.summary.fit
