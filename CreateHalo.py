# CODE
import struct
from random import *
from math import *
from yt.utilities.sdf import load_sdf
from Halo import Halo
from thingking import loadtxt
from sdfpy import load_sdf

import thingking as tk
import sys

scale, id, desc_scale, desc_id, num_prog, pid, upid, desc_pid, phantom, \
    sam_mvir, mvir, rvir, rs, vrms, mmp, scale_of_last_MM, vmax, x, y, z, \
    vx, vy, vz, Jx, Jy, Jz, Spin, Breadth_first_ID, Depth_first_ID, \
    Tree_root_ID, Orig_halo_ID, Snap_num, Next_coprogenitor_depthfirst_ID, \
    Last_progenitor_depthfirst_ID, Rs_Klypin, M_all, M200b, M200c, M500c, \
    M2500c, Xoff, Voff, Spin_Bullock, b_to_a, c_to_a, A_x, A_y, A_z, \
    b_to_a_500c, c_to_a_500c, A_x_500c, A_y_500c, A_z_500c, T_over_U, \
    M_pe_Behroozi, M_pe_Diemer, Macc, Mpeak, Vacc, Vpeak, Halfmass_Scale, \
    Acc_Rate_Inst, Acc_Rate_100Myr, Acc_Rate_Tdyn = \
    loadtxt("hlist_1.00000.list", unpack=True)

# Get the filename to save
fileSave1 = "data1.xyzb"
fileSave2 = "data2.xyzb"


#Get the halo file to open
#filenames = "hlist_0.55000.list"

#Load the halo data
#Halo_data = tk.loadtxt(filenames)

#openning the file to save the converted data
file1 = open(fileSave1, 'wb')
file2 = open(fileSave2, 'wb')
#----------------------	
# Writing the halo data
#----------------------

OldMinH1 = min(vmax)
OldMaxH1 = max(vmax)
NewMinH1 = 0.0
NewMaxH1 =300.0
OldRangeH1 = (OldMaxH1 - OldMinH1)
NewRangeH1 = (NewMaxH1 - NewMinH1)


#looping through data and writting the data to file
for h in range (0, len(x)):
	newVal1 = (((vmax[h] - OldMinH1) * NewRangeH1)/OldRangeH1) + NewMinH1
	file1.write (struct.pack('ddddddd', x[h], y[h], z[h], rvir[h]/1000.0, newVal1, mvir[h], 2.0))
     
#closing the the file
file1.close

OldMinH2 = min(mvir)
OldMaxH2 = max(mvir)
NewMinH2 = 0.0
NewMaxH2 =300.0
OldRangeH2 = (OldMaxH2 - OldMinH2)
NewRangeH2 = (NewMaxH2 - NewMinH2)

#looping through data and writting the data to file
for h in range (0, len(x)):
        newVal2 = (((mvir[h] - OldMinH2) * NewRangeH2)/OldRangeH2) + NewMinH2
        file2.write (struct.pack('ddddddd', x[h], y[h], z[h], rvir[h]/1000.0, newVal2, mvir[h], 2.0))

#closing the the file
file2.close

