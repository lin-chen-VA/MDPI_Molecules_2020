function barPlot(xlsxFileName)
    array = xlsread(xlsxFileName);
    bar(array);
    xticks(1:1:18);
    xticklabels({'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL'});
    xtickangle(90);