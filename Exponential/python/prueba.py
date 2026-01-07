#import matplotlib
#import matplotlib.pyplot as plt
import numpy as np
from classy import Class
#from scipy.optimize import fsolve
#from scipy.interpolate import interp1d
import math
k_out=[0.1]#unidades de 1/Mpc

common_settings = {# we need to set the output field to something although
                   # the really releveant outpout here will be set with 'k_output_values'
                  'output':'mPk,tCl,pCl,lCl',
                   'P_k_max_1/Mpc':3.0,
                   # value of k we want to polot in [1/Mpc]
                   'k_output_values': str(k_out).strip('[]'),
                   # LambdaCDM parameters
                   'h':0.6732117,
                   'Omega_fld' : 0,
                   'Omega_smg' : -1,
                   'Omega_Lambda': 0.69,
                   'Omega_b':0.02238280,
                   'Omega_cdm':0,
                   'gravity_model':'quintessence_monomial',
                   'x0_schm':1,
                   'theta_schm':2.7e-16,
                   'DM_schm':0.26,
                   'h_schm':1,
                   'V0_schm':1,
                   'lambda_schm':1,
                   #'m_phi_schm':1e-14,
                   'A_s':2.100549e-09 ,
                   'n_s':0.9660499,
                   'tau_reio':0.05430842,
                # Take fixed value for primordial Helium (instead of automatic BBN adjustment)
                  # 'YHe': 0.2454006,
                   # other options and settings
                   'compute damping scale':'yes', # needed to output the time of damping scale crossing
                   #'lensing':'yes'
                    }

m=Class()
m.set(common_settings)
m.compute()
