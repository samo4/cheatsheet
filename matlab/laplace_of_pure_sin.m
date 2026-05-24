% laplace_of_pure_sin.m
% Analytical surface plot of |X(s)| for x(t) = A*sin(2*pi*f0*t)*u(t).
%
%   X(s) = A*w0 / (s^2 + w0^2)     (one-sided Laplace, ROC: Re(s) > 0)
%
% Both axes are in rad/s (sigma and omega) so the pole shape is isotropic:
%   |X(s)| ≈ 1/(2|s-s0|) near each pole, equally sharp in all directions.
% Displaying in Hz vs 1/s would compress the peak ~470x in the freq axis.
%
% Z-axis uses log10 so the cone shape is visible over several decades
% rather than appearing as an invisible needle above a flat floor.

function laplace_of_pure_sin()

close all;

A  = 1;
f0 = 100;        % signal frequency [Hz]
w0 = 2*pi*f0;    % rad/s  (≈ 628)

%% s-plane grid — both axes in rad/s for an isotropic pole shape
wRange = 1.2 * w0;                        % show ±120 % of w0
sigma  = linspace(-wRange, wRange, 200);

% Non-uniform omega: coarse background + fine patches near ±w0
w_coarse = linspace(-wRange, wRange, 300)';
w_fine_p = linspace( w0-30,  w0+30, 300)';
w_fine_n = linspace(-w0-30, -w0+30, 300)';
omega = unique([w_coarse; w_fine_p; w_fine_n]);

[S, W] = meshgrid(sigma, omega);
s = S + 1i * W;

%% Analytical X(s): height = log|X|, colour = phase
%  log10 linearises the 1/r singularity → pole shape visible as a broad cone
%  HSV colormap (cyclic) encodes phase: 0→red, ±π→cyan, wraps seamlessly
Xs        = A * w0 ./ (s.^2 + w0^2);
Xmag_disp = log10(min(abs(Xs), 1e4) + 1e-4);   % height: log|X|
Xphase    = angle(Xs);                           % colour: ∠X(s) ∈ [-π, π]

zFloor = log10(1e-4);   % floor level for overlays

%% Plot
fig = figure(1); clf;
fig.Units    = 'centimeters';
fig.Position = [2 2 14 12];

surf(S, W, Xmag_disp, Xphase, 'EdgeColor', 'none');  % Z=magnitude, C=phase
colormap hsv;         % cyclic: ±π map to same hue, pole winding is visible
caxis([-pi pi]);
colorbar('Ticks', [-pi -pi/2 0 pi/2 pi], 'TickLabels', {'-π', '-π/2', '0', 'π/2', 'π'});
shading interp;
camlight left;
camlight(-60, -10);
lighting phong;
material([0.3 0.7 0.4 12]);
hold on;

% Fourier slice: orange dashed line at sigma = 0 on the floor
wLine = linspace(-wRange, wRange, 400);
plot3(zeros(size(wLine)), wLine, repmat(zFloor, size(wLine)), ...
  '--', 'Color', [0.85 0.33 0], 'LineWidth', 1.5);

% Pole markers (×) on the floor plane
plot3(0,  w0, zFloor, 'rx', 'MarkerSize', 12, 'LineWidth', 2);
plot3(0, -w0, zFloor, 'rx', 'MarkerSize', 12, 'LineWidth', 2);

xlabel('\sigma [rad/s]'); ylabel('i\omega [rad/s]'); zlabel('log_{10}(|X(s)|)');
ylim([-wRange wRange]); xlim([-wRange wRange]);
view(55, 30);
grid on;
title(sprintf('height=lg|X(s)|,  colour=angle(X(s)),  f_0=%d Hz', f0));
view(25, 25);

%% Export
try
  scriptDir = fileparts(mfilename('fullpath'));
  outDir    = fullfile(scriptDir, '..', 'figures');
  if ~exist(outDir, 'dir')
    mkdir(outDir);
  end
  exportgraphics(gcf, fullfile(outDir, 'laplace_sin.png'), 'Resolution', 300);
catch ME
  warning('Failed to export figure: %s', ME.message);
end

end
