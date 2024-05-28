# Função para gerar um conjunto de hashes transformados para diferentes senhas
from src.main import transform_password

def generate_transformed_hashes(password_list):
    transformed_hashes = {}
    for password in password_list:
        transformed_hashes[password] = transform_password(password)
    return transformed_hashes

def differential_attack(password):
    original_hash = transform_password(password)
    variations = [
        password + chr(i) for i in range(32, 127)
    ]  # Cria variações adicionando um caractere ASCII

    differences = {}
    for variation in variations:
        var_hash = transform_password(variation)
        if var_hash != original_hash:
            differences[variation] = var_hash

    return differences

def brute_force_attack(password_list, target_hash):
    for password in password_list:
        if transform_password(password) == target_hash:
            return password
    return None

def dictionary_attack(password_list, target_hash):
    for password in password_list:
        if transform_password(password) == target_hash:
            return password
    return None

def evaluate_security(password_list):
    transformed_hashes = generate_transformed_hashes(password_list)
    
    target_password = password_list[0]
    target_hash = transformed_hashes[target_password]
    cracked_password = brute_force_attack(password_list, target_hash)
    if cracked_password:
        print(f"Ataque de força bruta bem-sucedido. Senha: {cracked_password}")
    else:
        print("Ataque de força bruta falhou.")

def evaluate_security2(password_list, target_password):
    transformed_hashes = {pw: transform_password(pw) for pw in password_list}
    
    target_hash = transformed_hashes[target_password]
    
    cracked_password = dictionary_attack(password_list, target_hash)
    if cracked_password:
        print(f"Ataque de dicionário bem-sucedido. Senha: {cracked_password}")
    else:
        print("Ataque de dicionário falhou.")
    
    differential_results = differential_attack(target_password)
    if differential_results:
        print("Ataque diferencial encontrou variações:")
        for var, hash_val in differential_results.items():
            print(f"Variação: {var}, Hash: {hash_val}")
    else:
        print("Ataque diferencial não encontrou variações significativas.")