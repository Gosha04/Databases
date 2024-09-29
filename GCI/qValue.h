#ifndef Q_VALUE_H
#define Q_VALUE_H

class qValue {
private:
    double massInitial;  // Mass of reactants (in amu)
    double massFinal;    // Mass of products (in amu)
    const double amuToMeV = 931.5; // Conversion factor from amu to MeV

public:
    // Constructor
    qValue(double initMass = 0.0, double finalMass = 0.0);

    // Setters
    void setInitialMass(double initMass);
    void setFinalMass(double finalMass);

    // Getters
    double getInitialMass() const;
    double getFinalMass() const;

    // Function to calculate Q-value (in MeV)
    double calculateQValue() const;

    // Check if the reaction is exothermic (releases energy)
    bool isExothermic() const;

    // Check if the reaction is endothermic (absorbs energy)
    bool isEndothermic() const;
};

#endif // Q_VALUE_H
