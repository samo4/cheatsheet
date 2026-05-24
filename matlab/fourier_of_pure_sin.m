% fourier_sin.m
% Numerical verification of the Fourier Transform of a 100 Hz sine wave.
% "Real-world" flavour: finite measurement window, additive noise, Hann taper.
%
% Expected results (matches tikz figure in CONTROL.md):
%   Magnitude : peaks of A/2 at f = ±100 Hz
%   Phase     : -pi/2 at f = +100 Hz,  +pi/2 at f = -100 Hz
%               chaotic / random everywhere else (undefined in theory)

function fourier_of_pure_sin()

close all;

A  = 1;
f0 = 100;      % signal frequency [Hz]
Fs = 10000;    % sample rate [Hz]

%% Signal: sine with additive Gaussian noise
T = 0.5;
t = (0 : 1/Fs : T - 1/Fs)';
noise_amplitude = 0.25;
x = A * sin(2*pi*f0 * t) + noise_amplitude * randn(size(t));

%% Windowed FFT with zero-padding
% Use a local Hann window implementation to avoid Signal Processing Toolbox
N = length(t);
if N > 1
  win = 0.5 * (1 - cos(2*pi*(0:N-1)'/(N-1)));
else
  win = 1;
end
x_w  = x .* win;

NFFT = 2^nextpow2(length(t) * 16);            % 16x zero-padding → ~0.12 Hz bins
X    = fftshift(fft(x_w, NFFT)) / sum(win);   % amplitude-correct for Hann window
f    = (-NFFT/2 : NFFT/2-1)' * (Fs / NFFT);

%% values at ±100 Hz
[~, ip] = min(abs(f - f0));
[~, in] = min(abs(f + f0));

%% Plot
fLim = 300;

figure(1);
clf;
fig = gcf;
fig.Units = 'centimeters';
fig.Position = [2 2 20 10];

% --- Left
subplot(1,2,1);
plot(f, abs(X), '-', 'Color', [0.6 0.6 0.6], 'LineWidth', 0.6); hold on;
plot(f, abs(X), '.', 'Color', [0.2 0.2 0.2], 'MarkerSize', 6);
xlim([-fLim fLim]);
ylabel('|X(f)|'); xlabel('Frequency [Hz]');
title('|sin 100Hz + noise|');
grid on; hold off;

% --- Right
subplot(1,2,2);

ph = angle(X);
plot(f, ph, '-', 'Color', [0.9 0.9 0.9]); hold on;
plot(f(ip), ph(ip), 'bo', 'MarkerFaceColor','b', 'MarkerSize',5);
plot(f(in), ph(in), 'bo', 'MarkerFaceColor','b', 'MarkerSize',5);

xlim([-fLim fLim]); ylim([-pi pi]);
yticks([-pi -pi/2 0 pi/2 pi]);
yticklabels({'-π', '-π/2', '0', 'π/2', 'π'});
ylabel('∠X(f)');  xlabel('Frequency [Hz]');
title('Phase with highlight at ±100 Hz');
grid on; hold off;

% --- Export figure to project figures/ directory (PNG + PDF)
try
  scriptDir = fileparts(mfilename('fullpath'));
  outDir = fullfile(scriptDir, '..', 'figures');
  if ~exist(outDir, 'dir')
    mkdir(outDir);
  end
  exportgraphics(gcf, fullfile(outDir, 'fourier_sin.png'), 'Resolution', 300);
catch ME
  warning('Failed to export figure: %s', ME.message);
end

