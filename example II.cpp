#include <iostream>
#include <memory>
#include <map>
#include <functional>
#include <type_traits>

// Template-Klasse zur Erstellung von Objekten
template <typename Base, typename... Args>
class Factory {
public:
    using CreatorFunc = std::function<std::unique_ptr<Base>(Args...)>;

    template <typename Derived>
    void registerType(const std::string& name) {
        static_assert(std::is_base_of<Base, Derived>::value, "Derived muss von Base erben");
        creators[name] = [](Args... args) {
            return std::make_unique<Derived>(std::forward<Args>(args)...);
        };
    }

    std::unique_ptr<Base> create(const std::string& name, Args... args) const {
        auto it = creators.find(name);
        if (it != creators.end()) {
            return it->second(std::forward<Args>(args)...);
        }
        return nullptr;
    }

private:
    std::map<std::string, CreatorFunc> creators;
};

// Basisklasse
class Animal {
public:
    virtual void speak() const = 0;
    virtual ~Animal() = default;
};

// Abgeleitete Klassen
class Dog : public Animal {
public:
    void speak() const override {
        std::cout << "Woof!" << std::endl;
    }
};

class Cat : public Animal {
public:
    void speak() const override {
        std::cout << "Meow!" << std::endl;
    }
};

int main() {
    Factory<Animal> animalFactory;

    // Registrierung der Klassen
    animalFactory.registerType<Dog>("Dog");
    animalFactory.registerType<Cat>("Cat");

    // Objekte erstellen
    auto dog = animalFactory.create("Dog");
    auto cat = animalFactory.create("Cat");

    if (dog) dog->speak();
    if (cat) cat->speak();

    return 0;
}
