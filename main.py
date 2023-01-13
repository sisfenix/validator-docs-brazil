from validator_docs_brazil import CPFValidator

cpfValue = input('Digite seu CPF:')
cpfValidator = CPFValidator(cpfValue)

if cpfValidator.isCPF():
    print('CPF Valido')
else:
    print('CPF Invalido')