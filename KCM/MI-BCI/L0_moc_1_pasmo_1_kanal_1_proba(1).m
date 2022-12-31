clear all; close all;
load dataset_BCIcomp1

Fs=128;
macierzCech = [];
pasma = [8 13; 13 30];
cecha = 0;
x_znormalizowane = [];

for i=1 : 1 : 2
    %Projekt filtra rzedu 4 przepuszczajacego czestotliwosci w pasmie 1-4Hz
    [a(i,:),b(i,:)]=butter(4,[pasma(i,:)]/(Fs/2),'bandpass');
end

for i=1 : 1 : 140
    cecha = 0;
    for k=1 : 1 : 2
        for j=1 : 1 : 3
        
            cecha= cecha+1;

            %Wybor sygnalu
            signal=x_train(:,j,i);
                       
            %Przefiltrowanie wybranego sygnalu zgodnie z zaprojektowanym filtrem
            sygnalFiltered=filter(a(k,:),b(k,:),signal);
            
            %Wyznaczenie mocy sygnalu w zadanym pasmie czestotliwosci
            macierzCech(i, cecha)=mean(sygnalFiltered.^2);
        end
    end
end

%Normalizacja
for i=1 : 1 : 6
    x_max = max(macierzCech(:,i));
    x_min = min(macierzCech(:,i));
    for j=1 : 1 : 140
        znormalizowana =  (macierzCech(j,i)-x_min)/(x_max-x_min);
        x_znormalizowane(j,i) = znormalizowana;
    end
end

%Podzial na zbior uczacy i testowy

cechyTren = [];
cechyTest = [];
klasyTren = [];
klasyTest = [];

for i=1 : 1 : 140
    if mod(i,5) == 0
           cechyTest(i,:) = x_znormalizowane(i,:);
           klasyTest(i) = y_train(i);
    else
           cechyTren(i,:) = x_znormalizowane(i,:);
           klasyTren(i) = y_train(i);
    end
end

cechyTest = nonzeros(cechyTest);
cechyTren = nonzeros(cechyTren);

klasyTest = nonzeros(klasyTest);
klasyTren = nonzeros(klasyTren);




