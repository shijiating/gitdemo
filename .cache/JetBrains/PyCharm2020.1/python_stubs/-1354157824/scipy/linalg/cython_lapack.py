# encoding: utf-8
# module scipy.linalg.cython_lapack
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/linalg/cython_lapack.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
"""
LAPACK functions for Cython
===========================

Usable from Cython via::

    cimport scipy.linalg.cython_lapack

This module provides Cython-level wrappers for all primary routines included
in LAPACK 3.4.0 except for ``zcgesv`` since its interface is not consistent
from LAPACK 3.4.0 to 3.6.0. It also provides some of the
fixed-api auxiliary routines.

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- cbbcsd
- cbdsqr
- cgbbrd
- cgbcon
- cgbequ
- cgbequb
- cgbrfs
- cgbsv
- cgbsvx
- cgbtf2
- cgbtrf
- cgbtrs
- cgebak
- cgebal
- cgebd2
- cgebrd
- cgecon
- cgeequ
- cgeequb
- cgees
- cgeesx
- cgeev
- cgeevx
- cgehd2
- cgehrd
- cgelq2
- cgelqf
- cgels
- cgelsd
- cgelss
- cgelsy
- cgemqrt
- cgeql2
- cgeqlf
- cgeqp3
- cgeqr2
- cgeqr2p
- cgeqrf
- cgeqrfp
- cgeqrt
- cgeqrt2
- cgeqrt3
- cgerfs
- cgerq2
- cgerqf
- cgesc2
- cgesdd
- cgesv
- cgesvd
- cgesvx
- cgetc2
- cgetf2
- cgetrf
- cgetri
- cgetrs
- cggbak
- cggbal
- cgges
- cggesx
- cggev
- cggevx
- cggglm
- cgghrd
- cgglse
- cggqrf
- cggrqf
- cgtcon
- cgtrfs
- cgtsv
- cgtsvx
- cgttrf
- cgttrs
- cgtts2
- chbev
- chbevd
- chbevx
- chbgst
- chbgv
- chbgvd
- chbgvx
- chbtrd
- checon
- cheequb
- cheev
- cheevd
- cheevr
- cheevx
- chegs2
- chegst
- chegv
- chegvd
- chegvx
- cherfs
- chesv
- chesvx
- cheswapr
- chetd2
- chetf2
- chetrd
- chetrf
- chetri
- chetri2
- chetri2x
- chetrs
- chetrs2
- chfrk
- chgeqz
- chla_transtype
- chpcon
- chpev
- chpevd
- chpevx
- chpgst
- chpgv
- chpgvd
- chpgvx
- chprfs
- chpsv
- chpsvx
- chptrd
- chptrf
- chptri
- chptrs
- chsein
- chseqr
- clabrd
- clacgv
- clacn2
- clacon
- clacp2
- clacpy
- clacrm
- clacrt
- cladiv
- claed0
- claed7
- claed8
- claein
- claesy
- claev2
- clag2z
- clags2
- clagtm
- clahef
- clahqr
- clahr2
- claic1
- clals0
- clalsa
- clalsd
- clangb
- clange
- clangt
- clanhb
- clanhe
- clanhf
- clanhp
- clanhs
- clanht
- clansb
- clansp
- clansy
- clantb
- clantp
- clantr
- clapll
- clapmr
- clapmt
- claqgb
- claqge
- claqhb
- claqhe
- claqhp
- claqp2
- claqps
- claqr0
- claqr1
- claqr2
- claqr3
- claqr4
- claqr5
- claqsb
- claqsp
- claqsy
- clar1v
- clar2v
- clarcm
- clarf
- clarfb
- clarfg
- clarfgp
- clarft
- clarfx
- clargv
- clarnv
- clarrv
- clartg
- clartv
- clarz
- clarzb
- clarzt
- clascl
- claset
- clasr
- classq
- claswp
- clasyf
- clatbs
- clatdf
- clatps
- clatrd
- clatrs
- clatrz
- clauu2
- clauum
- cpbcon
- cpbequ
- cpbrfs
- cpbstf
- cpbsv
- cpbsvx
- cpbtf2
- cpbtrf
- cpbtrs
- cpftrf
- cpftri
- cpftrs
- cpocon
- cpoequ
- cpoequb
- cporfs
- cposv
- cposvx
- cpotf2
- cpotrf
- cpotri
- cpotrs
- cppcon
- cppequ
- cpprfs
- cppsv
- cppsvx
- cpptrf
- cpptri
- cpptrs
- cpstf2
- cpstrf
- cptcon
- cpteqr
- cptrfs
- cptsv
- cptsvx
- cpttrf
- cpttrs
- cptts2
- crot
- cspcon
- cspmv
- cspr
- csprfs
- cspsv
- cspsvx
- csptrf
- csptri
- csptrs
- csrscl
- cstedc
- cstegr
- cstein
- cstemr
- csteqr
- csycon
- csyconv
- csyequb
- csymv
- csyr
- csyrfs
- csysv
- csysvx
- csyswapr
- csytf2
- csytrf
- csytri
- csytri2
- csytri2x
- csytrs
- csytrs2
- ctbcon
- ctbrfs
- ctbtrs
- ctfsm
- ctftri
- ctfttp
- ctfttr
- ctgevc
- ctgex2
- ctgexc
- ctgsen
- ctgsja
- ctgsna
- ctgsy2
- ctgsyl
- ctpcon
- ctpmqrt
- ctpqrt
- ctpqrt2
- ctprfb
- ctprfs
- ctptri
- ctptrs
- ctpttf
- ctpttr
- ctrcon
- ctrevc
- ctrexc
- ctrrfs
- ctrsen
- ctrsna
- ctrsyl
- ctrti2
- ctrtri
- ctrtrs
- ctrttf
- ctrttp
- ctzrzf
- cunbdb
- cuncsd
- cung2l
- cung2r
- cungbr
- cunghr
- cungl2
- cunglq
- cungql
- cungqr
- cungr2
- cungrq
- cungtr
- cunm2l
- cunm2r
- cunmbr
- cunmhr
- cunml2
- cunmlq
- cunmql
- cunmqr
- cunmr2
- cunmr3
- cunmrq
- cunmrz
- cunmtr
- cupgtr
- cupmtr
- dbbcsd
- dbdsdc
- dbdsqr
- ddisna
- dgbbrd
- dgbcon
- dgbequ
- dgbequb
- dgbrfs
- dgbsv
- dgbsvx
- dgbtf2
- dgbtrf
- dgbtrs
- dgebak
- dgebal
- dgebd2
- dgebrd
- dgecon
- dgeequ
- dgeequb
- dgees
- dgeesx
- dgeev
- dgeevx
- dgehd2
- dgehrd
- dgejsv
- dgelq2
- dgelqf
- dgels
- dgelsd
- dgelss
- dgelsy
- dgemqrt
- dgeql2
- dgeqlf
- dgeqp3
- dgeqr2
- dgeqr2p
- dgeqrf
- dgeqrfp
- dgeqrt
- dgeqrt2
- dgeqrt3
- dgerfs
- dgerq2
- dgerqf
- dgesc2
- dgesdd
- dgesv
- dgesvd
- dgesvj
- dgesvx
- dgetc2
- dgetf2
- dgetrf
- dgetri
- dgetrs
- dggbak
- dggbal
- dgges
- dggesx
- dggev
- dggevx
- dggglm
- dgghrd
- dgglse
- dggqrf
- dggrqf
- dgsvj0
- dgsvj1
- dgtcon
- dgtrfs
- dgtsv
- dgtsvx
- dgttrf
- dgttrs
- dgtts2
- dhgeqz
- dhsein
- dhseqr
- disnan
- dlabad
- dlabrd
- dlacn2
- dlacon
- dlacpy
- dladiv
- dlae2
- dlaebz
- dlaed0
- dlaed1
- dlaed2
- dlaed3
- dlaed4
- dlaed5
- dlaed6
- dlaed7
- dlaed8
- dlaed9
- dlaeda
- dlaein
- dlaev2
- dlaexc
- dlag2
- dlag2s
- dlags2
- dlagtf
- dlagtm
- dlagts
- dlagv2
- dlahqr
- dlahr2
- dlaic1
- dlaln2
- dlals0
- dlalsa
- dlalsd
- dlamch
- dlamrg
- dlaneg
- dlangb
- dlange
- dlangt
- dlanhs
- dlansb
- dlansf
- dlansp
- dlanst
- dlansy
- dlantb
- dlantp
- dlantr
- dlanv2
- dlapll
- dlapmr
- dlapmt
- dlapy2
- dlapy3
- dlaqgb
- dlaqge
- dlaqp2
- dlaqps
- dlaqr0
- dlaqr1
- dlaqr2
- dlaqr3
- dlaqr4
- dlaqr5
- dlaqsb
- dlaqsp
- dlaqsy
- dlaqtr
- dlar1v
- dlar2v
- dlarf
- dlarfb
- dlarfg
- dlarfgp
- dlarft
- dlarfx
- dlargv
- dlarnv
- dlarra
- dlarrb
- dlarrc
- dlarrd
- dlarre
- dlarrf
- dlarrj
- dlarrk
- dlarrr
- dlarrv
- dlartg
- dlartgp
- dlartgs
- dlartv
- dlaruv
- dlarz
- dlarzb
- dlarzt
- dlas2
- dlascl
- dlasd0
- dlasd1
- dlasd2
- dlasd3
- dlasd4
- dlasd5
- dlasd6
- dlasd7
- dlasd8
- dlasda
- dlasdq
- dlasdt
- dlaset
- dlasq1
- dlasq2
- dlasq3
- dlasq4
- dlasq6
- dlasr
- dlasrt
- dlassq
- dlasv2
- dlaswp
- dlasy2
- dlasyf
- dlat2s
- dlatbs
- dlatdf
- dlatps
- dlatrd
- dlatrs
- dlatrz
- dlauu2
- dlauum
- dopgtr
- dopmtr
- dorbdb
- dorcsd
- dorg2l
- dorg2r
- dorgbr
- dorghr
- dorgl2
- dorglq
- dorgql
- dorgqr
- dorgr2
- dorgrq
- dorgtr
- dorm2l
- dorm2r
- dormbr
- dormhr
- dorml2
- dormlq
- dormql
- dormqr
- dormr2
- dormr3
- dormrq
- dormrz
- dormtr
- dpbcon
- dpbequ
- dpbrfs
- dpbstf
- dpbsv
- dpbsvx
- dpbtf2
- dpbtrf
- dpbtrs
- dpftrf
- dpftri
- dpftrs
- dpocon
- dpoequ
- dpoequb
- dporfs
- dposv
- dposvx
- dpotf2
- dpotrf
- dpotri
- dpotrs
- dppcon
- dppequ
- dpprfs
- dppsv
- dppsvx
- dpptrf
- dpptri
- dpptrs
- dpstf2
- dpstrf
- dptcon
- dpteqr
- dptrfs
- dptsv
- dptsvx
- dpttrf
- dpttrs
- dptts2
- drscl
- dsbev
- dsbevd
- dsbevx
- dsbgst
- dsbgv
- dsbgvd
- dsbgvx
- dsbtrd
- dsfrk
- dsgesv
- dspcon
- dspev
- dspevd
- dspevx
- dspgst
- dspgv
- dspgvd
- dspgvx
- dsposv
- dsprfs
- dspsv
- dspsvx
- dsptrd
- dsptrf
- dsptri
- dsptrs
- dstebz
- dstedc
- dstegr
- dstein
- dstemr
- dsteqr
- dsterf
- dstev
- dstevd
- dstevr
- dstevx
- dsycon
- dsyconv
- dsyequb
- dsyev
- dsyevd
- dsyevr
- dsyevx
- dsygs2
- dsygst
- dsygv
- dsygvd
- dsygvx
- dsyrfs
- dsysv
- dsysvx
- dsyswapr
- dsytd2
- dsytf2
- dsytrd
- dsytrf
- dsytri
- dsytri2
- dsytri2x
- dsytrs
- dsytrs2
- dtbcon
- dtbrfs
- dtbtrs
- dtfsm
- dtftri
- dtfttp
- dtfttr
- dtgevc
- dtgex2
- dtgexc
- dtgsen
- dtgsja
- dtgsna
- dtgsy2
- dtgsyl
- dtpcon
- dtpmqrt
- dtpqrt
- dtpqrt2
- dtprfb
- dtprfs
- dtptri
- dtptrs
- dtpttf
- dtpttr
- dtrcon
- dtrevc
- dtrexc
- dtrrfs
- dtrsen
- dtrsna
- dtrsyl
- dtrti2
- dtrtri
- dtrtrs
- dtrttf
- dtrttp
- dtzrzf
- dzsum1
- icmax1
- ieeeck
- ilaclc
- ilaclr
- iladiag
- iladlc
- iladlr
- ilaprec
- ilaslc
- ilaslr
- ilatrans
- ilauplo
- ilaver
- ilazlc
- ilazlr
- izmax1
- sbbcsd
- sbdsdc
- sbdsqr
- scsum1
- sdisna
- sgbbrd
- sgbcon
- sgbequ
- sgbequb
- sgbrfs
- sgbsv
- sgbsvx
- sgbtf2
- sgbtrf
- sgbtrs
- sgebak
- sgebal
- sgebd2
- sgebrd
- sgecon
- sgeequ
- sgeequb
- sgees
- sgeesx
- sgeev
- sgeevx
- sgehd2
- sgehrd
- sgejsv
- sgelq2
- sgelqf
- sgels
- sgelsd
- sgelss
- sgelsy
- sgemqrt
- sgeql2
- sgeqlf
- sgeqp3
- sgeqr2
- sgeqr2p
- sgeqrf
- sgeqrfp
- sgeqrt
- sgeqrt2
- sgeqrt3
- sgerfs
- sgerq2
- sgerqf
- sgesc2
- sgesdd
- sgesv
- sgesvd
- sgesvj
- sgesvx
- sgetc2
- sgetf2
- sgetrf
- sgetri
- sgetrs
- sggbak
- sggbal
- sgges
- sggesx
- sggev
- sggevx
- sggglm
- sgghrd
- sgglse
- sggqrf
- sggrqf
- sgsvj0
- sgsvj1
- sgtcon
- sgtrfs
- sgtsv
- sgtsvx
- sgttrf
- sgttrs
- sgtts2
- shgeqz
- shsein
- shseqr
- slabad
- slabrd
- slacn2
- slacon
- slacpy
- sladiv
- slae2
- slaebz
- slaed0
- slaed1
- slaed2
- slaed3
- slaed4
- slaed5
- slaed6
- slaed7
- slaed8
- slaed9
- slaeda
- slaein
- slaev2
- slaexc
- slag2
- slag2d
- slags2
- slagtf
- slagtm
- slagts
- slagv2
- slahqr
- slahr2
- slaic1
- slaln2
- slals0
- slalsa
- slalsd
- slamch
- slamrg
- slangb
- slange
- slangt
- slanhs
- slansb
- slansf
- slansp
- slanst
- slansy
- slantb
- slantp
- slantr
- slanv2
- slapll
- slapmr
- slapmt
- slapy2
- slapy3
- slaqgb
- slaqge
- slaqp2
- slaqps
- slaqr0
- slaqr1
- slaqr2
- slaqr3
- slaqr4
- slaqr5
- slaqsb
- slaqsp
- slaqsy
- slaqtr
- slar1v
- slar2v
- slarf
- slarfb
- slarfg
- slarfgp
- slarft
- slarfx
- slargv
- slarnv
- slarra
- slarrb
- slarrc
- slarrd
- slarre
- slarrf
- slarrj
- slarrk
- slarrr
- slarrv
- slartg
- slartgp
- slartgs
- slartv
- slaruv
- slarz
- slarzb
- slarzt
- slas2
- slascl
- slasd0
- slasd1
- slasd2
- slasd3
- slasd4
- slasd5
- slasd6
- slasd7
- slasd8
- slasda
- slasdq
- slasdt
- slaset
- slasq1
- slasq2
- slasq3
- slasq4
- slasq6
- slasr
- slasrt
- slassq
- slasv2
- slaswp
- slasy2
- slasyf
- slatbs
- slatdf
- slatps
- slatrd
- slatrs
- slatrz
- slauu2
- slauum
- sopgtr
- sopmtr
- sorbdb
- sorcsd
- sorg2l
- sorg2r
- sorgbr
- sorghr
- sorgl2
- sorglq
- sorgql
- sorgqr
- sorgr2
- sorgrq
- sorgtr
- sorm2l
- sorm2r
- sormbr
- sormhr
- sorml2
- sormlq
- sormql
- sormqr
- sormr2
- sormr3
- sormrq
- sormrz
- sormtr
- spbcon
- spbequ
- spbrfs
- spbstf
- spbsv
- spbsvx
- spbtf2
- spbtrf
- spbtrs
- spftrf
- spftri
- spftrs
- spocon
- spoequ
- spoequb
- sporfs
- sposv
- sposvx
- spotf2
- spotrf
- spotri
- spotrs
- sppcon
- sppequ
- spprfs
- sppsv
- sppsvx
- spptrf
- spptri
- spptrs
- spstf2
- spstrf
- sptcon
- spteqr
- sptrfs
- sptsv
- sptsvx
- spttrf
- spttrs
- sptts2
- srscl
- ssbev
- ssbevd
- ssbevx
- ssbgst
- ssbgv
- ssbgvd
- ssbgvx
- ssbtrd
- ssfrk
- sspcon
- sspev
- sspevd
- sspevx
- sspgst
- sspgv
- sspgvd
- sspgvx
- ssprfs
- sspsv
- sspsvx
- ssptrd
- ssptrf
- ssptri
- ssptrs
- sstebz
- sstedc
- sstegr
- sstein
- sstemr
- ssteqr
- ssterf
- sstev
- sstevd
- sstevr
- sstevx
- ssycon
- ssyconv
- ssyequb
- ssyev
- ssyevd
- ssyevr
- ssyevx
- ssygs2
- ssygst
- ssygv
- ssygvd
- ssygvx
- ssyrfs
- ssysv
- ssysvx
- ssyswapr
- ssytd2
- ssytf2
- ssytrd
- ssytrf
- ssytri
- ssytri2
- ssytri2x
- ssytrs
- ssytrs2
- stbcon
- stbrfs
- stbtrs
- stfsm
- stftri
- stfttp
- stfttr
- stgevc
- stgex2
- stgexc
- stgsen
- stgsja
- stgsna
- stgsy2
- stgsyl
- stpcon
- stpmqrt
- stpqrt
- stpqrt2
- stprfb
- stprfs
- stptri
- stptrs
- stpttf
- stpttr
- strcon
- strevc
- strexc
- strrfs
- strsen
- strsna
- strsyl
- strti2
- strtri
- strtrs
- strttf
- strttp
- stzrzf
- xerbla_array
- zbbcsd
- zbdsqr
- zcgesv
- zcposv
- zdrscl
- zgbbrd
- zgbcon
- zgbequ
- zgbequb
- zgbrfs
- zgbsv
- zgbsvx
- zgbtf2
- zgbtrf
- zgbtrs
- zgebak
- zgebal
- zgebd2
- zgebrd
- zgecon
- zgeequ
- zgeequb
- zgees
- zgeesx
- zgeev
- zgeevx
- zgehd2
- zgehrd
- zgelq2
- zgelqf
- zgels
- zgelsd
- zgelss
- zgelsy
- zgemqrt
- zgeql2
- zgeqlf
- zgeqp3
- zgeqr2
- zgeqr2p
- zgeqrf
- zgeqrfp
- zgeqrt
- zgeqrt2
- zgeqrt3
- zgerfs
- zgerq2
- zgerqf
- zgesc2
- zgesdd
- zgesv
- zgesvd
- zgesvx
- zgetc2
- zgetf2
- zgetrf
- zgetri
- zgetrs
- zggbak
- zggbal
- zgges
- zggesx
- zggev
- zggevx
- zggglm
- zgghrd
- zgglse
- zggqrf
- zggrqf
- zgtcon
- zgtrfs
- zgtsv
- zgtsvx
- zgttrf
- zgttrs
- zgtts2
- zhbev
- zhbevd
- zhbevx
- zhbgst
- zhbgv
- zhbgvd
- zhbgvx
- zhbtrd
- zhecon
- zheequb
- zheev
- zheevd
- zheevr
- zheevx
- zhegs2
- zhegst
- zhegv
- zhegvd
- zhegvx
- zherfs
- zhesv
- zhesvx
- zheswapr
- zhetd2
- zhetf2
- zhetrd
- zhetrf
- zhetri
- zhetri2
- zhetri2x
- zhetrs
- zhetrs2
- zhfrk
- zhgeqz
- zhpcon
- zhpev
- zhpevd
- zhpevx
- zhpgst
- zhpgv
- zhpgvd
- zhpgvx
- zhprfs
- zhpsv
- zhpsvx
- zhptrd
- zhptrf
- zhptri
- zhptrs
- zhsein
- zhseqr
- zlabrd
- zlacgv
- zlacn2
- zlacon
- zlacp2
- zlacpy
- zlacrm
- zlacrt
- zladiv
- zlaed0
- zlaed7
- zlaed8
- zlaein
- zlaesy
- zlaev2
- zlag2c
- zlags2
- zlagtm
- zlahef
- zlahqr
- zlahr2
- zlaic1
- zlals0
- zlalsa
- zlalsd
- zlangb
- zlange
- zlangt
- zlanhb
- zlanhe
- zlanhf
- zlanhp
- zlanhs
- zlanht
- zlansb
- zlansp
- zlansy
- zlantb
- zlantp
- zlantr
- zlapll
- zlapmr
- zlapmt
- zlaqgb
- zlaqge
- zlaqhb
- zlaqhe
- zlaqhp
- zlaqp2
- zlaqps
- zlaqr0
- zlaqr1
- zlaqr2
- zlaqr3
- zlaqr4
- zlaqr5
- zlaqsb
- zlaqsp
- zlaqsy
- zlar1v
- zlar2v
- zlarcm
- zlarf
- zlarfb
- zlarfg
- zlarfgp
- zlarft
- zlarfx
- zlargv
- zlarnv
- zlarrv
- zlartg
- zlartv
- zlarz
- zlarzb
- zlarzt
- zlascl
- zlaset
- zlasr
- zlassq
- zlaswp
- zlasyf
- zlat2c
- zlatbs
- zlatdf
- zlatps
- zlatrd
- zlatrs
- zlatrz
- zlauu2
- zlauum
- zpbcon
- zpbequ
- zpbrfs
- zpbstf
- zpbsv
- zpbsvx
- zpbtf2
- zpbtrf
- zpbtrs
- zpftrf
- zpftri
- zpftrs
- zpocon
- zpoequ
- zpoequb
- zporfs
- zposv
- zposvx
- zpotf2
- zpotrf
- zpotri
- zpotrs
- zppcon
- zppequ
- zpprfs
- zppsv
- zppsvx
- zpptrf
- zpptri
- zpptrs
- zpstf2
- zpstrf
- zptcon
- zpteqr
- zptrfs
- zptsv
- zptsvx
- zpttrf
- zpttrs
- zptts2
- zrot
- zspcon
- zspmv
- zspr
- zsprfs
- zspsv
- zspsvx
- zsptrf
- zsptri
- zsptrs
- zstedc
- zstegr
- zstein
- zstemr
- zsteqr
- zsycon
- zsyconv
- zsyequb
- zsymv
- zsyr
- zsyrfs
- zsysv
- zsysvx
- zsyswapr
- zsytf2
- zsytrf
- zsytri
- zsytri2
- zsytri2x
- zsytrs
- zsytrs2
- ztbcon
- ztbrfs
- ztbtrs
- ztfsm
- ztftri
- ztfttp
- ztfttr
- ztgevc
- ztgex2
- ztgexc
- ztgsen
- ztgsja
- ztgsna
- ztgsy2
- ztgsyl
- ztpcon
- ztpmqrt
- ztpqrt
- ztpqrt2
- ztprfb
- ztprfs
- ztptri
- ztptrs
- ztpttf
- ztpttr
- ztrcon
- ztrevc
- ztrexc
- ztrrfs
- ztrsen
- ztrsna
- ztrsyl
- ztrti2
- ztrtri
- ztrtrs
- ztrttf
- ztrttp
- ztzrzf
- zunbdb
- zuncsd
- zung2l
- zung2r
- zungbr
- zunghr
- zungl2
- zunglq
- zungql
- zungqr
- zungr2
- zungrq
- zungtr
- zunm2l
- zunm2r
- zunmbr
- zunmhr
- zunml2
- zunmlq
- zunmql
- zunmqr
- zunmr2
- zunmr3
- zunmrq
- zunmrz
- zunmtr
- zupgtr
- zupmtr
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_dlamch(*args, **kwargs): # real signature unknown
    pass

def _test_slamch(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2600296f60>'

__pyx_capi__ = {
    'cbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f260074fd20>'
    'cbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bba0>'
    'cgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bbd0>'
    'cgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bc00>'
    'cgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bc30>'
    'cgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bc60>'
    'cgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bc90>'
    'cgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029bcc0>'
    'cgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bcf0>'
    'cgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f260029bd20>'
    'cgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f260029bd50>'
    'cgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029bd80>'
    'cgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029bdb0>'
    'cgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bde0>'
    'cgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029be10>'
    'cgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029be40>'
    'cgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029be70>'
    'cgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bea0>'
    'cgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bed0>'
    'cgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect1 *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f260029bf00>'
    'cgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect1 *, char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f260029bf30>'
    'cgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bf60>'
    'cgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029bf90>'
    'cgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029bfc0>'
    'cgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f030>'
    'cgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029f060>'
    'cgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f090>'
    'cgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f0c0>'
    'cgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f260029f0f0>'
    'cgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f120>'
    'cgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f150>'
    'cgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029f180>'
    'cgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029f1b0>'
    'cgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f1e0>'
    'cgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f210>'
    'cgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029f240>'
    'cgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029f270>'
    'cgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f2a0>'
    'cgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f2d0>'
    'cgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029f300>'
    'cgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f330>'
    'cgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f360>'
    'cgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f390>'
    'cgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029f3c0>'
    'cgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f3f0>'
    'cgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f260029f420>'
    'cgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f260029f450>'
    'cgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f480>'
    'cgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f4b0>'
    'cgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f4e0>'
    'cgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x7f260029f510>'
    'cgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f260029f540>'
    'cgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f260029f570>'
    'cgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f5a0>'
    'cgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f5d0>'
    'cggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f600>'
    'cggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f630>'
    'cgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect2 *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f260029f660>'
    'cggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect2 *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f260029f690>'
    'cggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f6c0>'
    'cggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f260029f6f0>'
    'cggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f720>'
    'cgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f750>'
    'cgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f780>'
    'cggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f7b0>'
    'cggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f7e0>'
    'cgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f260029f810>'
    'cgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f840>'
    'cgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f870>'
    'cgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f8a0>'
    'cgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f8d0>'
    'cgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029f900>'
    'cgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029f930>'
    'chbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f960>'
    'chbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f260029f990>'
    'chbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f260029f9c0>'
    'chbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029f9f0>'
    'chbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029fa20>'
    'chbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f260029fa50>'
    'chbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f260029fa80>'
    'chbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029fab0>'
    'checon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f260029fae0>'
    'cheequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f260029fb10>'
    'cheev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029fb40>'
    'cheevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f260029fb70>'
    'cheevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f260029fba0>'
    'cheevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f260029fbd0>'
    'chegs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029fc00>'
    'chegst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029fc30>'
    'chegv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029fc60>'
    'chegvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f260029fc90>'
    'chegvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f260029fcc0>'
    'cherfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029fcf0>'
    'chesv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029fd20>'
    'chesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029fd50>'
    'cheswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f260029fd80>'
    'chetd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f260029fdb0>'
    'chetf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f260029fde0>'
    'chetrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029fe10>'
    'chetrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029fe40>'
    'chetri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029fe70>'
    'chetri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029fea0>'
    'chetri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029fed0>'
    'chetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f260029ff00>'
    'chetrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029ff30>'
    'chfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x7f260029ff60>'
    'chgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f260029ff90>'
    'chla_transtype': None, # (!) real value is '<capsule object "char (int *)" at 0x7f260029ffc0>'
    'chpcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a0030>'
    'chpev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a0060>'
    'chpevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002a0090>'
    'chpevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002a00c0>'
    'chpgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a00f0>'
    'chpgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a0120>'
    'chpgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002a0150>'
    'chpgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002a0180>'
    'chprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a01b0>'
    'chpsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a01e0>'
    'chpsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a0210>'
    'chptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a0240>'
    'chptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a0270>'
    'chptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a02a0>'
    'chptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a02d0>'
    'chsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002a0300>'
    'chseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a0330>'
    'clabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0360>'
    'clacgv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0390>'
    'clacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a03c0>'
    'clacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a03f0>'
    'clacp2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0420>'
    'clacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0450>'
    'clacrm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0480>'
    'clacrt': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a04b0>'
    'cladiv': None, # (!) real value is '<capsule object "__pyx_t_float_complex (__pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a04e0>'
    'claed0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a0510>'
    'claed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a0540>'
    'claed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a0570>'
    'claein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a05a0>'
    'claesy': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a05d0>'
    'claev2': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x7f26002a0600>'
    'clag2z': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002a0630>'
    'clags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x7f26002a0660>'
    'clagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a0690>'
    'clahef': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a06c0>'
    'clahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a06f0>'
    'clahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0720>'
    'claic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a0750>'
    'clals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a0780>'
    'clalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a07b0>'
    'clalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a07e0>'
    'clangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0810>'
    'clange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0840>'
    'clangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a0870>'
    'clanhb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a08a0>'
    'clanhe': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a08d0>'
    'clanhf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0900>'
    'clanhp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0930>'
    'clanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0960>'
    'clanht': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x7f26002a0990>'
    'clansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a09c0>'
    'clansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a09f0>'
    'clansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0a20>'
    'clantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0a50>'
    'clantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0a80>'
    'clantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0ab0>'
    'clapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0ae0>'
    'clapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a0b10>'
    'clapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a0b40>'
    'claqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0b70>'
    'claqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0ba0>'
    'claqhb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0bd0>'
    'claqhe': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0c00>'
    'claqhp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0c30>'
    'claqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x7f26002a0c60>'
    'claqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a0c90>'
    'claqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a0cc0>'
    'claqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a0cf0>'
    'claqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0d20>'
    'claqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0d50>'
    'claqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a0d80>'
    'claqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0db0>'
    'claqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0de0>'
    'claqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0e10>'
    'claqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002a0e40>'
    'clar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0e70>'
    'clar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a0ea0>'
    'clarcm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a0ed0>'
    'clarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f26002a0f00>'
    'clarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a0f30>'
    'clarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f26002a0f60>'
    'clarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f26002a0f90>'
    'clarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a0fc0>'
    'clarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f26002a2030>'
    'clargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2060>'
    'clarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *)" at 0x7f26002a2090>'
    'clarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a20c0>'
    'clartg': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a20f0>'
    'clartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a2120>'
    'clarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f26002a2150>'
    'clarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a2180>'
    'clarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a21b0>'
    'clascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a21e0>'
    'claset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a2210>'
    'clasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a2240>'
    'classq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002a2270>'
    'claswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, int *, int *, int *)" at 0x7f26002a22a0>'
    'clasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a22d0>'
    'clatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2300>'
    'clatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a2330>'
    'clatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2360>'
    'clatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a2390>'
    'clatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a23c0>'
    'clatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x7f26002a23f0>'
    'clauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2420>'
    'clauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2450>'
    'cpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2480>'
    'cpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a24b0>'
    'cpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a24e0>'
    'cpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2510>'
    'cpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2540>'
    'cpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2570>'
    'cpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a25a0>'
    'cpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a25d0>'
    'cpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2600>'
    'cpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a2630>'
    'cpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a2660>'
    'cpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2690>'
    'cpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a26c0>'
    'cpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a26f0>'
    'cpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2720>'
    'cporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2750>'
    'cposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2780>'
    'cposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a27b0>'
    'cpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a27e0>'
    'cpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2810>'
    'cpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2840>'
    'cpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2870>'
    'cppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a28a0>'
    'cppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a28d0>'
    'cpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2900>'
    'cppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2930>'
    'cppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2960>'
    'cpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a2990>'
    'cpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a29c0>'
    'cpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a29f0>'
    'cpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2a20>'
    'cpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2a50>'
    'cptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2a80>'
    'cpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2ab0>'
    'cptrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2ae0>'
    'cptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2b10>'
    'cptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2b40>'
    'cpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a2b70>'
    'cpttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2ba0>'
    'cptts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a2bd0>'
    'crot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0x7f26002a2c00>'
    'cspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a2c30>'
    'cspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a2c60>'
    'cspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f26002a2c90>'
    'csprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2cc0>'
    'cspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2cf0>'
    'cspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2d20>'
    'csptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2d50>'
    'csptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a2d80>'
    'csptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a2db0>'
    'csrscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a2de0>'
    'cstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002a2e10>'
    'cstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002a2e40>'
    'cstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002a2e70>'
    'cstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002a2ea0>'
    'csteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a2ed0>'
    'csycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a2f00>'
    'csyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a2f30>'
    'csyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0x7f26002a2f60>'
    'csymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a2f90>'
    'csyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a2fc0>'
    'csyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4030>'
    'csysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4060>'
    'csysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4090>'
    'csyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f26002a40c0>'
    'csytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f26002a40f0>'
    'csytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4120>'
    'csytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4150>'
    'csytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4180>'
    'csytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a41b0>'
    'csytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a41e0>'
    'csytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4210>'
    'ctbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4240>'
    'ctbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4270>'
    'ctbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a42a0>'
    'ctfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a42d0>'
    'ctftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4300>'
    'ctfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a4330>'
    'ctfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4360>'
    'ctgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4390>'
    'ctgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f26002a43c0>'
    'ctgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x7f26002a43f0>'
    'ctgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x7f26002a4420>'
    'ctgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4450>'
    'ctgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f26002a4480>'
    'ctgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a44b0>'
    'ctgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *)" at 0x7f26002a44e0>'
    'ctpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4510>'
    'ctpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4540>'
    'ctpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4570>'
    'ctpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a45a0>'
    'ctprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a45d0>'
    'ctprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4600>'
    'ctptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4630>'
    'ctptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4660>'
    'ctpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a4690>'
    'ctpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a46c0>'
    'ctrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a46f0>'
    'ctrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4720>'
    'ctrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0x7f26002a4750>'
    'ctrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4780>'
    'ctrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a47b0>'
    'ctrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a47e0>'
    'ctrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002a4810>'
    'ctrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4840>'
    'ctrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4870>'
    'ctrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a48a0>'
    'ctrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a48d0>'
    'ctrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4900>'
    'ctzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4930>'
    'cunbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4960>'
    'cuncsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002a4990>'
    'cung2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a49c0>'
    'cung2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a49f0>'
    'cungbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4a20>'
    'cunghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4a50>'
    'cungl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a4a80>'
    'cunglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4ab0>'
    'cungql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4ae0>'
    'cungqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4b10>'
    'cungr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f26002a4b40>'
    'cungrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4b70>'
    'cungtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4ba0>'
    'cunm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4bd0>'
    'cunm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4c00>'
    'cunmbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4c30>'
    'cunmhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4c60>'
    'cunml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4c90>'
    'cunmlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4cc0>'
    'cunmql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4cf0>'
    'cunmqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4d20>'
    'cunmr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4d50>'
    'cunmr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4d80>'
    'cunmrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4db0>'
    'cunmrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4de0>'
    'cunmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002a4e10>'
    'cupgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4e40>'
    'cupmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002a4e70>'
    'dbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a4ea0>'
    'dbdsdc': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a4ed0>'
    'dbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a4f00>'
    'ddisna': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a4f30>'
    'dgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a4f60>'
    'dgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a4f90>'
    'dgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a4fc0>'
    'dgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6030>'
    'dgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6060>'
    'dgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6090>'
    'dgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a60c0>'
    'dgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a60f0>'
    'dgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a6120>'
    'dgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6150>'
    'dgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6180>'
    'dgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a61b0>'
    'dgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a61e0>'
    'dgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6210>'
    'dgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6240>'
    'dgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6270>'
    'dgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a62a0>'
    'dgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect2 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a62d0>'
    'dgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect2 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x7f26002a6300>'
    'dgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6330>'
    'dgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a6360>'
    'dgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6390>'
    'dgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a63c0>'
    'dgejsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a63f0>'
    'dgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6420>'
    'dgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6450>'
    'dgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6480>'
    'dgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a64b0>'
    'dgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a64e0>'
    'dgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6510>'
    'dgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6540>'
    'dgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6570>'
    'dgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a65a0>'
    'dgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a65d0>'
    'dgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6600>'
    'dgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6630>'
    'dgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6660>'
    'dgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6690>'
    'dgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a66c0>'
    'dgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a66f0>'
    'dgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6720>'
    'dgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6750>'
    'dgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6780>'
    'dgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a67b0>'
    'dgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a67e0>'
    'dgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a6810>'
    'dgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6840>'
    'dgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6870>'
    'dgesvj': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a68a0>'
    'dgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a68d0>'
    'dgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002a6900>'
    'dgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a6930>'
    'dgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a6960>'
    'dgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6990>'
    'dgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a69c0>'
    'dggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a69f0>'
    'dggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6a20>'
    'dgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect3 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a6a50>'
    'dggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect3 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x7f26002a6a80>'
    'dggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6ab0>'
    'dggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002a6ae0>'
    'dggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6b10>'
    'dgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6b40>'
    'dgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6b70>'
    'dggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6ba0>'
    'dggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6bd0>'
    'dgsvj0': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6c00>'
    'dgsvj1': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6c30>'
    'dgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6c60>'
    'dgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6c90>'
    'dgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6cc0>'
    'dgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6cf0>'
    'dgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6d20>'
    'dgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6d50>'
    'dgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6d80>'
    'dhgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6db0>'
    'dhsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a6de0>'
    'dhseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6e10>'
    'disnan': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a6e40>'
    'dlabad': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a6e70>'
    'dlabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6ea0>'
    'dlacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6ed0>'
    'dlacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6f00>'
    'dlacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a6f30>'
    'dladiv': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a6f60>'
    'dlae2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a6f90>'
    'dlaebz': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a6fc0>'
    'dlaed0': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8030>'
    'dlaed1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8060>'
    'dlaed2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x7f26002a8090>'
    'dlaed3': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a80c0>'
    'dlaed4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a80f0>'
    'dlaed5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8120>'
    'dlaed6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8150>'
    'dlaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8180>'
    'dlaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a81b0>'
    'dlaed9': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a81e0>'
    'dlaeda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8210>'
    'dlaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8240>'
    'dlaev2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8270>'
    'dlaexc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a82a0>'
    'dlag2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a82d0>'
    'dlag2s': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002a8300>'
    'dlags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8330>'
    'dlagtf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8360>'
    'dlagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8390>'
    'dlagts': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a83c0>'
    'dlagv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a83f0>'
    'dlahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8420>'
    'dlahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8450>'
    'dlaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8480>'
    'dlaln2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a84b0>'
    'dlals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a84e0>'
    'dlalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8510>'
    'dlalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8540>'
    'dlamch': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *)" at 0x7f26002a8570>'
    'dlamrg': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a85a0>'
    'dlaneg': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a85d0>'
    'dlangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8600>'
    'dlange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8630>'
    'dlangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8660>'
    'dlanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8690>'
    'dlansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a86c0>'
    'dlansf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a86f0>'
    'dlansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8720>'
    'dlanst': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8750>'
    'dlansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8780>'
    'dlantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a87b0>'
    'dlantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a87e0>'
    'dlantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8810>'
    'dlanv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8840>'
    'dlapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8870>'
    'dlapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a88a0>'
    'dlapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a88d0>'
    'dlapy2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8900>'
    'dlapy3': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8930>'
    'dlaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002a8960>'
    'dlaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002a8990>'
    'dlaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a89c0>'
    'dlaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a89f0>'
    'dlaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8a20>'
    'dlaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8a50>'
    'dlaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8a80>'
    'dlaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8ab0>'
    'dlaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8ae0>'
    'dlaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8b10>'
    'dlaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002a8b40>'
    'dlaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002a8b70>'
    'dlaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002a8ba0>'
    'dlaqtr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8bd0>'
    'dlar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8c00>'
    'dlar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8c30>'
    'dlarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8c60>'
    'dlarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8c90>'
    'dlarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8cc0>'
    'dlarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8cf0>'
    'dlarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8d20>'
    'dlarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8d50>'
    'dlargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8d80>'
    'dlarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8db0>'
    'dlarra': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002a8de0>'
    'dlarrb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8e10>'
    'dlarrc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002a8e40>'
    'dlarrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8e70>'
    'dlarre': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8ea0>'
    'dlarrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8ed0>'
    'dlarrj': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8f00>'
    'dlarrk': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8f30>'
    'dlarrr': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002a8f60>'
    'dlarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002a8f90>'
    'dlartg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002a8fc0>'
    'dlartgp': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab030>'
    'dlartgs': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab060>'
    'dlartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab090>'
    'dlaruv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab0c0>'
    'dlarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab0f0>'
    'dlarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab120>'
    'dlarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab150>'
    'dlas2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab180>'
    'dlascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab1b0>'
    'dlasd0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab1e0>'
    'dlasd1': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab210>'
    'dlasd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, int *)" at 0x7f26002ab240>'
    'dlasd3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab270>'
    'dlasd4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab2a0>'
    'dlasd5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab2d0>'
    'dlasd6': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab300>'
    'dlasd7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab330>'
    'dlasd8': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab360>'
    'dlasda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab390>'
    'dlasdq': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab3c0>'
    'dlasdt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *)" at 0x7f26002ab3f0>'
    'dlaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab420>'
    'dlasq1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab450>'
    'dlasq2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab480>'
    'dlasq3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab4b0>'
    'dlasq4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab4e0>'
    'dlasq6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab510>'
    'dlasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab540>'
    'dlasrt': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab570>'
    'dlassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab5a0>'
    'dlasv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab5d0>'
    'dlaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0x7f26002ab600>'
    'dlasy2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab630>'
    'dlasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab660>'
    'dlat2s': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002ab690>'
    'dlatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab6c0>'
    'dlatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab6f0>'
    'dlatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab720>'
    'dlatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab750>'
    'dlatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab780>'
    'dlatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002ab7b0>'
    'dlauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab7e0>'
    'dlauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab810>'
    'dopgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab840>'
    'dopmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab870>'
    'dorbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab8a0>'
    'dorcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002ab8d0>'
    'dorg2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab900>'
    'dorg2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab930>'
    'dorgbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab960>'
    'dorghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab990>'
    'dorgl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ab9c0>'
    'dorglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ab9f0>'
    'dorgql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aba20>'
    'dorgqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aba50>'
    'dorgr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aba80>'
    'dorgrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abab0>'
    'dorgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abae0>'
    'dorm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abb10>'
    'dorm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abb40>'
    'dormbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abb70>'
    'dormhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abba0>'
    'dorml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abbd0>'
    'dormlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abc00>'
    'dormql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abc30>'
    'dormqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abc60>'
    'dormr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abc90>'
    'dormr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abcc0>'
    'dormrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abcf0>'
    'dormrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abd20>'
    'dormtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abd50>'
    'dpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abd80>'
    'dpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abdb0>'
    'dpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abde0>'
    'dpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abe10>'
    'dpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abe40>'
    'dpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abe70>'
    'dpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abea0>'
    'dpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abed0>'
    'dpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abf00>'
    'dpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abf30>'
    'dpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002abf60>'
    'dpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abf90>'
    'dpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002abfc0>'
    'dpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa030>'
    'dpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa060>'
    'dporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa090>'
    'dposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa0c0>'
    'dposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa0f0>'
    'dpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa120>'
    'dpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa150>'
    'dpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa180>'
    'dpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa1b0>'
    'dppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa1e0>'
    'dppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa210>'
    'dpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa240>'
    'dppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa270>'
    'dppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa2a0>'
    'dpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa2d0>'
    'dpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa300>'
    'dpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa330>'
    'dpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa360>'
    'dpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa390>'
    'dptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa3c0>'
    'dpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa3f0>'
    'dptrfs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa420>'
    'dptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa450>'
    'dptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa480>'
    'dpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa4b0>'
    'dpttrs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa4e0>'
    'dptts2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa510>'
    'drscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa540>'
    'dsbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa570>'
    'dsbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aa5a0>'
    'dsbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aa5d0>'
    'dsbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa600>'
    'dsbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa630>'
    'dsbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aa660>'
    'dsbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aa690>'
    'dsbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa6c0>'
    'dsfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002aa6f0>'
    'dsgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aa720>'
    'dspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa750>'
    'dspev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa780>'
    'dspevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aa7b0>'
    'dspevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aa7e0>'
    'dspgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa810>'
    'dspgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa840>'
    'dspgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aa870>'
    'dspgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aa8a0>'
    'dsposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aa8d0>'
    'dsprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa900>'
    'dspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa930>'
    'dspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa960>'
    'dsptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa990>'
    'dsptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aa9c0>'
    'dsptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aa9f0>'
    'dsptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aaa20>'
    'dstebz': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aaa50>'
    'dstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aaa80>'
    'dstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aaab0>'
    'dstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aaae0>'
    'dstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aab10>'
    'dsteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aab40>'
    'dsterf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aab70>'
    'dstev': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aaba0>'
    'dstevd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aabd0>'
    'dstevr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aac00>'
    'dstevx': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aac30>'
    'dsycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aac60>'
    'dsyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aac90>'
    'dsyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aacc0>'
    'dsyev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aacf0>'
    'dsyevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aad20>'
    'dsyevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aad50>'
    'dsyevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aad80>'
    'dsygs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aadb0>'
    'dsygst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aade0>'
    'dsygv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aae10>'
    'dsygvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aae40>'
    'dsygvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002aae70>'
    'dsyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aaea0>'
    'dsysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aaed0>'
    'dsysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aaf00>'
    'dsyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aaf30>'
    'dsytd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002aaf60>'
    'dsytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002aaf90>'
    'dsytrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002aafc0>'
    'dsytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae030>'
    'dsytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae060>'
    'dsytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae090>'
    'dsytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae0c0>'
    'dsytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae0f0>'
    'dsytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae120>'
    'dtbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae150>'
    'dtbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae180>'
    'dtbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae1b0>'
    'dtfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae1e0>'
    'dtftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae210>'
    'dtfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae240>'
    'dtfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae270>'
    'dtgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae2a0>'
    'dtgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae2d0>'
    'dtgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae300>'
    'dtgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002ae330>'
    'dtgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae360>'
    'dtgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002ae390>'
    'dtgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002ae3c0>'
    'dtgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002ae3f0>'
    'dtpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae420>'
    'dtpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae450>'
    'dtpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae480>'
    'dtpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae4b0>'
    'dtprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae4e0>'
    'dtprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae510>'
    'dtptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae540>'
    'dtptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae570>'
    'dtpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae5a0>'
    'dtpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae5d0>'
    'dtrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae600>'
    'dtrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae630>'
    'dtrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae660>'
    'dtrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae690>'
    'dtrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002ae6c0>'
    'dtrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002ae6f0>'
    'dtrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae720>'
    'dtrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae750>'
    'dtrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae780>'
    'dtrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae7b0>'
    'dtrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae7e0>'
    'dtrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae810>'
    'dtzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002ae840>'
    'dzsum1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (int *, __pyx_t_double_complex *, int *)" at 0x7f26002ae870>'
    'icmax1': None, # (!) real value is '<capsule object "int (int *, __pyx_t_float_complex *, int *)" at 0x7f26002ae8a0>'
    'ieeeck': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002ae8d0>'
    'ilaclc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002ae900>'
    'ilaclr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_float_complex *, int *)" at 0x7f26002ae930>'
    'iladiag': None, # (!) real value is '<capsule object "int (char *)" at 0x7f26002ae960>'
    'iladlc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae990>'
    'iladlr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002ae9c0>'
    'ilaprec': None, # (!) real value is '<capsule object "int (char *)" at 0x7f26002ae9f0>'
    'ilaslc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aea20>'
    'ilaslr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aea50>'
    'ilatrans': None, # (!) real value is '<capsule object "int (char *)" at 0x7f26002aea80>'
    'ilauplo': None, # (!) real value is '<capsule object "int (char *)" at 0x7f26002aeab0>'
    'ilaver': None, # (!) real value is '<capsule object "void (int *, int *, int *)" at 0x7f26002aeae0>'
    'ilazlc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002aeb10>'
    'ilazlr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002aeb40>'
    'izmax1': None, # (!) real value is '<capsule object "int (int *, __pyx_t_double_complex *, int *)" at 0x7f26002aeb70>'
    'sbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aeba0>'
    'sbdsdc': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aebd0>'
    'sbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aec00>'
    'scsum1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (int *, __pyx_t_float_complex *, int *)" at 0x7f26002aec30>'
    'sdisna': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aec60>'
    'sgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aec90>'
    'sgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aecc0>'
    'sgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aecf0>'
    'sgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aed20>'
    'sgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aed50>'
    'sgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aed80>'
    'sgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aedb0>'
    'sgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002aede0>'
    'sgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002aee10>'
    'sgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aee40>'
    'sgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aee70>'
    'sgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aeea0>'
    'sgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aeed0>'
    'sgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aef00>'
    'sgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002aef30>'
    'sgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aef60>'
    'sgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aef90>'
    'sgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect2 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002aefc0>'
    'sgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect2 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x7f26002af030>'
    'sgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af060>'
    'sgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002af090>'
    'sgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af0c0>'
    'sgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af0f0>'
    'sgejsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002af120>'
    'sgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af150>'
    'sgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af180>'
    'sgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af1b0>'
    'sgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002af1e0>'
    'sgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af210>'
    'sgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af240>'
    'sgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af270>'
    'sgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af2a0>'
    'sgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af2d0>'
    'sgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af300>'
    'sgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af330>'
    'sgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af360>'
    'sgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af390>'
    'sgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af3c0>'
    'sgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af3f0>'
    'sgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af420>'
    'sgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af450>'
    'sgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af480>'
    'sgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af4b0>'
    'sgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af4e0>'
    'sgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002af510>'
    'sgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002af540>'
    'sgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af570>'
    'sgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af5a0>'
    'sgesvj': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af5d0>'
    'sgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af600>'
    'sgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002af630>'
    'sgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002af660>'
    'sgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002af690>'
    'sgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af6c0>'
    'sgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af6f0>'
    'sggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af720>'
    'sggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002af750>'
    'sgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect3 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002af780>'
    'sggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect3 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x7f26002af7b0>'
    'sggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af7e0>'
    'sggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002af810>'
    'sggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af840>'
    'sgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af870>'
    'sgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af8a0>'
    'sggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af8d0>'
    'sggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af900>'
    'sgsvj0': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af930>'
    'sgsvj1': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af960>'
    'sgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af990>'
    'sgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af9c0>'
    'sgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002af9f0>'
    'sgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afa20>'
    'sgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afa50>'
    'sgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afa80>'
    'sgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afab0>'
    'shgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afae0>'
    'shsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002afb10>'
    'shseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afb40>'
    'slabad': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002afb70>'
    'slabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afba0>'
    'slacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afbd0>'
    'slacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afc00>'
    'slacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afc30>'
    'sladiv': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002afc60>'
    'slae2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002afc90>'
    'slaebz': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afcc0>'
    'slaed0': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afcf0>'
    'slaed1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afd20>'
    'slaed2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x7f26002afd50>'
    'slaed3': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afd80>'
    'slaed4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afdb0>'
    'slaed5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002afde0>'
    'slaed6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afe10>'
    'slaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afe40>'
    'slaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002afe70>'
    'slaed9': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002afea0>'
    'slaeda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002afed0>'
    'slaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aff00>'
    'slaev2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002aff30>'
    'slaexc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002aff60>'
    'slag2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002aff90>'
    'slag2d': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002affc0>'
    'slags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1030>'
    'slagtf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1060>'
    'slagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1090>'
    'slagts': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b10c0>'
    'slagv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b10f0>'
    'slahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1120>'
    'slahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1150>'
    'slaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1180>'
    'slaln2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b11b0>'
    'slals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b11e0>'
    'slalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1210>'
    'slalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1240>'
    'slamch': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *)" at 0x7f26002b1270>'
    'slamrg': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b12a0>'
    'slangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b12d0>'
    'slange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1300>'
    'slangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1330>'
    'slanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1360>'
    'slansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1390>'
    'slansf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b13c0>'
    'slansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b13f0>'
    'slanst': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1420>'
    'slansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1450>'
    'slantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1480>'
    'slantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b14b0>'
    'slantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b14e0>'
    'slanv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1510>'
    'slapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1540>'
    'slapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1570>'
    'slapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b15a0>'
    'slapy2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b15d0>'
    'slapy3': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1600>'
    'slaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002b1630>'
    'slaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002b1660>'
    'slaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1690>'
    'slaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b16c0>'
    'slaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b16f0>'
    'slaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1720>'
    'slaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1750>'
    'slaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1780>'
    'slaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b17b0>'
    'slaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b17e0>'
    'slaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002b1810>'
    'slaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002b1840>'
    'slaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0x7f26002b1870>'
    'slaqtr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b18a0>'
    'slar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b18d0>'
    'slar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1900>'
    'slarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1930>'
    'slarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1960>'
    'slarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1990>'
    'slarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b19c0>'
    'slarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b19f0>'
    'slarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1a20>'
    'slargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1a50>'
    'slarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1a80>'
    'slarra': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b1ab0>'
    'slarrb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1ae0>'
    'slarrc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b1b10>'
    'slarrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1b40>'
    'slarre': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1b70>'
    'slarrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1ba0>'
    'slarrj': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1bd0>'
    'slarrk': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1c00>'
    'slarrr': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1c30>'
    'slarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1c60>'
    'slartg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1c90>'
    'slartgp': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1cc0>'
    'slartgs': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1cf0>'
    'slartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1d20>'
    'slaruv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1d50>'
    'slarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1d80>'
    'slarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1db0>'
    'slarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1de0>'
    'slas2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1e10>'
    'slascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1e40>'
    'slasd0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1e70>'
    'slasd1': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1ea0>'
    'slasd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, int *)" at 0x7f26002b1ed0>'
    'slasd3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1f00>'
    'slasd4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1f30>'
    'slasd5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b1f60>'
    'slasd6': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b1f90>'
    'slasd7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b1fc0>'
    'slasd8': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3030>'
    'slasda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3060>'
    'slasdq': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3090>'
    'slasdt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *)" at 0x7f26002b30c0>'
    'slaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b30f0>'
    'slasq1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3120>'
    'slasq2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3150>'
    'slasq3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b3180>'
    'slasq4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b31b0>'
    'slasq6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b31e0>'
    'slasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3210>'
    'slasrt': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3240>'
    'slassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b3270>'
    'slasv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b32a0>'
    'slaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0x7f26002b32d0>'
    'slasy2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3300>'
    'slasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3330>'
    'slatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3360>'
    'slatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3390>'
    'slatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b33c0>'
    'slatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b33f0>'
    'slatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3420>'
    'slatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b3450>'
    'slauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3480>'
    'slauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b34b0>'
    'sopgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b34e0>'
    'sopmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3510>'
    'sorbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3540>'
    'sorcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b3570>'
    'sorg2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b35a0>'
    'sorg2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b35d0>'
    'sorgbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3600>'
    'sorghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3630>'
    'sorgl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3660>'
    'sorglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3690>'
    'sorgql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b36c0>'
    'sorgqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b36f0>'
    'sorgr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3720>'
    'sorgrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3750>'
    'sorgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3780>'
    'sorm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b37b0>'
    'sorm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b37e0>'
    'sormbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3810>'
    'sormhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3840>'
    'sorml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3870>'
    'sormlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b38a0>'
    'sormql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b38d0>'
    'sormqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3900>'
    'sormr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3930>'
    'sormr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3960>'
    'sormrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3990>'
    'sormrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b39c0>'
    'sormtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b39f0>'
    'spbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3a20>'
    'spbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3a50>'
    'spbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3a80>'
    'spbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3ab0>'
    'spbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3ae0>'
    'spbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3b10>'
    'spbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3b40>'
    'spbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3b70>'
    'spbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3ba0>'
    'spftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3bd0>'
    'spftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3c00>'
    'spftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3c30>'
    'spocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3c60>'
    'spoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3c90>'
    'spoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3cc0>'
    'sporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3cf0>'
    'sposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3d20>'
    'sposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3d50>'
    'spotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3d80>'
    'spotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3db0>'
    'spotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3de0>'
    'spotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3e10>'
    'sppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3e40>'
    'sppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3e70>'
    'spprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3ea0>'
    'sppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3ed0>'
    'sppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3f00>'
    'spptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3f30>'
    'spptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3f60>'
    'spptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b3f90>'
    'spstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b3fc0>'
    'spstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5030>'
    'sptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5060>'
    'spteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5090>'
    'sptrfs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b50c0>'
    'sptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b50f0>'
    'sptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5120>'
    'spttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5150>'
    'spttrs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5180>'
    'sptts2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b51b0>'
    'srscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b51e0>'
    'ssbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5210>'
    'ssbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5240>'
    'ssbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5270>'
    'ssbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b52a0>'
    'ssbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b52d0>'
    'ssbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5300>'
    'ssbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5330>'
    'ssbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5360>'
    'ssfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0x7f26002b5390>'
    'sspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b53c0>'
    'sspev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b53f0>'
    'sspevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5420>'
    'sspevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5450>'
    'sspgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5480>'
    'sspgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b54b0>'
    'sspgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b54e0>'
    'sspgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5510>'
    'ssprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5540>'
    'sspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5570>'
    'sspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b55a0>'
    'ssptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b55d0>'
    'ssptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5600>'
    'ssptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5630>'
    'ssptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5660>'
    'sstebz': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5690>'
    'sstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b56c0>'
    'sstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b56f0>'
    'sstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5720>'
    'sstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5750>'
    'ssteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5780>'
    'ssterf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b57b0>'
    'sstev': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b57e0>'
    'sstevd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5810>'
    'sstevr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5840>'
    'sstevx': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5870>'
    'ssycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b58a0>'
    'ssyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b58d0>'
    'ssyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5900>'
    'ssyev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5930>'
    'ssyevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5960>'
    'ssyevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5990>'
    'ssyevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b59c0>'
    'ssygs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b59f0>'
    'ssygst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5a20>'
    'ssygv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5a50>'
    'ssygvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5a80>'
    'ssygvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5ab0>'
    'ssyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5ae0>'
    'ssysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5b10>'
    'ssysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5b40>'
    'ssyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5b70>'
    'ssytd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5ba0>'
    'ssytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5bd0>'
    'ssytrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5c00>'
    'ssytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5c30>'
    'ssytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5c60>'
    'ssytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5c90>'
    'ssytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5cc0>'
    'ssytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5cf0>'
    'ssytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5d20>'
    'stbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5d50>'
    'stbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5d80>'
    'stbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5db0>'
    'stfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5de0>'
    'stftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5e10>'
    'stfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5e40>'
    'stfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5e70>'
    'stgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b5ea0>'
    'stgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5ed0>'
    'stgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5f00>'
    'stgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b5f30>'
    'stgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b5f60>'
    'stgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5f90>'
    'stgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b5fc0>'
    'stgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b7030>'
    'stpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b7060>'
    'stpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b7090>'
    'stpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b70c0>'
    'stpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b70f0>'
    'stprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b7120>'
    'stprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b7150>'
    'stptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b7180>'
    'stptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b71b0>'
    'stpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b71e0>'
    'stpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b7210>'
    'strcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b7240>'
    'strevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b7270>'
    'strexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b72a0>'
    'strrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b72d0>'
    'strsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0x7f26002b7300>'
    'strsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0x7f26002b7330>'
    'strsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b7360>'
    'strti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b7390>'
    'strtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b73c0>'
    'strtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b73f0>'
    'strttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b7420>'
    'strttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0x7f26002b7450>'
    'stzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0x7f26002b7480>'
    'xerbla_array': None, # (!) real value is '<capsule object "void (char *, int *, int *)" at 0x7f26002b74b0>'
    'zbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b74e0>'
    'zbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7510>'
    'zcgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b7540>'
    'zcposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b7570>'
    'zdrscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002b75a0>'
    'zgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b75d0>'
    'zgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7600>'
    'zgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7630>'
    'zgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7660>'
    'zgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7690>'
    'zgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b76c0>'
    'zgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b76f0>'
    'zgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002b7720>'
    'zgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002b7750>'
    'zgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7780>'
    'zgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b77b0>'
    'zgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b77e0>'
    'zgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b7810>'
    'zgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7840>'
    'zgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7870>'
    'zgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b78a0>'
    'zgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b78d0>'
    'zgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect1 *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b7900>'
    'zgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect1 *, char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b7930>'
    'zgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7960>'
    'zgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7990>'
    'zgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b79c0>'
    'zgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b79f0>'
    'zgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b7a20>'
    'zgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7a50>'
    'zgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7a80>'
    'zgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b7ab0>'
    'zgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7ae0>'
    'zgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7b10>'
    'zgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b7b40>'
    'zgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b7b70>'
    'zgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7ba0>'
    'zgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7bd0>'
    'zgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b7c00>'
    'zgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b7c30>'
    'zgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7c60>'
    'zgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7c90>'
    'zgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b7cc0>'
    'zgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7cf0>'
    'zgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7d20>'
    'zgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7d50>'
    'zgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b7d80>'
    'zgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7db0>'
    'zgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002b7de0>'
    'zgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b7e10>'
    'zgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7e40>'
    'zgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7e70>'
    'zgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b7ea0>'
    'zgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x7f26002b7ed0>'
    'zgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002b7f00>'
    'zgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002b7f30>'
    'zgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7f60>'
    'zgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7f90>'
    'zggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b7fc0>'
    'zggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9030>'
    'zgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect2 *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b9060>'
    'zggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect2 *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b9090>'
    'zggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b90c0>'
    'zggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b90f0>'
    'zggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9120>'
    'zgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9150>'
    'zgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9180>'
    'zggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b91b0>'
    'zggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b91e0>'
    'zgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002b9210>'
    'zgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9240>'
    'zgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9270>'
    'zgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b92a0>'
    'zgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b92d0>'
    'zgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9300>'
    'zgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9330>'
    'zhbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9360>'
    'zhbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b9390>'
    'zhbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b93c0>'
    'zhbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b93f0>'
    'zhbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9420>'
    'zhbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b9450>'
    'zhbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b9480>'
    'zhbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b94b0>'
    'zhecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002b94e0>'
    'zheequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002b9510>'
    'zheev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9540>'
    'zheevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b9570>'
    'zheevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b95a0>'
    'zheevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b95d0>'
    'zhegs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9600>'
    'zhegst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9630>'
    'zhegv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9660>'
    'zhegvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b9690>'
    'zhegvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b96c0>'
    'zherfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b96f0>'
    'zhesv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9720>'
    'zhesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9750>'
    'zheswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002b9780>'
    'zhetd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002b97b0>'
    'zhetf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002b97e0>'
    'zhetrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9810>'
    'zhetrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9840>'
    'zhetri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9870>'
    'zhetri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b98a0>'
    'zhetri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b98d0>'
    'zhetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9900>'
    'zhetrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9930>'
    'zhfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x7f26002b9960>'
    'zhgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9990>'
    'zhpcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002b99c0>'
    'zhpev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b99f0>'
    'zhpevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b9a20>'
    'zhpevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b9a50>'
    'zhpgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002b9a80>'
    'zhpgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9ab0>'
    'zhpgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002b9ae0>'
    'zhpgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b9b10>'
    'zhprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9b40>'
    'zhpsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9b70>'
    'zhpsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9ba0>'
    'zhptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002b9bd0>'
    'zhptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9c00>'
    'zhptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9c30>'
    'zhptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9c60>'
    'zhsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002b9c90>'
    'zhseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002b9cc0>'
    'zlabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9cf0>'
    'zlacgv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9d20>'
    'zlacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b9d50>'
    'zlacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9d80>'
    'zlacp2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9db0>'
    'zlacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002b9de0>'
    'zlacrm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002b9e10>'
    'zlacrt': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002b9e40>'
    'zladiv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002b9e70>'
    'zlaed0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b9ea0>'
    'zlaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002b9ed0>'
    'zlaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9f00>'
    'zlaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002b9f30>'
    'zlaesy': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002b9f60>'
    'zlaev2': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x7f26002b9f90>'
    'zlag2c': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002b9fc0>'
    'zlags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x7f26002bb030>'
    'zlagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002bb060>'
    'zlahef': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bb090>'
    'zlahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bb0c0>'
    'zlahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bb0f0>'
    'zlaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002bb120>'
    'zlals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bb150>'
    'zlalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002bb180>'
    'zlalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002bb1b0>'
    'zlangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb1e0>'
    'zlange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb210>'
    'zlangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002bb240>'
    'zlanhb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb270>'
    'zlanhe': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb2a0>'
    'zlanhf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb2d0>'
    'zlanhp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb300>'
    'zlanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb330>'
    'zlanht': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x7f26002bb360>'
    'zlansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb390>'
    'zlansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb3c0>'
    'zlansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb3f0>'
    'zlantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb420>'
    'zlantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb450>'
    'zlantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb480>'
    'zlapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb4b0>'
    'zlapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bb4e0>'
    'zlapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bb510>'
    'zlaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb540>'
    'zlaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb570>'
    'zlaqhb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb5a0>'
    'zlaqhe': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb5d0>'
    'zlaqhp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb600>'
    'zlaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x7f26002bb630>'
    'zlaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002bb660>'
    'zlaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bb690>'
    'zlaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002bb6c0>'
    'zlaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bb6f0>'
    'zlaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bb720>'
    'zlaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bb750>'
    'zlaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bb780>'
    'zlaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb7b0>'
    'zlaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb7e0>'
    'zlaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0x7f26002bb810>'
    'zlar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb840>'
    'zlar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002bb870>'
    'zlarcm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bb8a0>'
    'zlarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f26002bb8d0>'
    'zlarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bb900>'
    'zlarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f26002bb930>'
    'zlarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f26002bb960>'
    'zlarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002bb990>'
    'zlarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f26002bb9c0>'
    'zlargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bb9f0>'
    'zlarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *)" at 0x7f26002bba20>'
    'zlarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002bba50>'
    'zlartg': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002bba80>'
    'zlartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002bbab0>'
    'zlarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f26002bbae0>'
    'zlarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bbb10>'
    'zlarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002bbb40>'
    'zlascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbb70>'
    'zlaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002bbba0>'
    'zlasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002bbbd0>'
    'zlassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0x7f26002bbc00>'
    'zlaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, int *, int *, int *)" at 0x7f26002bbc30>'
    'zlasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbc60>'
    'zlat2c': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0x7f26002bbc90>'
    'zlatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bbcc0>'
    'zlatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0x7f26002bbcf0>'
    'zlatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bbd20>'
    'zlatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002bbd50>'
    'zlatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bbd80>'
    'zlatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x7f26002bbdb0>'
    'zlauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbde0>'
    'zlauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbe10>'
    'zpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bbe40>'
    'zpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bbe70>'
    'zpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bbea0>'
    'zpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbed0>'
    'zpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbf00>'
    'zpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bbf30>'
    'zpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbf60>'
    'zpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbf90>'
    'zpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bbfc0>'
    'zpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002be030>'
    'zpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002be060>'
    'zpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be090>'
    'zpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be0c0>'
    'zpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be0f0>'
    'zpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be120>'
    'zporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be150>'
    'zposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be180>'
    'zposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be1b0>'
    'zpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be1e0>'
    'zpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be210>'
    'zpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be240>'
    'zpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be270>'
    'zppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be2a0>'
    'zppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be2d0>'
    'zpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be300>'
    'zppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be330>'
    'zppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be360>'
    'zpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002be390>'
    'zpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002be3c0>'
    'zpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be3f0>'
    'zpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be420>'
    'zpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be450>'
    'zptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be480>'
    'zpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be4b0>'
    'zptrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be4e0>'
    'zptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be510>'
    'zptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be540>'
    'zpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002be570>'
    'zpttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be5a0>'
    'zptts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002be5d0>'
    'zrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0x7f26002be600>'
    'zspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002be630>'
    'zspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002be660>'
    'zspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f26002be690>'
    'zsprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be6c0>'
    'zspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be6f0>'
    'zspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be720>'
    'zsptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be750>'
    'zsptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002be780>'
    'zsptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be7b0>'
    'zstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002be7e0>'
    'zstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002be810>'
    'zstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002be840>'
    'zstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0x7f26002be870>'
    'zsteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be8a0>'
    'zsycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002be8d0>'
    'zsyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002be900>'
    'zsyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0x7f26002be930>'
    'zsymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002be960>'
    'zsyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002be990>'
    'zsyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002be9c0>'
    'zsysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002be9f0>'
    'zsysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bea20>'
    'zsyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002bea50>'
    'zsytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002bea80>'
    'zsytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002beab0>'
    'zsytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002beae0>'
    'zsytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002beb10>'
    'zsytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002beb40>'
    'zsytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002beb70>'
    'zsytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002beba0>'
    'ztbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bebd0>'
    'ztbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bec00>'
    'ztbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bec30>'
    'ztfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002bec60>'
    'ztftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bec90>'
    'ztfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002becc0>'
    'ztfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002becf0>'
    'ztgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bed20>'
    'ztgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002bed50>'
    'ztgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x7f26002bed80>'
    'ztgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x7f26002bedb0>'
    'ztgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bede0>'
    'ztgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002bee10>'
    'ztgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bee40>'
    'ztgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *)" at 0x7f26002bee70>'
    'ztpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002beea0>'
    'ztpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002beed0>'
    'ztpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bef00>'
    'ztpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002bef30>'
    'ztprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002bef60>'
    'ztprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002bef90>'
    'ztptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002befc0>'
    'ztptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0030>'
    'ztpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002c0060>'
    'ztpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0090>'
    'ztrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002c00c0>'
    'ztrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002c00f0>'
    'ztrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0x7f26002c0120>'
    'ztrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002c0150>'
    'ztrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0180>'
    'ztrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002c01b0>'
    'ztrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0x7f26002c01e0>'
    'ztrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0210>'
    'ztrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0240>'
    'ztrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0270>'
    'ztrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c02a0>'
    'ztrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c02d0>'
    'ztzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0300>'
    'zunbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0330>'
    'zuncsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0x7f26002c0360>'
    'zung2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002c0390>'
    'zung2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002c03c0>'
    'zungbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c03f0>'
    'zunghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0420>'
    'zungl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002c0450>'
    'zunglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0480>'
    'zungql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c04b0>'
    'zungqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c04e0>'
    'zungr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f26002c0510>'
    'zungrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0540>'
    'zungtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0570>'
    'zunm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c05a0>'
    'zunm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c05d0>'
    'zunmbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0600>'
    'zunmhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0630>'
    'zunml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c0660>'
    'zunmlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0690>'
    'zunmql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c06c0>'
    'zunmqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c06f0>'
    'zunmr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c0720>'
    'zunmr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c0750>'
    'zunmrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c0780>'
    'zunmrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c07b0>'
    'zunmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0x7f26002c07e0>'
    'zupgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c0810>'
    'zupmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f26002c0840>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg.cython_lapack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2600296f60>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/linalg/cython_lapack.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

