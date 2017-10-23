# example of configuration file

tag = 'ggH_SF_1j_dymvaOptim'

# used by mkShape to define output directory for root files
outputDir = 'rootFile_1j_dymvaOptim'


# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts_1j_dymvaOptim.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 



# luminosity to normalize to (in 1/fb)
lumi = 35.867

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plotGGH_SF_signal'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
