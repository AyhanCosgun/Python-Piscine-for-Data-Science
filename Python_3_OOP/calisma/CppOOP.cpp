#include <iostream>
#include <string>

class Character {
public:
 virtual void die() = 0;
};

class Stark : public Character {
public:
    std::string first_name;

    Stark(std::string name) : first_name(name) {}
	void die() override {
		std::cout << first_name << " has died." << std::endl;
	}
};

int main() {

	return 0;
}

