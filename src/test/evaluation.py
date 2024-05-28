# Função para gerar um conjunto de hashes transformados para diferentes senhas
from src.main import transform_password

def generate_transformed_hashes(password_list):
    transformed_hashes = {}
    for password in password_list:
        transformed_hashes[password] = transform_password(password)
    return transformed_hashes

def evaluate_collisions(transformed_hashes):
    unique_hashes = set(transformed_hashes.values())
    return len(unique_hashes) != len(transformed_hashes)

def brute_force_attack(password_list, target_hash):
    for password in password_list:
        if transform_password(password) == target_hash:
            return password
    return None

def statistical_attack(transformed_hashes):
    hash_counts = {}
    for h in transformed_hashes.values():
        if h in hash_counts:
            hash_counts[h] += 1
        else:
            hash_counts[h] = 1
    
    for count in hash_counts.values():
        if count > 1:
            return True
    return False

def evaluate_security(password_list):
    transformed_hashes = generate_transformed_hashes(password_list)
    
    collisions = evaluate_collisions(transformed_hashes)
    if collisions:
        print("Colisões encontradas.")
    else:
        print("Nenhuma colisão encontrada.")
    
    target_password = password_list[0]
    target_hash = transformed_hashes[target_password]
    cracked_password = brute_force_attack(password_list, target_hash)
    if cracked_password:
        print(f"Ataque de força bruta bem-sucedido. Senha: {cracked_password}")
    else:
        print("Ataque de força bruta falhou.")
    
    statistical_attack_result = statistical_attack(transformed_hashes)
    if statistical_attack_result:
        print("Vulnerável a ataques estatísticos.")
    else:
        print("Resistente a ataques estatísticos.")