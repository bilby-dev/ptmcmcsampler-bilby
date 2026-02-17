# ptmcmcsampler-bilby

Plugin for using [PTMCMCSampler](https://github.com/nanograv/PTMCMCSampler) with bilby.

This plugin exposes the `ptmcmcsampler` sampler via the `bilby.samplers` entry point.
Once installed, you can select it in `bilby.run_sampler` using `sampler='ptmcmcsampler'`.

## Installation

The package can be install using pip

```
pip install ptmcmcsampler-bilby
```

or conda

```
conda install conda-forge:ptmcmcsampler-bilby
```
