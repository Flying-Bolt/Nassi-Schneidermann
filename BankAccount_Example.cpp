// =============================================================================
// BankAccount_Example.cpp
// Beispielprogramm für den Code Tree / Nassi-Shneidermann-Diagramm-Generator
// Thema: Einfaches Bankkonto-System
// =============================================================================

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <stdexcept>

// ─────────────────────────────────────────────────────────────
// Enum: Transaktionstyp
// ─────────────────────────────────────────────────────────────
enum class TransactionType {
    DEPOSIT,
    WITHDRAWAL,
    TRANSFER
};

// ─────────────────────────────────────────────────────────────
// Struct: Transaktion
// ─────────────────────────────────────────────────────────────
struct Transaction {
    TransactionType type;
    double          amount;
    std::string     description;

    Transaction(TransactionType t, double a, const std::string& desc)
        : type(t), amount(a), description(desc) {}
};

// ─────────────────────────────────────────────────────────────
// Klasse: BankAccount
// ─────────────────────────────────────────────────────────────
class BankAccount {
private:
    std::string              owner;
    std::string              accountNumber;
    double                   balance;
    std::vector<Transaction> history;

    static int accountCounter;

    std::string generateAccountNumber() {
        return "DE" + std::to_string(1000 + ++accountCounter);
    }

public:
    // Konstruktor
    BankAccount(const std::string& ownerName, double initialBalance = 0.0)
        : owner(ownerName), balance(initialBalance) {
        accountNumber = generateAccountNumber();
        if (initialBalance > 0) {
            history.emplace_back(TransactionType::DEPOSIT, initialBalance, "Eröffnungseinlage");
        }
    }

    // Einzahlen
    void deposit(double amount, const std::string& description = "Einzahlung") {
        if (amount <= 0) {
            throw std::invalid_argument("Einzahlungsbetrag muss positiv sein.");
        }
        balance += amount;
        history.emplace_back(TransactionType::DEPOSIT, amount, description);
    }

    // Abheben
    void withdraw(double amount, const std::string& description = "Abhebung") {
        if (amount <= 0) {
            throw std::invalid_argument("Abhebungsbetrag muss positiv sein.");
        }
        if (amount > balance) {
            throw std::runtime_error("Nicht genügend Guthaben.");
        }
        balance -= amount;
        history.emplace_back(TransactionType::WITHDRAWAL, amount, description);
    }

    // Überweisung an anderes Konto
    void transfer(BankAccount& target, double amount) {
        withdraw(amount, "Überweisung an " + target.getOwner());
        target.deposit(amount, "Überweisung von " + owner);
    }

    // Kontoauszug anzeigen
    void printStatement() const {
        std::cout << "\n╔══════════════════════════════════════════╗\n";
        std::cout << "║         KONTOAUSZUG                      ║\n";
        std::cout << "╠══════════════════════════════════════════╣\n";
        std::cout << "║ Inhaber:  " << std::left << std::setw(31) << owner << "║\n";
        std::cout << "║ Konto-Nr: " << std::left << std::setw(31) << accountNumber << "║\n";
        std::cout << "╠══════════════════════════════════════════╣\n";

        for (const auto& tx : history) {
            char sign = (tx.type == TransactionType::WITHDRAWAL) ? '-' : '+';
            std::cout << "║ " << sign
                      << std::setw(8) << std::fixed << std::setprecision(2) << tx.amount
                      << " EUR  " << std::left << std::setw(23) << tx.description << "║\n";
        }

        std::cout << "╠══════════════════════════════════════════╣\n";
        std::cout << "║ Kontostand: " << std::right << std::setw(10)
                  << std::fixed << std::setprecision(2) << balance
                  << " EUR              ║\n";
        std::cout << "╚══════════════════════════════════════════╝\n";
    }

    // Getter
    double      getBalance()       const { return balance; }
    std::string getOwner()         const { return owner; }
    std::string getAccountNumber() const { return accountNumber; }
    int         getTransactionCount() const { return static_cast<int>(history.size()); }
};

// Statisches Mitglied initialisieren
int BankAccount::accountCounter = 0;

// ─────────────────────────────────────────────────────────────
// Hilfsfunktion: Zinsen berechnen
// ─────────────────────────────────────────────────────────────
double calculateInterest(double balance, double rate, int years) {
    double result = balance;
    for (int i = 0; i < years; ++i) {
        result *= (1.0 + rate / 100.0);
    }
    return result - balance;
}

// ─────────────────────────────────────────────────────────────
// Hilfsfunktion: Konten vergleichen
// ─────────────────────────────────────────────────────────────
void compareAccounts(const BankAccount& a, const BankAccount& b) {
    std::cout << "\n--- Kontovergleich ---\n";
    if (a.getBalance() > b.getBalance()) {
        std::cout << a.getOwner() << " hat mehr Guthaben ("
                  << a.getBalance() << " EUR).\n";
    } else if (a.getBalance() < b.getBalance()) {
        std::cout << b.getOwner() << " hat mehr Guthaben ("
                  << b.getBalance() << " EUR).\n";
    } else {
        std::cout << "Beide Konten haben gleich viel Guthaben.\n";
    }
}

// ─────────────────────────────────────────────────────────────
// main
// ─────────────────────────────────────────────────────────────
int main() {
    std::cout << "=== Bankkonto-Beispielprogramm ===\n\n";

    // Konten anlegen
    BankAccount alice("Alice Müller", 1000.00);
    BankAccount bob("Bob Schmidt",    500.00);

    // Transaktionen
    alice.deposit(250.00, "Gehalt");
    alice.withdraw(80.00,  "Miete");
    alice.transfer(bob, 150.00);

    bob.deposit(300.00, "Freelance-Auftrag");
    bob.withdraw(50.00,  "Einkauf");

    // Kontoauszüge
    alice.printStatement();
    bob.printStatement();

    // Vergleich
    compareAccounts(alice, bob);

    // Zinsen berechnen
    double interest = calculateInterest(alice.getBalance(), 2.5, 5);
    std::cout << "\nZinsprognose für " << alice.getOwner()
              << " (2,5% p.a., 5 Jahre): +"
              << std::fixed << std::setprecision(2) << interest << " EUR\n";

    // Fehlerbehandlung demonstrieren
    std::cout << "\n--- Fehlerbehandlung ---\n";
    try {
        bob.withdraw(99999.00);
    } catch (const std::runtime_error& e) {
        std::cout << "Fehler abgefangen: " << e.what() << "\n";
    }

    std::cout << "\nProgramm beendet.\n";
    return 0;
}
