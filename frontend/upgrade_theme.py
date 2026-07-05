import re
import os

css_file = r"c:\Users\Mehedi\Desktop\Ai-Mentor\frontend\src\styles.css"
with open(css_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace root variables
content = re.sub(
    r":root \{.*?\n\}",
    """:root {
  font-family: 'Outfit', 'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif;
  color: #f8fafc;
  background: #020617;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  --ink: #f8fafc;
  --muted: #94a3b8;
  --subtle: #475569;
  --line: rgba(148, 163, 184, 0.2);
  --glass: rgba(15, 23, 42, 0.65);
  --glass-strong: rgba(15, 23, 42, 0.85);
  --field: rgba(15, 23, 42, 0.5);
  --accent: #8b5cf6;
  --accent-2: #2dd4bf;
  --cyan: #ec4899;
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #f43f5e;
  --shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6);
}""",
    content,
    flags=re.DOTALL,
)

# Replace background image and gradients in body
content = re.sub(
    r"body \{.*?background-attachment: fixed;\n\}",
    """body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
  background:
    radial-gradient(circle at 15% 50%, rgba(139, 92, 246, 0.15), transparent 25vw),
    radial-gradient(circle at 85% 30%, rgba(45, 212, 191, 0.15), transparent 25vw),
    linear-gradient(135deg, #020617 0%, #0f172a 100%);
  background-attachment: fixed;
}""",
    content,
    flags=re.DOTALL,
)

# Strip out before pseudo element for body
content = re.sub(r"body::before \{.*?\n\}", "", content, flags=re.DOTALL)

# Replace RGB values for accent colors
# Old Orange (249, 115, 22) -> Violet (139, 92, 246)
content = re.sub(r"249,\s*115,\s*22", "139, 92, 246", content)

# Old Yellow (251, 191, 36) -> Teal (45, 212, 191)
content = re.sub(r"251,\s*191,\s*36", "45, 212, 191", content)

# Old Cyan (125, 211, 252) -> Pink (236, 72, 153)
content = re.sub(r"125,\s*211,\s*252", "236, 72, 153", content)

# Old Background Dark Blue variants -> Slate variants
content = re.sub(r"3,\s*10,\s*18", "15, 23, 42", content)
content = re.sub(r"7,\s*17,\s*29", "15, 23, 42", content)
content = re.sub(r"12,\s*24,\s*38", "15, 23, 42", content)
content = re.sub(r"5,\s*13,\s*24", "15, 23, 42", content)
content = re.sub(r"8,\s*14,\s*24", "15, 23, 42", content)
content = re.sub(r"9,\s*30,\s*48", "15, 23, 42", content)
content = re.sub(r"13,\s*28,\s*44", "30, 41, 59", content)

# Replace solid hex colors used in gradients
content = content.replace("#ef4444", "var(--cyan)")
content = content.replace("#101f2f", "#0f172a")

# Make buttons look more modern (remove heavy box shadow from primary button)
content = re.sub(
    r"\.primary-button,\s*\.full-button\s*\{.*?\n\}",
    """.primary-button,
.full-button {
  color: #ffffff;
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  box-shadow: 0 8px 24px rgba(139, 92, 246, 0.4);
  font-weight: 700;
}""",
    content,
    flags=re.DOTALL,
)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated styles.css with premium theme!")
