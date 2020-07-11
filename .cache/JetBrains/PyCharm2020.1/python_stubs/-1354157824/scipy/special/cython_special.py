# encoding: utf-8
# module scipy.special.cython_special
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/special/cython_special.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
"""
.. highlight:: cython

Cython API for Special Functions
================================

Scalar, typed versions of many of the functions in ``scipy.special``
can be accessed directly from Cython; the complete list is given
below. Functions are overloaded using Cython fused types so their
names match their ufunc counterpart. The module follows the following
conventions:

- If a function's ufunc counterpart returns multiple values, then the
  function returns its outputs via pointers in the final arguments
- If a function's ufunc counterpart returns a single value, then the
  function's output is returned directly.

The module is usable from Cython via::

    cimport scipy.special.cython_special

Error Handling
--------------

Functions can indicate an error by returning ``nan``; however they
cannot emit warnings like their counterparts in ``scipy.special``.

Available Functions
-------------------

- :py:func:`~scipy.special.cbrt`::

        double cbrt(double)

- :py:func:`~scipy.special.k0e`::

        double k0e(double)

- :py:func:`~scipy.special.nctdtridf`::

        double nctdtridf(double, double, double)

- :py:func:`~scipy.special.pbwa`::

        void pbwa(double, double, double *, double *)

- :py:func:`~scipy.special.sici`::

        void sici(double complex, double complex *, double complex *)
        void sici(double, double *, double *)

- :py:func:`~scipy.special.cosdg`::

        double cosdg(double)

- :py:func:`~scipy.special.eval_hermitenorm`::

        double eval_hermitenorm(long, double)

- :py:func:`~scipy.special.k0`::

        double k0(double)

- :py:func:`~scipy.special.kolmogorov`::

        double kolmogorov(double)

- :py:func:`~scipy.special.beip`::

        double beip(double)

- :py:func:`~scipy.special.cotdg`::

        double cotdg(double)

- :py:func:`~scipy.special.bdtrik`::

        double bdtrik(double, double, double)

- :py:func:`~scipy.special.ellipkinc`::

        double ellipkinc(double, double)

- :py:func:`~scipy.special.ellipe`::

        double ellipe(double)

- :py:func:`~scipy.special.hankel1e`::

        double complex hankel1e(double, double complex)

- :py:func:`~scipy.special.kelvin`::

        void kelvin(double, double complex *, double complex *, double complex *, double complex *)

- :py:func:`~scipy.special.exp2`::

        double exp2(double)

- :py:func:`~scipy.special.nbdtrin`::

        double nbdtrin(double, double, double)

- :py:func:`~scipy.special.k1e`::

        double k1e(double)

- :py:func:`~scipy.special.smirnovi`::

        double smirnovi(long, double)
        double smirnovi(double, double)

- :py:func:`~scipy.special.jve`::

        double complex jve(double, double complex)
        double jve(double, double)

- :py:func:`~scipy.special.gdtria`::

        double gdtria(double, double, double)

- :py:func:`~scipy.special.eval_hermite`::

        double eval_hermite(long, double)

- :py:func:`~scipy.special.pro_ang1_cv`::

        void pro_ang1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.log_ndtr`::

        double log_ndtr(double)
        double complex log_ndtr(double complex)

- :py:func:`~scipy.special.expit`::

        long double expit(long double)
        float expit(float)
        double expit(double)

- :py:func:`~scipy.special.iti0k0`::

        void iti0k0(double, double *, double *)

- :py:func:`~scipy.special.itstruve0`::

        double itstruve0(double)

- :py:func:`~scipy.special.ellipkm1`::

        double ellipkm1(double)

- :py:func:`~scipy.special.mathieu_modsem2`::

        void mathieu_modsem2(double, double, double, double *, double *)

- :py:func:`~scipy.special.stdtrit`::

        double stdtrit(double, double)

- :py:func:`~scipy.special.ncfdtr`::

        double ncfdtr(double, double, double, double)

- :py:func:`~scipy.special.chdtri`::

        double chdtri(double, double)

- :py:func:`~scipy.special.pro_cv`::

        double pro_cv(double, double, double)

- :py:func:`~scipy.special.gammaincc`::

        double gammaincc(double, double)

- :py:func:`~scipy.special.pdtri`::

        double pdtri(long, double)
        double pdtri(double, double)

- :py:func:`~scipy.special.expi`::

        double expi(double)
        double complex expi(double complex)

- :py:func:`~scipy.special.eval_sh_chebyu`::

        double complex eval_sh_chebyu(double, double complex)
        double eval_sh_chebyu(long, double)
        double eval_sh_chebyu(double, double)

- :py:func:`~scipy.special.modstruve`::

        double modstruve(double, double)

- :py:func:`~scipy.special.btdtria`::

        double btdtria(double, double, double)

- :py:func:`~scipy.special.hankel1`::

        double complex hankel1(double, double complex)

- :py:func:`~scipy.special.log1p`::

        double log1p(double)
        double complex log1p(double complex)

- :py:func:`~scipy.special.stdtr`::

        double stdtr(double, double)

- :py:func:`~scipy.special.jv`::

        double complex jv(double, double complex)
        double jv(double, double)

- :py:func:`~scipy.special.obl_cv`::

        double obl_cv(double, double, double)

- :py:func:`~scipy.special.hankel2`::

        double complex hankel2(double, double complex)

- :py:func:`~scipy.special.eval_genlaguerre`::

        double eval_genlaguerre(double, double, double)
        double eval_genlaguerre(long, double, double)
        double complex eval_genlaguerre(double, double, double complex)

- :py:func:`~scipy.special.binom`::

        double binom(double, double)

- :py:func:`~scipy.special.modfresnelm`::

        void modfresnelm(double, double complex *, double complex *)

- :py:func:`~scipy.special.pro_rad1_cv`::

        void pro_rad1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.kn`::

        double kn(long, double)
        double kn(double, double)

- :py:func:`~scipy.special.ncfdtrinc`::

        double ncfdtrinc(double, double, double, double)

- :py:func:`~scipy.special.pdtr`::

        double pdtr(double, double)

- :py:func:`~scipy.special.obl_rad2`::

        void obl_rad2(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.tandg`::

        double tandg(double)

- :py:func:`~scipy.special.ellipj`::

        void ellipj(double, double, double *, double *, double *, double *)

- :py:func:`~scipy.special.mathieu_modsem1`::

        void mathieu_modsem1(double, double, double, double *, double *)

- :py:func:`~scipy.special.besselpoly`::

        double besselpoly(double, double, double)

- :py:func:`~scipy.special.y0`::

        double y0(double)

- :py:func:`~scipy.special.modfresnelp`::

        void modfresnelp(double, double complex *, double complex *)

- :py:func:`~scipy.special.huber`::

        double huber(double, double)

- :py:func:`~scipy.special.kolmogi`::

        double kolmogi(double)

- :py:func:`~scipy.special.nctdtr`::

        double nctdtr(double, double, double)

- :py:func:`~scipy.special.rgamma`::

        double rgamma(double)
        double complex rgamma(double complex)

- :py:func:`~scipy.special.pro_rad1`::

        void pro_rad1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.shichi`::

        void shichi(double complex, double complex *, double complex *)
        void shichi(double, double *, double *)

- :py:func:`~scipy.special.xlog1py`::

        double xlog1py(double, double)
        double complex xlog1py(double complex, double complex)

- :py:func:`~scipy.special.hyp1f1`::

        double hyp1f1(double, double, double)
        double complex hyp1f1(double, double, double complex)

- :py:func:`~scipy.special.airy`::

        void airy(double, double *, double *, double *, double *)
        void airy(double complex, double complex *, double complex *, double complex *, double complex *)

- :py:func:`~scipy.special.j1`::

        double j1(double)

- :py:func:`~scipy.special.betainc`::

        double betainc(double, double, double)

- :py:func:`~scipy.special.y1`::

        double y1(double)

- :py:func:`~scipy.special.eval_chebyt`::

        double eval_chebyt(double, double)
        double eval_chebyt(long, double)
        double complex eval_chebyt(double, double complex)

- :py:func:`~scipy.special.ndtri`::

        double ndtri(double)

- :py:func:`~scipy.special.obl_rad1`::

        void obl_rad1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.sindg`::

        double sindg(double)

- :py:func:`~scipy.special.i0`::

        double i0(double)

- :py:func:`~scipy.special.pro_rad2_cv`::

        void pro_rad2_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.itairy`::

        void itairy(double, double *, double *, double *, double *)

- :py:func:`~scipy.special.gdtr`::

        double gdtr(double, double, double)

- :py:func:`~scipy.special.eval_legendre`::

        double complex eval_legendre(double, double complex)
        double eval_legendre(long, double)
        double eval_legendre(double, double)

- :py:func:`~scipy.special.keip`::

        double keip(double)

- :py:func:`~scipy.special.zetac`::

        double zetac(double)

- :py:func:`~scipy.special.gdtrib`::

        double gdtrib(double, double, double)

- :py:func:`~scipy.special.chdtrc`::

        double chdtrc(double, double)

- :py:func:`~scipy.special.bdtrc`::

        double bdtrc(long, long, double)
        double bdtrc(double, double, double)

- :py:func:`~scipy.special.mathieu_modcem2`::

        void mathieu_modcem2(double, double, double, double *, double *)

- :py:func:`~scipy.special.round`::

        double round(double)

- :py:func:`~scipy.special.nbdtrik`::

        double nbdtrik(double, double, double)

- :py:func:`~scipy.special.pro_ang1`::

        void pro_ang1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.chndtrix`::

        double chndtrix(double, double, double)

- :py:func:`~scipy.special.xlogy`::

        double xlogy(double, double)
        double complex xlogy(double complex, double complex)

- :py:func:`~scipy.special.gammainccinv`::

        double gammainccinv(double, double)

- :py:func:`~scipy.special.eval_sh_chebyt`::

        double eval_sh_chebyt(double, double)
        double complex eval_sh_chebyt(double, double complex)
        double eval_sh_chebyt(long, double)

- :py:func:`~scipy.special.fdtrc`::

        double fdtrc(double, double, double)

- :py:func:`~scipy.special.hyperu`::

        double hyperu(double, double, double)

- :py:func:`~scipy.special.obl_ang1`::

        void obl_ang1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.nbdtri`::

        double nbdtri(long, long, double)
        double nbdtri(double, double, double)

- :py:func:`~scipy.special.mathieu_cem`::

        void mathieu_cem(double, double, double, double *, double *)

- :py:func:`~scipy.special.j0`::

        double j0(double)

- :py:func:`~scipy.special.ncfdtridfd`::

        double ncfdtridfd(double, double, double, double)

- :py:func:`~scipy.special.erfi`::

        double complex erfi(double complex)
        double erfi(double)

- :py:func:`~scipy.special.airye`::

        void airye(double complex, double complex *, double complex *, double complex *, double complex *)
        void airye(double, double *, double *, double *, double *)

- :py:func:`~scipy.special.expm1`::

        double expm1(double)
        double complex expm1(double complex)

- :py:func:`~scipy.special.eval_laguerre`::

        double complex eval_laguerre(double, double complex)
        double eval_laguerre(long, double)
        double eval_laguerre(double, double)

- :py:func:`~scipy.special.mathieu_sem`::

        void mathieu_sem(double, double, double, double *, double *)

- :py:func:`~scipy.special.ncfdtri`::

        double ncfdtri(double, double, double, double)

- :py:func:`~scipy.special.kerp`::

        double kerp(double)

- :py:func:`~scipy.special.exprel`::

        double exprel(double)

- :py:func:`~scipy.special.exp10`::

        double exp10(double)

- :py:func:`~scipy.special.voigt_profile`::

        double voigt_profile(double, double, double)

- :py:func:`~scipy.special.nctdtrit`::

        double nctdtrit(double, double, double)

- :py:func:`~scipy.special.eval_chebys`::

        double eval_chebys(double, double)
        double complex eval_chebys(double, double complex)
        double eval_chebys(long, double)

- :py:func:`~scipy.special.boxcox`::

        double boxcox(double, double)

- :py:func:`~scipy.special.i1e`::

        double i1e(double)

- :py:func:`~scipy.special.yv`::

        double yv(double, double)
        double complex yv(double, double complex)

- :py:func:`~scipy.special.betaincinv`::

        double betaincinv(double, double, double)

- :py:func:`~scipy.special.yve`::

        double complex yve(double, double complex)
        double yve(double, double)

- :py:func:`~scipy.special.loggamma`::

        double loggamma(double)
        double complex loggamma(double complex)

- :py:func:`~scipy.special.ellipeinc`::

        double ellipeinc(double, double)

- :py:func:`~scipy.special.rel_entr`::

        double rel_entr(double, double)

- :py:func:`~scipy.special.eval_gegenbauer`::

        double eval_gegenbauer(long, double, double)
        double complex eval_gegenbauer(double, double, double complex)
        double eval_gegenbauer(double, double, double)

- :py:func:`~scipy.special.kl_div`::

        double kl_div(double, double)

- :py:func:`~scipy.special.tklmbda`::

        double tklmbda(double, double)

- :py:func:`~scipy.special.gammasgn`::

        double gammasgn(double)

- :py:func:`~scipy.special.obl_ang1_cv`::

        void obl_ang1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.eval_chebyu`::

        double complex eval_chebyu(double, double complex)
        double eval_chebyu(double, double)
        double eval_chebyu(long, double)

- :py:func:`~scipy.special.agm`::

        double agm(double, double)

- :py:func:`~scipy.special.obl_rad2_cv`::

        void obl_rad2_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.erfc`::

        double erfc(double)
        double complex erfc(double complex)

- :py:func:`~scipy.special.boxcox1p`::

        double boxcox1p(double, double)

- :py:func:`~scipy.special.wrightomega`::

        double wrightomega(double)
        double complex wrightomega(double complex)

- :py:func:`~scipy.special.dawsn`::

        double dawsn(double)
        double complex dawsn(double complex)

- :py:func:`~scipy.special.kei`::

        double kei(double)

- :py:func:`~scipy.special.mathieu_b`::

        double mathieu_b(double, double)

- :py:func:`~scipy.special.inv_boxcox`::

        double inv_boxcox(double, double)

- :py:func:`~scipy.special.it2j0y0`::

        void it2j0y0(double, double *, double *)

- :py:func:`~scipy.special.stdtridf`::

        double stdtridf(double, double)

- :py:func:`~scipy.special.eval_jacobi`::

        double complex eval_jacobi(double, double, double, double complex)
        double eval_jacobi(long, double, double, double)
        double eval_jacobi(double, double, double, double)

- :py:func:`~scipy.special.eval_chebyc`::

        double eval_chebyc(double, double)
        double eval_chebyc(long, double)
        double complex eval_chebyc(double, double complex)

- :py:func:`~scipy.special.eval_sh_jacobi`::

        double eval_sh_jacobi(double, double, double, double)
        double eval_sh_jacobi(long, double, double, double)
        double complex eval_sh_jacobi(double, double, double, double complex)

- :py:func:`~scipy.special.chdtr`::

        double chdtr(double, double)

- :py:func:`~scipy.special.it2struve0`::

        double it2struve0(double)

- :py:func:`~scipy.special.inv_boxcox1p`::

        double inv_boxcox1p(double, double)

- :py:func:`~scipy.special.kv`::

        double complex kv(double, double complex)
        double kv(double, double)

- :py:func:`~scipy.special.bdtri`::

        double bdtri(long, long, double)
        double bdtri(double, double, double)

- :py:func:`~scipy.special.wofz`::

        double complex wofz(double complex)

- :py:func:`~scipy.special.kve`::

        double kve(double, double)
        double complex kve(double, double complex)

- :py:func:`~scipy.special.i0e`::

        double i0e(double)

- :py:func:`~scipy.special.owens_t`::

        double owens_t(double, double)

- :py:func:`~scipy.special.chndtridf`::

        double chndtridf(double, double, double)

- :py:func:`~scipy.special.pbdv`::

        void pbdv(double, double, double *, double *)

- :py:func:`~scipy.special.fresnel`::

        void fresnel(double, double *, double *)
        void fresnel(double complex, double complex *, double complex *)

- :py:func:`~scipy.special.fdtridfd`::

        double fdtridfd(double, double, double)

- :py:func:`~scipy.special.gdtrc`::

        double gdtrc(double, double, double)

- :py:func:`~scipy.special.mathieu_modcem1`::

        void mathieu_modcem1(double, double, double, double *, double *)

- :py:func:`~scipy.special.i1`::

        double i1(double)

- :py:func:`~scipy.special.berp`::

        double berp(double)

- :py:func:`~scipy.special.spence`::

        double spence(double)
        double complex spence(double complex)

- :py:func:`~scipy.special.pdtrik`::

        double pdtrik(double, double)

- :py:func:`~scipy.special.nrdtrimn`::

        double nrdtrimn(double, double, double)

- :py:func:`~scipy.special.ncfdtridfn`::

        double ncfdtridfn(double, double, double, double)

- :py:func:`~scipy.special.pseudo_huber`::

        double pseudo_huber(double, double)

- :py:func:`~scipy.special.entr`::

        double entr(double)

- :py:func:`~scipy.special.poch`::

        double poch(double, double)

- :py:func:`~scipy.special.smirnov`::

        double smirnov(long, double)
        double smirnov(double, double)

- :py:func:`~scipy.special.chndtr`::

        double chndtr(double, double, double)

- :py:func:`~scipy.special.btdtr`::

        double btdtr(double, double, double)

- :py:func:`~scipy.special.bei`::

        double bei(double)

- :py:func:`~scipy.special.eval_sh_legendre`::

        double eval_sh_legendre(double, double)
        double complex eval_sh_legendre(double, double complex)
        double eval_sh_legendre(long, double)

- :py:func:`~scipy.special.pdtrc`::

        double pdtrc(double, double)

- :py:func:`~scipy.special.gamma`::

        double gamma(double)
        double complex gamma(double complex)

- :py:func:`~scipy.special.erfcx`::

        double complex erfcx(double complex)
        double erfcx(double)

- :py:func:`~scipy.special.ber`::

        double ber(double)

- :py:func:`~scipy.special.bdtr`::

        double bdtr(long, long, double)
        double bdtr(double, double, double)

- :py:func:`~scipy.special.hyp2f1`::

        double hyp2f1(double, double, double, double)
        double complex hyp2f1(double, double, double, double complex)

- :py:func:`~scipy.special.fdtri`::

        double fdtri(double, double, double)

- :py:func:`~scipy.special.itj0y0`::

        void itj0y0(double, double *, double *)

- :py:func:`~scipy.special.pbvv`::

        void pbvv(double, double, double *, double *)

- :py:func:`~scipy.special.btdtri`::

        double btdtri(double, double, double)

- :py:func:`~scipy.special.yn`::

        double yn(long, double)
        double yn(double, double)

- :py:func:`~scipy.special.cosm1`::

        double cosm1(double)

- :py:func:`~scipy.special.obl_rad1_cv`::

        void obl_rad1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.itmodstruve0`::

        double itmodstruve0(double)

- :py:func:`~scipy.special.pro_rad2`::

        void pro_rad2(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.nctdtrinc`::

        double nctdtrinc(double, double, double)

- :py:func:`~scipy.special.ker`::

        double ker(double)

- :py:func:`~scipy.special.erf`::

        double erf(double)
        double complex erf(double complex)

- :py:func:`~scipy.special.chdtriv`::

        double chdtriv(double, double)

- :py:func:`~scipy.special.ive`::

        double ive(double, double)
        double complex ive(double, double complex)

- :py:func:`~scipy.special.nrdtrisd`::

        double nrdtrisd(double, double, double)

- :py:func:`~scipy.special.gammaln`::

        double gammaln(double)

- :py:func:`~scipy.special.expn`::

        double expn(long, double)
        double expn(double, double)

- :py:func:`~scipy.special.fdtr`::

        double fdtr(double, double, double)

- :py:func:`~scipy.special.radian`::

        double radian(double, double, double)

- :py:func:`~scipy.special.k1`::

        double k1(double)

- :py:func:`~scipy.special.gammaincinv`::

        double gammaincinv(double, double)

- :py:func:`~scipy.special.hyp0f1`::

        double hyp0f1(double, double)
        double complex hyp0f1(double, double complex)

- :py:func:`~scipy.special.hankel2e`::

        double complex hankel2e(double, double complex)

- :py:func:`~scipy.special.chndtrinc`::

        double chndtrinc(double, double, double)

- :py:func:`~scipy.special.exp1`::

        double complex exp1(double complex)
        double exp1(double)

- :py:func:`~scipy.special.sph_harm`::

        double complex sph_harm(long, long, double, double)
        double complex sph_harm(double, double, double, double)

- :py:func:`~scipy.special.nbdtrc`::

        double nbdtrc(long, long, double)
        double nbdtrc(double, double, double)

- :py:func:`~scipy.special.gammainc`::

        double gammainc(double, double)

- :py:func:`~scipy.special.nbdtr`::

        double nbdtr(long, long, double)
        double nbdtr(double, double, double)

- :py:func:`~scipy.special.it2i0k0`::

        void it2i0k0(double, double *, double *)

- :py:func:`~scipy.special.mathieu_a`::

        double mathieu_a(double, double)

- :py:func:`~scipy.special.struve`::

        double struve(double, double)

- :py:func:`~scipy.special.bdtrin`::

        double bdtrin(double, double, double)

- :py:func:`~scipy.special.lpmv`::

        double lpmv(double, double, double)

- :py:func:`~scipy.special.gdtrix`::

        double gdtrix(double, double, double)

- :py:func:`~scipy.special.beta`::

        double beta(double, double)

- :py:func:`~scipy.special.ndtr`::

        double ndtr(double)
        double complex ndtr(double complex)

- :py:func:`~scipy.special.iv`::

        double complex iv(double, double complex)
        double iv(double, double)

- :py:func:`~scipy.special.ellipk`::

        double ellipk(double)

- :py:func:`~scipy.special.psi`::

        double psi(double)
        double complex psi(double complex)

- :py:func:`~scipy.special.betaln`::

        double betaln(double, double)

- :py:func:`~scipy.special.logit`::

        long double logit(long double)
        double logit(double)
        float logit(float)

- :py:func:`~scipy.special.btdtrib`::

        double btdtrib(double, double, double)
"""

