# Rental Price Calculator

This project is a calculator developed in **Python** that allows users to calculate rental prices, including components such as the **4x1000 tax**, **VAT**, and other additional costs. It is ideal for managing financial costs and simplifying rental-related calculations for properties or services.

---

## Features

- **Initial Discount:** Automatically applies a 5% discount to the base rental price.
- **VAT Calculation:** Automatically calculates VAT (default 19%) based on the adjusted base price and additional costs.
- **4x1000 Tax Calculation:** Optionally includes the calculation of the 4x1000 financial tax.
- **Additional Costs:** Allows users to add other custom costs or fees.
- **Detailed Summary:** Provides a clear breakdown of the total calculation.
- **Simple User Interface:** Executable from the terminal or command line.

---

## Requirements

To run this project, you need:

- **Python 3.7 or higher**
- Standard Python library (no external packages required)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AngelScarpetta2004/Calculadora-de-precios-Arriendo.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Calculadora-de-precios-Arriendo
   ```

3. Run the script:
   ```bash
   python calculadora.py
   ```

---

## Usage

1. Enter the base price of the property or rental item.
2. Add additional costs when prompted (you can specify multiple costs).
3. Get the total calculation, including a breakdown of the discounted base price, VAT, 4x1000 tax (if applicable), and additional costs.

### Interactive Example:

When running the script, the program will request the following information:

- **Base price of the property:** Enter the initial rental value.
- **Additional costs:** Specify extra costs, such as maintenance or services. Enter "fin" ("end") when you are done adding costs.

### Expected Output:

If the base price is **$1,000,000**, with additional costs of **$50,000**, the calculation will be as follows:

- Discounted base price (5%): $950,000
- Additional costs: $50,000
- Taxable amount: $1,000,000
- VAT (19%): $190,000
- Total price without 4x1000: $1,190,000
- 4x1000 (0.4%): $4,000
- **Total price with 4x1000:** $1,194,000

---

## Main Code

The main file is [`calculadora.py`](https://github.com/AngelScarpetta2004/Calculadora-de-precios-Arriendo/blob/main/calculadora.py), which includes the functions necessary to perform the calculations. You can customize the rates and add new components as needed.

---

## Contribution

If you want to contribute:

1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Submit a pull request with your improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## Author

Developed by [Angel Scarpetta](https://github.com/AngelScarpetta2004).

---

## Future Improvements

- Integration with a graphical user interface (GUI).
- Automated calculations for multiple currencies.
- Report generation in PDF or Excel format.
