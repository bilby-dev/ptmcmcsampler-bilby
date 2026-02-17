import bilby
import pytest
from ptmcmcsampler_bilby.sampler import PTMCMCSampler


@pytest.fixture()
def SamplerClass():
    return PTMCMCSampler


@pytest.fixture()
def create_sampler(SamplerClass, bilby_gaussian_likelihood_and_priors, tmp_path):
    likelihood, priors = bilby_gaussian_likelihood_and_priors

    def create_fn(**kwargs):
        return SamplerClass(
            likelihood,
            priors,
            outdir=tmp_path / "outdir",
            label="test",
            use_ratio=False,
            **kwargs,
        )

    return create_fn


@pytest.fixture
def expected_default_kwargs():
    return dict(
        p0=None,
        Niter=2 * 10**4 + 1,
        neff=10**4,
        burn=5 * 10**3,
        verbose=True,
        ladder=None,
        Tmin=1,
        Tmax=None,
        Tskip=100,
        isave=1000,
        thin=1,
        covUpdate=1000,
        SCAMweight=1,
        AMweight=1,
        DEweight=1,
        HMCweight=0,
        MALAweight=0,
        NUTSweight=0,
        HMCstepsize=0.1,
        HMCsteps=300,
        groups=None,
        custom_proposals=None,
        loglargs={},
        loglkwargs={},
        logpargs={},
        logpkwargs={},
        logl_grad=None,
        logp_grad=None,
        outDir=None,
    )


@pytest.fixture
def sampler(create_sampler):
    return create_sampler()


def test_default_kwargs(sampler, expected_default_kwargs):
    assert sampler.kwargs == expected_default_kwargs


@pytest.mark.parametrize(
    "equiv",
    bilby.core.sampler.base_sampler.MCMCSampler.nwalkers_equiv_kwargs,
)
def test_translate_kwargs(create_sampler, equiv, expected_default_kwargs):
    expected_default_kwargs.update({"Niter": 123})
    sampler = create_sampler(**{equiv: 123})
    assert sampler.kwargs == expected_default_kwargs


@pytest.mark.parametrize(
    "equiv",
    bilby.core.sampler.base_sampler.MCMCSampler.nburn_equiv_kwargs,
)
def test_translate_burn_kwargs(create_sampler, equiv, expected_default_kwargs):
    expected_default_kwargs.update({"burn": 123})
    sampler = create_sampler(**{equiv: 123})
    assert sampler.kwargs == expected_default_kwargs
