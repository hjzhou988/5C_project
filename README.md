# Analysis of enrichment of Klf4 and other factors in chromatin looping interactions in ESC.  

## Get_Intersection_set_outputbed_Dstn.py
Given two protein's ChIP-seq "summit" data, figuring out their common locations. The distance between two summits less than variable "Dstn" is considered common. "Dstn" is set 200 bp by default.

## Find_TF_alone_sites_Dstn.py
Given two protein's ChIP-seq "summit" data, figuring out the first protein's unique locations. Same as "Get_Intersection_set_outputbed_Dstn.py", the distance between two summits less than variable "Dstn" is considered common. "Dstn" is set 200 bp by default.

## Return_TF_sites_in_5C_regions.py
Find the subset of a protein's summits data that intersect with 5C region.

## enrichment_score.ipynb
Calculate the enrichment score for the pair of proteins that you are interested in. The enrichment score is defined as the number of common locations (intersection) devided by the number of union. 

## Calculate_fraction_and_p_value_and_then_plot.ipynb
Enrichment analysis of TF in chromatin looping interactions. For each condition (">0",">1",">2",">3"), calculate the fold change in significant loops compared to non-significant loops. Also calculate the p value from Fisher's exact test. Finally, plot all conditions into one graph. 

ChIP-seq data source:
- Chronis C, Fiziev P, Papp B, Butz S, Bonora G, Sabri S, Ernst J, Plath K. 2017. Cooperative Binding of Transcription Factors Orchestrates Reprogramming. Cell 168: 442–459.e20.
- Phillips-Cremins JE, Sauria MEG, Sanyal A, Gerasimova TI, Lajoie BR, Bell JSK, Ong C-T, Hookway TA, Guo C, Sun Y, et al. 2013. Architectural protein subclasses shape 3D organization of genomes during lineage commitment. Cell 153: 1281–1295.

5C data source:
- Phillips-Cremins JE, Sauria MEG, Sanyal A, Gerasimova TI, Lajoie BR, Bell JSK, Ong C-T, Hookway TA, Guo C, Sun Y, et al. 2013. Architectural protein subclasses shape 3D organization of genomes during lineage commitment. Cell 153: 1281–1295.
