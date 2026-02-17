# ptmcmcsampler-bilby

Plugin for using ptmcmcsampler with bilby.

This plugin exposes the `ptmcmcsampler` sampler via the `bilby.samplers` entry point.
Once installed, you can select it in `bilby.run_sampler` using `sampler='ptmcmcsampler'`.
