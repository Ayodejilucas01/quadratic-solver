import cmath

def get_number(prompt, allow_zero=True):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Try again.")
            continue
        try:
            value = float(user_input)
            if not allow_zero and value == 0:
                print("a Cannot Be Zero - not a quadratic equation")
                continue
            return value
        except ValueError:
            print("Use Numbers not Words - try again")

def format_root(r):
    # If almost real, show as real
    if abs(r.imag) < 1e-9:
        # format to remove useless zeros
        if abs(r.real) < 1e-9:
            return "0"
        return f"{r.real:.4f}".rstrip('0').rstrip('.')
    # Complex
    real_part = r.real
    imag_part = r.imag
    
    if abs(real_part) < 1e-9:
        return f"{imag_part:.4f}j".rstrip('0').rstrip('.').replace('.j','j')
    
    real_str = f"{real_part:.4f}".rstrip('0').rstrip('.')
    imag_abs_str = f"{abs(imag_part):.4f}".rstrip('0').rstrip('.')
    sign = "+" if imag_part >= 0 else "-"
    return f"{real_str} {sign} {imag_abs_str}j"

def solve_once():
    print("\n--- New Equation ---")
    a = get_number("Enter a: ", allow_zero=False)
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")

    print(f"\nSolving: {a}x² + {b}x + {c} = 0")
    D = (b ** 2) - (4 * a * c)
    print(f"Discriminant = {D}")

    sqrt_D = cmath.sqrt(D)
    x1 = (-b + sqrt_D) / (2 * a)
    x2 = (-b - sqrt_D) / (2 * a)

    if D > 0:
        print("Two distinct real roots:")
    elif abs(D) < 1e-9:
        print("One repeated real root:")
    else:
        print("Two complex roots:")

    print(f"x1 = {format_root(x1)}")
    print(f"x2 = {format_root(x2)}")

def main():
    print("=== QUADRATIC SOLVER ===")
    print("Solves ax² + bx + c = 0")
    
    while True:
        solve_once()
        
        while True:
            again = input("\nSolve again? (y/n): ").strip().lower()
            if again in ('y', 'yes'):
                break
            elif again in ('n', 'no'):
                print("\nThanks! Bye.")
                return
            else:
                print("Please type y or n")

if __name__ == "__main__":
    main()
