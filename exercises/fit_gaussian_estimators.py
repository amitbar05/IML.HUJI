from IMLearn.learners import UnivariateGaussian, MultivariateGaussian
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "simple_white"


def test_univariate_gaussian():
    # Question 1 - Draw samples and print fitted model
    num_samples = 1000
    real_expectation = 10
    real_variance = 1
    samples = np.random.normal(real_expectation, real_variance, num_samples)
    sample_mean_estimator = np.mean(samples)
    sample_variance_estimator = np.var(samples, ddof=1)
    print(sample_mean_estimator, sample_variance_estimator)

    # Question 2 - Empirically showing sample mean is consistent
    step_increase = 10
    sample_size_data = []
    mean_diff_data = []
    for step_number in range(1, int(num_samples / step_increase) + 1):
        temp_sample_size = step_number * 10
        temp_sample = samples[:temp_sample_size]
        sample_size_data.append(temp_sample_size)
        mean_diff_data.append(abs(np.mean(temp_sample) - real_expectation))
    # need to plot the data

    layout = go.Layout(title=r"$\text{Absolute Difference Between the Estimation of the Expectation and the Real Expectation}$",
                               xaxis_title="$m\\text{ - number of samples}$",
                               yaxis_title=r"$\epsilon\text{ - estimation error}$",
                               height=600)
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=sample_size_data, y=mean_diff_data, fill='tonexty', mode='lines', marker=dict(color="blue"), showlegend=False))
    fig.show()
    raise NotImplementedError()

    # Question 3 - Plotting Empirical PDF of fitted model
    raise NotImplementedError()


def test_multivariate_gaussian():
    # Question 4 - Draw samples and print fitted model
    raise NotImplementedError()

    # Question 5 - Likelihood evaluation
    raise NotImplementedError()

    # Question 6 - Maximum likelihood
    raise NotImplementedError()


if __name__ == '__main__':
    np.random.seed(0)
    test_univariate_gaussian()
    test_multivariate_gaussian()
