clear all; close all;
load dataset_BCIcomp1

Fs=128;

%Wybor sygnalu
signal=x_train(:,1,1);

%Projekt filtra rzedu 4 przepuszczajacego czestotliwosci w pasmie 1-4Hz
[a,b]=butter(4,[1 4]/(Fs/2),'bandpass');

%Przefiltrowanie wybranego sygnalu zgodnie z zaprojektowanym filtrem
sygnalFiltered=filter(a,b,signal);

%Wyznaczenie mocy sygnalu w zadanym pasmie czestotliwosci
moc=mean(sygnalFiltered.^2)
