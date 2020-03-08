function HPlot3(XRayFileName, EMFileName1, EMFileName2, EMFileName3, EMFileName4, EMFileName5, EMFileName6)
    XRay = csvread(XRayFileName);
    EM1 = csvread(EMFileName1);
    EM2 = csvread(EMFileName2);
    EM3 = csvread(EMFileName3);
    %EM4 = csvread(EMFileName4);
    %EM5 = csvread(EMFileName5);
    %EM6 = csvread(EMFileName6);
    
    %HPlotSum(XRay, EM1, EM2, EM3, EM4, EM5, EM6);
    HPlotSum(XRay, EM1, EM2, EM3);

end

function HPlotSum(XRay, EM1, EM2, EM3)
    cutoff = 10;
    XHBOS = sum(XRay(:, 1:5), 2);
    t = size(XHBOS, 1);
    a = size(XHBOS(XHBOS>cutoff), 1);
    fprintf('number: %d, # of greater than the cutoff: %d, ratio: %f%%\n', t, a, a/t*100);
    EMHBOS1 = sum(EM1(:, 1:5), 2);
    t = size(EMHBOS1, 1);
    a = size(EMHBOS1(EMHBOS1>cutoff), 1);
    fprintf('number: %d, # of greater than the cutoff: %d, ratio: %f%%\n', t, a, a/t*100);
    EMHBOS2 = sum(EM2(:, 1:5), 2);
    t = size(EMHBOS2, 1);
    a = size(EMHBOS2(EMHBOS2>cutoff), 1);
    fprintf('number: %d, # of greater than the cutoff: %d, ratio: %f%%\n', t, a, a/t*100);
    EMHBOS3 = sum(EM3(:, 1:5), 2);
    t = size(EMHBOS3, 1);
    a = size(EMHBOS3(EMHBOS3>cutoff), 1);
    fprintf('number: %d, # of greater than the cutoff: %d, ratio: %f%%\n', t, a, a/t*100);
    [xBins] = histc(XHBOS, 0:0.1:13);
    [emBins1] = histc(EMHBOS1, 0:0.1:13);
    [emBins2] = histc(EMHBOS2, 0:0.1:13);
    [emBins3] = histc(EMHBOS3, 0:0.1:13);
    fitX = 0:0.1:13;
    fitY = xBins;
    pd = fitdist(XHBOS(XHBOS<3),'Normal')
    norm = normpdf(0:0.1:13,1.07757,1.2);
    norm = norm/max(norm)/24;
    plot(0:0.1:13, norm);
    hold on;
    plot(0:0.1:13, xBins/sum(xBins), 'r', 'LineWidth', 3);
    hold on;
    plot(0:0.1:13, emBins1/sum(emBins1), 'b', 'LineWidth', 3);
    hold on;
    plot(0:0.1:13, emBins2/sum(emBins2), 'b-.', 'LineWidth', 3);
    hold on;
    plot(0:0.1:13, emBins3/sum(emBins3), 'c', 'LineWidth', 3);
end