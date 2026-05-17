print("=== Social Engineering Awareness Tool ===")

print("\nCommon Social Engineering Attacks:")
attacks = [
    "Phishing Emails",
    "Fake Login Pages",
    "Phone Scams",
    "USB Drops",
    "Impersonation",
    "Social Media Scams"
]

for i, attack in enumerate(attacks, start=1):
    print(f"{i}. {attack}")

print("\nSafety Tips:")
tips = [
    "Never share passwords",
    "Verify suspicious emails",
    "Use two-factor authentication",
    "Do not click unknown links",
    "Check website URLs carefully"
]

for i, tip in enumerate(tips, start=1):
    print(f"{i}. {tip}")

print("\nThis project is for cybersecurity awareness and education only.")
