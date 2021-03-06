# cuts

#cuts = {}
#eleWP='cut_WP_Tight80X'
# eleWP='cut_WP_Tight80X_SS'  
# eleWP='mva_80p_Iso2015'
# eleWP='mva_80p_Iso2016'
# eleWP='mva_90p_Iso2015'
#eleWP='mva_90p_Iso2016'
  
supercut = 'mllmin3l>12  \
            && std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>20 \
            && std_vector_lepton_pt[2]>15 \
            && std_vector_lepton_pt[3]<10 \
            && abs(chlll) == 1 \
           '
cuts['preselection']   = '1'

cuts['2jet_cut'] = ' ( std_vector_jet_pt[0] >= 30 ) \
                   && ( std_vector_jet_pt[1] >= 30 ) \
                 '
 #11 = e
# 13 = mu
# 15 = tau

