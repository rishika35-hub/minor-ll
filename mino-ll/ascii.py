
import os

def shichna_robodad():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Total Rows: 100+, Total Cols: 120
    rows = 110
    cols = 120

    for r in range(rows):
        line = ""
        for c in range(cols):
            # --- SECTION 1: HAIR & TOP BORDER ---
            if r < 5:
                line += "*"
            elif r < 20:
                # Hair Logic: Curved shape using column constraints
                if 40 < c < 80:
                    if r < 10: line += "@"
                    elif 45 < c < 75: line += "#"
                    else: line += "@"
                else:
                    line += "*"
            
            # --- SECTION 2: FOREHEAD ---
            elif r < 35:
                if 35 < c < 85:
                    # Forehead highlight logic
                    if 45 < c < 75: line += " "
                    else: line += "."
                else:
                    line += "*"

            # --- SECTION 3: EYES & EYEBROWS ---
            elif r < 45:
                if 35 < c < 85:
                    # Eyebrows (r 36-38)
                    if r < 38:
                        if (40 < c < 55) or (65 < c < 80): line += "#"
                        else: line += "."
                    # Eyes Logic (r 40-43)
                    elif 40 <= r <= 43:
                        # Left Eye
                        if 42 <= c <= 52:
                            if c == 47: line += "@" # Pupil
                            else: line += "0"
                        # Right Eye
                        elif 68 <= c <= 78:
                            if c == 73: line += "@" # Pupil
                            else: line += "0"
                        else: line += " "
                    else: line += " "
                else:
                    line += "*"

            # --- SECTION 4: NOSE ---
            elif r < 65:
                if 35 < c < 85:
                    if 58 <= c <= 62:
                        line += "|"
                    elif r > 62 and 55 <= c <= 65:
                        line += "V"
                    else:
                        line += " "
                else:
                    line += "*"

            # --- SECTION 5: MOUTH & CHIN ---
            elif r < 80:
                if 35 < c < 85:
                    if 70 <= r <= 72 and 50 <= c <= 70:
                        line += "="
                    elif r > 75:
                        line += ":"
                    else:
                        line += "."
                else:
                    line += "*"

            # --- SECTION 6: COAT & SHOULDERS (The Scrolling Part) ---
            else:
                # Match-Case Example (Python 3.10+)
                # This handles the heavy scrolling coat area
                rem = r % 3
                match rem:
                    case 0:
                        if 10 < c < 110: line += "#"
                        else: line += "*"
                    case 1:
                        if 5 < c < 115: line += "%"
                        else: line += "*"
                    case _:
                        line += "@"
        
        print(line)

if __name__ == "__main__":
    shichna_robodad()