
from neuron import h
# create pre - and post - synaptic sections

h.load_file("pyramidal_cell_23.hoc")

pyramidal = h.PYRAMIDAL()
pyramidal.celldef()

stim = h.NetStim()
stim.number = 100000
stim.start = 0
stim.interval = 50
stim.noise=1
# create a synapse in the pre - synaptic section

#exponential synapse (AMPA like)
syn = h.ExpSyn (1 , sec = pyramidal.apic[16] )
syn2 = h.ExpSyn (0.5 , sec = pyramidal.apic[12] )
syn3 = h.ExpSyn (0.25 , sec = pyramidal.soma)

#syn = h.FDSExp2Syn (1 , sec = pyramidal.apic[16] )
#syn2 = h.FDSExp2Syn (1 , sec = pyramidal.apic[12] )
#syn3 = h.FDSExp2Syn (0.5 , sec = pyramidal.soma )

#Synapse with depression (I need to understand how to change parameters)
#syn_exp = h.FDSExp2Syn (1, sec= cable1)

	
# connect the netstim do the synaptic object


#if you change the order of de delays (10, 5, 1)(Wheights: 0.75),
#you can see orientation selectivity in the ExpSyn synapse model

#syn.d1=1
#syn.tau_D1=800
#syn.f=2
#syn.tau_D2=20000


nc = h.NetCon( stim , syn)
nc.weight[0] = 1
nc.delay = 21.0


#nc2 = h.NetCon( stim2 , syn2)
nc2 = h.NetCon( stim, syn2)
nc2.weight[0] = 1
nc2.delay = 11.0

#nc3 = h.NetCon( stim3 , syn3)
nc3 = h.NetCon( stim , syn3)
nc3.weight[0] = 1
nc3.delay = 1.0


vec = {}
for var in 'v_pre', 'v_apic16', 'i_syn', 'i_syn2','i_syn3','t', 'v_soma', 'v_apic12':
	vec[ var ] = h.Vector()
# record the membrane potentials and
# synaptic currents
#vec[ 'v_apic16'].record ( post (0.5)._ref_v )
vec[ 'v_apic16'].record ( pyramidal.apic[16](1)._ref_v )
#vec[ 'i_syn'].record ( syn._ref_i )
vec['v_soma'].record (pyramidal.soma(0.5)._ref_v)
vec['v_apic12'].record (pyramidal.apic[12](0.5)._ref_v)

#record current of different synapses: 
#vec[ 'i_syn'].record ( syn_exp._ref_i )
vec[ 'i_syn'].record ( syn._ref_i )
vec[ 'i_syn2'].record ( syn2._ref_i )
vec[ 'i_syn3'].record ( syn3._ref_i )
vec[ 't'].record (h._ref_t )
# run the simulation
apcount = h.APCount(pyramidal.soma(0.5))
apcount.thresh = 1

h.load_file("stdrun.hoc")
h.init()
h.tstop = 1000.0




import numpy as np
frequencies_to_analyse = 40
stim.interval = 10
spikecount = []
xaxis = []


f = open('frequency_analysis.csv', 'w')
f.write("Frequency of stimulation, Spike count\n")
for i in range(frequencies_to_analyse-1):
	h.run()
	if i==0:
		spikecount.append(apcount.n)
	out_string = str(1000/stim.interval) + "," + str(apcount.n) + "\n"
	spikecount.append(apcount.n)
	xaxis.append(1000/stim.interval)
	stim.interval +=5
	#print stim.interval
	f.write(str(out_string))
f.close()


import matplotlib.pyplot as plt

#xs = list(range(10, 40, 5))

plt.subplot(2,1,1)
plt.plot(spikecount)
plt.subplot(2,1,2)
plt.plot(xaxis)
plt.show()

"""

#print "number of spikes = ",apcount.n

# plot the results
#import pylab
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import matplotlib.patches as mpatches



plt.subplot(3 ,1 ,1)
lines1=plt.plot( vec[ 't'] ,vec['v_apic12'], label='apical[12]')
plt.setp(lines1, linewidth=1.5)
lines2 = plt.plot( vec['t'], vec['v_apic16'], label='apical[16]')
plt.title('apical voltages')
plt.setp(lines2, linewidth=1.5)
# Place a legend above this legend, expanding itself to
# fully use the given bounding box.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.subplot(3 ,1 ,2)
lines3=plt.plot( vec['t'] ,vec['i_syn'],label='syn1') 
plt.setp(lines3, linewidth=1.5)
lines4=plt.plot(vec['t'] ,vec['i_syn2'], label='syn2')
plt.setp(lines4, linewidth=1.5)
lines5=plt.plot(vec['t'] ,vec['i_syn3'],label='syn3')
plt.setp(lines5, linewidth=1.5)
plt.title('Post-Synaptic currents (syn1, 2 and 3)')
# Place a legend above this legend, expanding itself to
# fully use the given bounding box.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)


plt.subplot(3 ,1 ,3)
plt.plot(vec[ 't'] ,vec['v_soma'],label='soma') 
plt.plot(vec['t'], vec['v_apic16'],label='apic[16]') 
plt.plot(vec['t'], vec['v_apic12'],label='apic[12]') 
plt.title('Apic16, Apic12 and soma voltages')
# Place a legend above this legend, expanding itself to
# fully use the given bounding box.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.tight_layout()
plt.savefig('./final_presentation_figures/pcell_expsyn_soma_away_noise0.png', dpi=300, bbox_inches='tight')
plt.show()
"""