# imports
import scipy.special._ufuncs as _ufuncs # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/special/_ufuncs.cpython-35m-x86_64-linux-gnu.so
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def agm(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.agm """
    pass

def bdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtr """
    pass

def bdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtrc """
    pass

def bdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtri """
    pass

def bdtrik(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtrik """
    pass

def bdtrin(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtrin """
    pass

def bei(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bei """
    pass

def beip(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.beip """
    pass

def ber(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ber """
    pass

def berp(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.berp """
    pass

def besselpoly(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.besselpoly """
    pass

def beta(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.beta """
    pass

def betainc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.betainc """
    pass

def betaincinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.betaincinv """
    pass

def betaln(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.betaln """
    pass

def binom(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.binom """
    pass

def boxcox(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.boxcox """
    pass

def boxcox1p(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.boxcox1p """
    pass

def btdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtr """
    pass

def btdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtri """
    pass

def btdtria(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtria """
    pass

def btdtrib(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtrib """
    pass

def cbrt(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cbrt """
    pass

def chdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtr """
    pass

def chdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtrc """
    pass

def chdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtri """
    pass

def chdtriv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtriv """
    pass

def chndtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtr """
    pass

def chndtridf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtridf """
    pass

def chndtrinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtrinc """
    pass

def chndtrix(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtrix """
    pass

def cosdg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cosdg """
    pass

def cosm1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cosm1 """
    pass

def cotdg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cotdg """
    pass

def dawsn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.dawsn """
    pass

def ellipe(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipe """
    pass

def ellipeinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipeinc """
    pass

def ellipk(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipk """
    pass

def ellipkinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipkinc """
    pass

def ellipkm1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipkm1 """
    pass

def entr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.entr """
    pass

def erf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erf """
    pass

def erfc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfc """
    pass

def erfcx(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfcx """
    pass

def erfi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfi """
    pass

def eval_chebyc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebyc """
    pass

def eval_chebys(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebys """
    pass

def eval_chebyt(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebyt """
    pass

def eval_chebyu(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebyu """
    pass

def eval_gegenbauer(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_gegenbauer """
    pass

def eval_genlaguerre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_genlaguerre """
    pass

def eval_hermite(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_hermite """
    pass

def eval_hermitenorm(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_hermitenorm """
    pass

def eval_jacobi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_jacobi """
    pass

def eval_laguerre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_laguerre """
    pass

def eval_legendre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_legendre """
    pass

def eval_sh_chebyt(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_chebyt """
    pass

def eval_sh_chebyu(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_chebyu """
    pass

def eval_sh_jacobi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_jacobi """
    pass

def eval_sh_legendre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_legendre """
    pass

def exp1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exp1 """
    pass

def exp10(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exp10 """
    pass

def exp2(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exp2 """
    pass

def expi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expi """
    pass

def expit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expit """
    pass

def expm1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expm1 """
    pass

def expn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expn """
    pass

def exprel(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exprel """
    pass

def fdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtr """
    pass

def fdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtrc """
    pass

def fdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtri """
    pass

def fdtridfd(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtridfd """
    pass

def gamma(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gamma """
    pass

def gammainc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammainc """
    pass

def gammaincc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammaincc """
    pass

def gammainccinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammainccinv """
    pass

def gammaincinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammaincinv """
    pass

def gammaln(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammaln """
    pass

def gammasgn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammasgn """
    pass

def gdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtr """
    pass

def gdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtrc """
    pass

def gdtria(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtria """
    pass

def gdtrib(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtrib """
    pass

def gdtrix(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtrix """
    pass

def hankel1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel1 """
    pass

def hankel1e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel1e """
    pass

def hankel2(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel2 """
    pass

def hankel2e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel2e """
    pass

def huber(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.huber """
    pass

def hyp0f1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyp0f1 """
    pass

def hyp1f1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyp1f1 """
    pass

def hyp2f1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyp2f1 """
    pass

def hyperu(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyperu """
    pass

def i0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i0 """
    pass

def i0e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i0e """
    pass

def i1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i1 """
    pass

def i1e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i1e """
    pass

def inv_boxcox(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.inv_boxcox """
    pass

def inv_boxcox1p(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.inv_boxcox1p """
    pass

def it2struve0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.it2struve0 """
    pass

def itmodstruve0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.itmodstruve0 """
    pass

def itstruve0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.itstruve0 """
    pass

def iv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.iv """
    pass

def ive(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ive """
    pass

def j0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.j0 """
    pass

def j1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.j1 """
    pass

def jv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.jv """
    pass

def jve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.jve """
    pass

def k0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k0 """
    pass

def k0e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k0e """
    pass

def k1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k1 """
    pass

def k1e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k1e """
    pass

def kei(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kei """
    pass

def keip(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.keip """
    pass

def ker(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ker """
    pass

def kerp(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kerp """
    pass

def kl_div(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kl_div """
    pass

def kn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kn """
    pass

def kolmogi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kolmogi """
    pass

def kolmogorov(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kolmogorov """
    pass

def kv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kv """
    pass

def kve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kve """
    pass

def log1p(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.log1p """
    pass

def loggamma(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.loggamma """
    pass

def logit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.logit """
    pass

def log_ndtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.log_ndtr """
    pass

def lpmv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.lpmv """
    pass

def mathieu_a(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.mathieu_a """
    pass

def mathieu_b(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.mathieu_b """
    pass

def modstruve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.modstruve """
    pass

def nbdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtr """
    pass

def nbdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtrc """
    pass

def nbdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtri """
    pass

def nbdtrik(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtrik """
    pass

def nbdtrin(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtrin """
    pass

def ncfdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtr """
    pass

def ncfdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtri """
    pass

def ncfdtridfd(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtridfd """
    pass

def ncfdtridfn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtridfn """
    pass

def ncfdtrinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtrinc """
    pass

def nctdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtr """
    pass

def nctdtridf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtridf """
    pass

def nctdtrinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtrinc """
    pass

def nctdtrit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtrit """
    pass

def ndtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ndtr """
    pass

def ndtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ndtri """
    pass

def nrdtrimn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nrdtrimn """
    pass

def nrdtrisd(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nrdtrisd """
    pass

def obl_cv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.obl_cv """
    pass

def owens_t(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.owens_t """
    pass

def pdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtr """
    pass

def pdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtrc """
    pass

def pdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtri """
    pass

def pdtrik(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtrik """
    pass

def poch(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.poch """
    pass

def pro_cv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pro_cv """
    pass

def pseudo_huber(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pseudo_huber """
    pass

def psi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.psi """
    pass

def radian(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.radian """
    pass

def rel_entr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.rel_entr """
    pass

def rgamma(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.rgamma """
    pass

def round(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.round """
    pass

def sindg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.sindg """
    pass

def smirnov(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.smirnov """
    pass

def smirnovi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.smirnovi """
    pass

def spence(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.spence """
    pass

def sph_harm(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.sph_harm """
    pass

def stdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.stdtr """
    pass

def stdtridf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.stdtridf """
    pass

def stdtrit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.stdtrit """
    pass

def struve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.struve """
    pass

def tandg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.tandg """
    pass

def tklmbda(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.tklmbda """
    pass

def voigt_profile(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.voigt_profile """
    pass

def wofz(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.wofz """
    pass

def wrightomega(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.wrightomega """
    pass

def xlog1py(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.xlog1py """
    pass

def xlogy(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.xlogy """
    pass

def y0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.y0 """
    pass

def y1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.y1 """
    pass

def yn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.yn """
    pass

def yv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.yv """
    pass

def yve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.yve """
    pass

def zetac(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.zetac """
    pass

def _airye_pywrap(*args, **kwargs): # real signature unknown
    pass

def _airy_pywrap(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_beta_dd_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_beta_dd_py(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_exprel_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_exprel_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dD_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dd_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dD_py(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dd_py(*args, **kwargs): # real signature unknown
    pass

def _bench_loggamma_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_loggamma_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_logit_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_logit_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_d_py(*args, **kwargs): # real signature unknown
    pass

def _ellipj_pywrap(*args, **kwargs): # real signature unknown
    pass

def _fresnel_pywrap(*args, **kwargs): # real signature unknown
    pass

def _it2i0k0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _it2j0y0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _itairy_pywrap(*args, **kwargs): # real signature unknown
    pass

def _iti0k0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _itj0y0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _kelvin_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_cem_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modcem1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modcem2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modsem1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modsem2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_sem_pywrap(*args, **kwargs): # real signature unknown
    pass

def _modfresnelm_pywrap(*args, **kwargs): # real signature unknown
    pass

def _modfresnelp_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_ang1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_ang1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad2_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pbdv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pbvv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pbwa_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_ang1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_ang1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad2_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _shichi_pywrap(*args, **kwargs): # real signature unknown
    pass

def _sici_pywrap(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260030fda0>'

__pyx_capi__ = {
    '__pyx_fuse_0_0eval_chebyc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327b70>'
    '__pyx_fuse_0_0eval_chebys': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327630>'
    '__pyx_fuse_0_0eval_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003270f0>'
    '__pyx_fuse_0_0eval_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003278d0>'
    '__pyx_fuse_0_0eval_gegenbauer': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327810>'
    '__pyx_fuse_0_0eval_genlaguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326db0>'
    '__pyx_fuse_0_0eval_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327ab0>'
    '__pyx_fuse_0_0eval_laguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327570>'
    '__pyx_fuse_0_0eval_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003271b0>'
    '__pyx_fuse_0_0eval_sh_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327330>'
    '__pyx_fuse_0_0eval_sh_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326c30>'
    '__pyx_fuse_0_0eval_sh_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327c30>'
    '__pyx_fuse_0_0eval_sh_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327f30>'
    '__pyx_fuse_0_1eval_chebyc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327ba0>'
    '__pyx_fuse_0_1eval_chebys': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327660>'
    '__pyx_fuse_0_1eval_chebyt': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327120>'
    '__pyx_fuse_0_1eval_chebyu': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327900>'
    '__pyx_fuse_0_1eval_gegenbauer': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327840>'
    '__pyx_fuse_0_1eval_genlaguerre': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326de0>'
    '__pyx_fuse_0_1eval_jacobi': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327ae0>'
    '__pyx_fuse_0_1eval_laguerre': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003275a0>'
    '__pyx_fuse_0_1eval_legendre': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003271e0>'
    '__pyx_fuse_0_1eval_sh_chebyt': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327360>'
    '__pyx_fuse_0_1eval_sh_chebyu': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326c60>'
    '__pyx_fuse_0_1eval_sh_jacobi': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327c60>'
    '__pyx_fuse_0_1eval_sh_legendre': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327f60>'
    '__pyx_fuse_0airy': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f2600327090>'
    '__pyx_fuse_0airye': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26003274b0>'
    '__pyx_fuse_0bdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003280f0>'
    '__pyx_fuse_0bdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327270>'
    '__pyx_fuse_0bdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327d50>'
    '__pyx_fuse_0dawsn': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327a50>'
    '__pyx_fuse_0erf': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328210>'
    '__pyx_fuse_0erfc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327990>'
    '__pyx_fuse_0erfcx': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328090>'
    '__pyx_fuse_0erfi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327450>'
    '__pyx_fuse_0exp1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328390>'
    '__pyx_fuse_0expi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326bd0>'
    '__pyx_fuse_0expit': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326ae0>'
    '__pyx_fuse_0expm1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327510>'
    '__pyx_fuse_0expn': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003282d0>'
    '__pyx_fuse_0fresnel': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f2600327e10>'
    '__pyx_fuse_0gamma': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328030>'
    '__pyx_fuse_0hyp0f1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328330>'
    '__pyx_fuse_0hyp1f1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327030>'
    '__pyx_fuse_0hyp2f1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328150>'
    '__pyx_fuse_0iv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328570>'
    '__pyx_fuse_0ive': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328270>'
    '__pyx_fuse_0jv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326d50>'
    '__pyx_fuse_0jve': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326a20>'
    '__pyx_fuse_0kn': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326e70>'
    '__pyx_fuse_0kv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327cf0>'
    '__pyx_fuse_0kve': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327db0>'
    '__pyx_fuse_0log1p': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326cf0>'
    '__pyx_fuse_0log_ndtr': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326a80>'
    '__pyx_fuse_0loggamma': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003277b0>'
    '__pyx_fuse_0logit': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600328630>'
    '__pyx_fuse_0nbdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003284b0>'
    '__pyx_fuse_0nbdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600328450>'
    '__pyx_fuse_0nbdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003273f0>'
    '__pyx_fuse_0ndtr': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600328510>'
    '__pyx_fuse_0pdtri': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326b70>'
    '__pyx_fuse_0psi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003285d0>'
    '__pyx_fuse_0rgamma': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326ed0>'
    '__pyx_fuse_0shichi': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f2600326f30>'
    '__pyx_fuse_0sici': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f2600326960>'
    '__pyx_fuse_0smirnov': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327ed0>'
    '__pyx_fuse_0smirnovi': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003269c0>'
    '__pyx_fuse_0spence': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327e70>'
    '__pyx_fuse_0sph_harm': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f26003283f0>'
    '__pyx_fuse_0wrightomega': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003279f0>'
    '__pyx_fuse_0xlog1py': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326f90>'
    '__pyx_fuse_0xlogy': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003272d0>'
    '__pyx_fuse_0yn': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003281b0>'
    '__pyx_fuse_0yv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003276f0>'
    '__pyx_fuse_0yve': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327750>'
    '__pyx_fuse_1_0eval_chebyc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327bd0>'
    '__pyx_fuse_1_0eval_chebys': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327690>'
    '__pyx_fuse_1_0eval_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327150>'
    '__pyx_fuse_1_0eval_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327930>'
    '__pyx_fuse_1_0eval_gegenbauer': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327870>'
    '__pyx_fuse_1_0eval_genlaguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326e10>'
    '__pyx_fuse_1_0eval_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327b10>'
    '__pyx_fuse_1_0eval_laguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003275d0>'
    '__pyx_fuse_1_0eval_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327210>'
    '__pyx_fuse_1_0eval_sh_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327390>'
    '__pyx_fuse_1_0eval_sh_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600326c90>'
    '__pyx_fuse_1_0eval_sh_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327c90>'
    '__pyx_fuse_1_0eval_sh_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600327f90>'
    '__pyx_fuse_1_1eval_chebyc': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600327c00>'
    '__pyx_fuse_1_1eval_chebys': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f26003276c0>'
    '__pyx_fuse_1_1eval_chebyt': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600327180>'
    '__pyx_fuse_1_1eval_chebyu': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600327960>'
    '__pyx_fuse_1_1eval_gegenbauer': None, # (!) real value is '<capsule object "double (long, double, double, int __pyx_skip_dispatch)" at 0x7f26003278a0>'
    '__pyx_fuse_1_1eval_genlaguerre': None, # (!) real value is '<capsule object "double (long, double, double, int __pyx_skip_dispatch)" at 0x7f2600326e40>'
    '__pyx_fuse_1_1eval_jacobi': None, # (!) real value is '<capsule object "double (long, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327b40>'
    '__pyx_fuse_1_1eval_laguerre': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600327600>'
    '__pyx_fuse_1_1eval_legendre': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600327240>'
    '__pyx_fuse_1_1eval_sh_chebyt': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f26003273c0>'
    '__pyx_fuse_1_1eval_sh_chebyu': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600326cc0>'
    '__pyx_fuse_1_1eval_sh_jacobi': None, # (!) real value is '<capsule object "double (long, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327cc0>'
    '__pyx_fuse_1_1eval_sh_legendre': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600327fc0>'
    '__pyx_fuse_1airy': None, # (!) real value is '<capsule object "void (double, double *, double *, double *, double *)" at 0x7f26003270c0>'
    '__pyx_fuse_1airye': None, # (!) real value is '<capsule object "void (double, double *, double *, double *, double *)" at 0x7f26003274e0>'
    '__pyx_fuse_1bdtr': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0x7f2600328120>'
    '__pyx_fuse_1bdtrc': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0x7f26003272a0>'
    '__pyx_fuse_1bdtri': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0x7f2600327d80>'
    '__pyx_fuse_1dawsn': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600327a80>'
    '__pyx_fuse_1erf': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600328240>'
    '__pyx_fuse_1erfc': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003279c0>'
    '__pyx_fuse_1erfcx': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003280c0>'
    '__pyx_fuse_1erfi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600327480>'
    '__pyx_fuse_1exp1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003283c0>'
    '__pyx_fuse_1expi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326c00>'
    '__pyx_fuse_1expit': None, # (!) real value is '<capsule object "float (float, int __pyx_skip_dispatch)" at 0x7f2600326b10>'
    '__pyx_fuse_1expm1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600327540>'
    '__pyx_fuse_1expn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600328300>'
    '__pyx_fuse_1fresnel': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0x7f2600327e40>'
    '__pyx_fuse_1gamma': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600328060>'
    '__pyx_fuse_1hyp0f1': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600328360>'
    '__pyx_fuse_1hyp1f1': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600327060>'
    '__pyx_fuse_1hyp2f1': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600328180>'
    '__pyx_fuse_1iv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003285a0>'
    '__pyx_fuse_1ive': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003282a0>'
    '__pyx_fuse_1jv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326d80>'
    '__pyx_fuse_1jve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326a50>'
    '__pyx_fuse_1kn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600326ea0>'
    '__pyx_fuse_1kv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327d20>'
    '__pyx_fuse_1kve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327de0>'
    '__pyx_fuse_1log1p': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326d20>'
    '__pyx_fuse_1log_ndtr': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326ab0>'
    '__pyx_fuse_1loggamma': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003277e0>'
    '__pyx_fuse_1logit': None, # (!) real value is '<capsule object "float (float, int __pyx_skip_dispatch)" at 0x7f2600328660>'
    '__pyx_fuse_1nbdtr': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0x7f26003284e0>'
    '__pyx_fuse_1nbdtrc': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0x7f2600328480>'
    '__pyx_fuse_1nbdtri': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0x7f2600327420>'
    '__pyx_fuse_1ndtr': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600328540>'
    '__pyx_fuse_1pdtri': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600326ba0>'
    '__pyx_fuse_1psi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600328600>'
    '__pyx_fuse_1rgamma': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326f00>'
    '__pyx_fuse_1shichi': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0x7f2600326f60>'
    '__pyx_fuse_1sici': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0x7f2600326990>'
    '__pyx_fuse_1smirnov': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600327f00>'
    '__pyx_fuse_1smirnovi': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f26003269f0>'
    '__pyx_fuse_1spence': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600327ea0>'
    '__pyx_fuse_1sph_harm': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, long, double, double, int __pyx_skip_dispatch)" at 0x7f2600328420>'
    '__pyx_fuse_1wrightomega': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600327a20>'
    '__pyx_fuse_1xlog1py': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326fc0>'
    '__pyx_fuse_1xlogy': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327300>'
    '__pyx_fuse_1yn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f26003281e0>'
    '__pyx_fuse_1yv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327720>'
    '__pyx_fuse_1yve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600327780>'
    '__pyx_fuse_2expit': None, # (!) real value is '<capsule object "long double (long double, int __pyx_skip_dispatch)" at 0x7f2600326b40>'
    '__pyx_fuse_2logit': None, # (!) real value is '<capsule object "long double (long double, int __pyx_skip_dispatch)" at 0x7f2600328690>'
    'agm': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325d80>'
    'bdtrik': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600641d80>'
    'bdtrin': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326810>'
    'bei': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326330>'
    'beip': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641d20>'
    'ber': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326390>'
    'berp': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326180>'
    'besselpoly': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325450>'
    'beta': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003268a0>'
    'betainc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003255d0>'
    'betaincinv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325c30>'
    'betaln': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326900>'
    'binom': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003252a0>'
    'boxcox': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325bd0>'
    'boxcox1p': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325de0>'
    'btdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326300>'
    'btdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326450>'
    'btdtria': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003251b0>'
    'btdtrib': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326930>'
    'cbrt': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f260e159f00>'
    'chdtr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325f00>'
    'chdtrc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325810>'
    'chdtri': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003250f0>'
    'chdtriv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003265a0>'
    'chndtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003262d0>'
    'chndtridf': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326060>'
    'chndtrinc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326720>'
    'chndtrix': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325900>'
    'cosdg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641210>'
    'cosm1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326480>'
    'cotdg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641d50>'
    'ellipe': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641de0>'
    'ellipeinc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325c60>'
    'ellipj': None, # (!) real value is '<capsule object "void (double, double, double *, double *, double *, double *)" at 0x7f26003253f0>'
    'ellipk': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003268d0>'
    'ellipkinc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600641db0>'
    'ellipkm1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325030>'
    'entr': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326270>'
    'eval_hermite': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600641f30>'
    'eval_hermitenorm': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0x7f2600641c90>'
    'exp10': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325b40>'
    'exp2': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641e70>'
    'exprel': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325b10>'
    'fdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326630>'
    'fdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325960>'
    'fdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003263c0>'
    'fdtridfd': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003260c0>'
    'gammainc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326750>'
    'gammaincc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325150>'
    'gammainccinv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325930>'
    'gammaincinv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003266c0>'
    'gammaln': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326600>'
    'gammasgn': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325d20>'
    'gdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325750>'
    'gdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003260f0>'
    'gdtria': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600641f00>'
    'gdtrib': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003257e0>'
    'gdtrix': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326870>'
    'hankel1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003251e0>'
    'hankel1e': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600641e10>'
    'hankel2': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600325270>'
    'hankel2e': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f26003266f0>'
    'huber': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003254e0>'
    'hyperu': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325990>'
    'i0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003256c0>'
    'i0e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325fc0>'
    'i1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326150>'
    'i1e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325c00>'
    'inv_boxcox': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325e70>'
    'inv_boxcox1p': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325f60>'
    'it2i0k0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0x7f2600326780>'
    'it2j0y0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0x7f2600325ea0>'
    'it2struve0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325f30>'
    'itairy': None, # (!) real value is '<capsule object "void (double, double *, double *, double *, double *)" at 0x7f2600325720>'
    'iti0k0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0x7f2600641f90>'
    'itj0y0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0x7f26003263f0>'
    'itmodstruve0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003264e0>'
    'itstruve0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641fc0>'
    'j0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325a20>'
    'j1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003255a0>'
    'k0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641cc0>'
    'k0e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f260e159870>'
    'k1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326690>'
    'k1e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641ed0>'
    'kei': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325e10>'
    'keip': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325780>'
    'kelvin': None, # (!) real value is '<capsule object "void (double, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f2600641e40>'
    'ker': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600326570>'
    'kerp': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325ae0>'
    'kl_div': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325cc0>'
    'kolmogi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325510>'
    'kolmogorov': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600641cf0>'
    'lpmv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326840>'
    'mathieu_a': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003267b0>'
    'mathieu_b': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325e40>'
    'mathieu_cem': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0x7f26003259f0>'
    'mathieu_modcem1': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0x7f2600326120>'
    'mathieu_modcem2': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0x7f2600325840>'
    'mathieu_modsem1': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0x7f2600325420>'
    'mathieu_modsem2': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0x7f2600325060>'
    'mathieu_sem': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0x7f2600325a80>'
    'modfresnelm': None, # (!) real value is '<capsule object "void (double, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26003252d0>'
    'modfresnelp': None, # (!) real value is '<capsule object "void (double, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26003254b0>'
    'modstruve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325180>'
    'nbdtrik': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003258a0>'
    'nbdtrin': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600641ea0>'
    'ncfdtr': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f26003250c0>'
    'ncfdtri': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325ab0>'
    'ncfdtridfd': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325a50>'
    'ncfdtridfn': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326210>'
    'ncfdtrinc': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325330>'
    'nctdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325540>'
    'nctdtridf': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f260070b390>'
    'nctdtrinc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326540>'
    'nctdtrit': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325ba0>'
    'ndtri': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325630>'
    'nrdtrimn': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003261e0>'
    'nrdtrisd': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f26003265d0>'
    'obl_ang1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0x7f26003259c0>'
    'obl_ang1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0x7f2600325d50>'
    'obl_cv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325240>'
    'obl_rad1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0x7f2600325660>'
    'obl_rad1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0x7f26003264b0>'
    'obl_rad2': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0x7f2600325390>'
    'obl_rad2_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0x7f2600325db0>'
    'owens_t': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326030>'
    'pbdv': None, # (!) real value is '<capsule object "void (double, double, double *, double *)" at 0x7f2600326090>'
    'pbvv': None, # (!) real value is '<capsule object "void (double, double, double *, double *)" at 0x7f2600326420>'
    'pbwa': None, # (!) real value is '<capsule object "void (double, double, double *, double *)" at 0x7f26002b85d0>'
    'pdtr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325360>'
    'pdtrc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326360>'
    'pdtrik': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003261b0>'
    'poch': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003262a0>'
    'pro_ang1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0x7f26003258d0>'
    'pro_ang1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0x7f2600641f60>'
    'pro_cv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325120>'
    'pro_rad1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0x7f2600325570>'
    'pro_rad1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0x7f2600325300>'
    'pro_rad2': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0x7f2600326510>'
    'pro_rad2_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0x7f26003256f0>'
    'pseudo_huber': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600326240>'
    'radian': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600326660>'
    'rel_entr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325c90>'
    'round': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325870>'
    'sindg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325690>'
    'stdtr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325210>'
    'stdtridf': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325ed0>'
    'stdtrit': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325090>'
    'struve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f26003267e0>'
    'tandg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003253c0>'
    'tklmbda': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0x7f2600325cf0>'
    'voigt_profile': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0x7f2600325b70>'
    'wofz': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0x7f2600325f90>'
    'y0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325480>'
    'y1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f2600325600>'
    'zetac': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0x7f26003257b0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.special.cython_special', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260030fda0>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/special/cython_special.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

