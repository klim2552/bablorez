# Торговая стратегия основанная на скользящих медианах

## Описание торговой системы

Данная торговая система включает в себя свод правил, по которым торговый советник принимает решения об открытии позиций по финансовым инструментам. Данная документация содержит следующие разделы:

-   Описание торговой стратегии, применяемой в данной системе;
    
-   Риск-менеджмент;
    
-   Блок-схема алгоритма.
    

### Описание торговой стратегии, применяемой в данной системе

Торговая стратегия основана основана на индикаторе технического анализа "Канал относительной волатильности". Суть данного индикатора строится на предположении, что цена финансового инструмента, по достижению границы канала или его пересечении, направиться в сторону другой границы канала.

Наглядно, это можно увидеть на рисунке ниже:
![alt text](https://github.com/klim2552/bablorez/blob/master/data/MM.JPG)

Здесь, "Канал относительной волатильности" образуют красная и синяя линии. Желтая линия является ценой финансового инструмента.

#### Описание индикатора.
"Канал относительной волатильности" строится по двум скользящим медианам.Методика расчета кажой из них следующая:

Скользящая медиана минимумов:

![alt text](https://github.com/klim2552/bablorez/blob/master/data/eqn.png) , где x - это значение минимума, а n число значений.

Скользящая медиана максимумов:

![alt text](https://github.com/klim2552/bablorez/blob/master/data/eqn1.png) , где x - это значение максимума, а n число значений.

Использование скользящей медианы вместо скользящей средней обусловлено тем, что скользящая медиана способна улавливать с наименьшей погрешностью видоизменения цен и давать более точные сигналы для открытия позиций. 
