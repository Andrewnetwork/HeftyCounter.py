# HeftyNumber.py
HeftyNumber is a library built upon Numpy for doing arithmetic in arbitrary bases with arbitrary precision. 

I hope that this library will shape up to be a useful tool for anyone studying number theory or combinatorics.

Port from my C++ Version: https://github.com/Andrewnetwork/breaking-the-code/blob/master/AndrewWork/Server/HeftyCounter.cpp

## Features
* Ability to count in any base. 
* Effortless base conversion. 
* Vector representation of large numbers. 

## Ratonale & History
I wrote a botnet that orchestrated the distributed solution of problems. At its core was a counting mechanism. 
The first conception of the system was used to brute force the cracking of passwords-- the simplest use case we thought of 
as students for distributed computing and problem solving. In order to do this, we would count in the base of the length 
of the password character lexicon, and every number in that base could be easily translated to a possible password in that 
character set. More importantly, ranges of numbers would represent password combinations. These password ranges would be 
sent to computers in the botnet whereupon the range of passwords would be tried against some locked file -- I designed 
it so that it would send the password range to an executable, making it more robust than I'm making it seem. This 
implementation can count in any arbitrary base and is extremely efficient. The size of the counter is only limited by 
the memory capacity of the host computer, as we numpy ndarray’s as the core data structure. 
