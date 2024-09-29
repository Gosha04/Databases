#include <iostream>

class qValue {
private:
    double massInitial;  // Mass of reactants (in amu)
    double massFinal;    // Mass of products (in amu)
    const double amuToMeV = 931.5; // Conversion factor from amu to MeV

public:
    // Constructor to initialize masses (default to 0)
    qValue(double initMass = 0.0, double finalMass = 0.0) 
        : massInitial(initMass), massFinal(finalMass) {}

    // Setters
    void setInitialMass(double initMass) {
        massInitial = initMass;
    }

    void setFinalMass(double finalMass) {
        massFinal = finalMass;
    }

    // Getters
    double getInitialMass() const {
        return massInitial;
    }

    double getFinalMass() const {
        return massFinal;
    }

    // Function to calculate Q-value (in MeV)
    double calculateQValue() const {
        return (massInitial - massFinal) * amuToMeV;
    }

    // Check if the reaction is exothermic (releases energy)
    bool isExothermic() const {
        return calculateQValue() > 0;
    }

    // Check if the reaction is endothermic (absorbs energy)
    bool isEndothermic() const {
        return calculateQValue() < 0;
    }
};

int main() {
    // Example of usage
    qValue reaction;

    // Set masses (for example, in atomic mass units - amu)
    reaction.setInitialMass(235.0439); // Example: Uranium-235
    reaction.setFinalMass(234.9930);   // Example: Product mass after decay

    // Calculate the Q-value
    double qValue = reaction.calculateQValue();
    
    // Output results
    std::cout << "Q-value: " << qValue << " MeV" << std::endl;

    // Determine if the reaction is exothermic or endothermic
    if (reaction.isExothermic()) {
        std::cout << "The reaction is exothermic (releases energy)." << std::endl;
    } else if (reaction.isEndothermic()) {
        std::cout << "The reaction is endothermic (absorbs energy)." << std::endl;
    } else {
        std::cout << "No energy change (Q-value is zero)." << std::endl;
    }

    return 0;
}
