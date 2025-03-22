all:
#g++ -Wno-write-strings PI_genAddr.cpp -o hiiu
#g++ -o hiiu PI_genAddr.cpp -lcrypto -lsodium -lbip39
	g++ -o hiiu test.cpp -lcrypto -lsodium -I/usr/include/python3.8 -lpython3.8 
# g++ -o test1 test1.cpp -lsodium

clean:
	@rm -f hiiu
	@echo clean done !