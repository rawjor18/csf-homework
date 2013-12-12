vop = lg_ppg / (lg_fga - lg_orb + lg_tov + 0.44 * lg_fta)
drb_per = (lg_trb - lg_orb) / lg_trb
factor = (2/3) - (0.5 * (lg_ast / lg_fg)) / (2 * (lg_fg / lg_ft))
poss =  0.5 * ((fga_t1 + 0.4 * fta_t1 - 1.07 * (orb_t1 / (orb_t1 + drb_opp)) * (fga_t1- fgm_t1) + to_t1) + (fga_opp + 0.4 * fta_opp - 1.07 * (orb_opp / (orb_opp + drb_t1)) * fga_opp - fgm_opp) + to_opp))

uPER = (1/mp) * [3p + (2/3) * ast + (2 - factor * (team_ast/team_fgm))*fgm + (ftm*0.5 * (1+(1-(team_ast/team_fgm))+(2/3)*(team_ast/team_fgm)))-vop*tov-vop*drb_per*(fga-fgm)-vop*0.44*(0.44+(0.56*drb_per))*(fta-ftm)+vop*(1-drb_per)*(trb-orb)+vop*drb_per*orb+vop*stl+vop*drb_per*blk-pf*((lg_ftm/lg_pf) - 0.44*(lg_fta/lg_pf)*vop)]