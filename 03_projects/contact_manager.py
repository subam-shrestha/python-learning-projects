"""
PASSWORD STRENGTH CHECKER
Check if password is strong enough
"""

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters needed")
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")
    
    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Add numbers")
    
    # Check for special characters
    if any(c in "!@#$%^&*()_+-=" for c in password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%)")
    
    # Determine strength
    if score == 5:
        return "🔒 STRONG PASSWORD!", feedback
    elif score >= 3:
        return "⚠️ MEDIUM PASSWORD", feedback
    else:
        return "❌ WEAK PASSWORD", feedback

# Main
print("🔐 PASSWORD STRENGTH CHECKER\n")
password = input("Enter password to check: ")

strength, tips = check_password_strength(password)

print(f"\n{strength}")
if tips:
    print("\nImprovement tips:")
    for tip in tips:
        print(tip)
else:
    print("✅ Your password is secure!")


#tbh this was confusing to me at first, but i think i understand it now. the function check_password_strength takes a password as input and checks it against several criteria (length, uppercase, lowercase, numbers, special characters). It keeps track of a score and provides feedback on how to improve the password if it's not strong enough. The main part of the code prompts the user for a password and then displays the strength and any improvement tips.