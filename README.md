# project_plasticity_GK

this is a project presented at LASCON VI, studying the effects of plasticity in neuronal gain control, was well as its relation with dendritic tree properties. 
In order to do that, we imported a morphological reconstruction of a pyramidal cell from neuromorpho.org.
Interestingly, this cell belonged to a guy with my age, 23 years old.
Then, we stimulated three diferent parts of the dendritic tree with different delay regimes. 

We were able see some differences in the output of our model, most due to poisson-noise properties and dendritic tree low-pass filtering. Roughly, we implemented a model that fired if the three local of stimulation were set in a temporal way as to allow charge accumulation in the soma, i.e., from the most distal part of the dendritic tree to the most proximal part. 
In the retina, we can see some ganglion cells which are direction selective. But, one importat regard is that, as in almost every physiological system, a purely passive approximation doesn't capture good insights of the phenomena. So, when one talks about direction selectivity in a passive model and a cell which has direction selectivity, those are, likely, different physiological processess (although passive properties are underlying both). 
