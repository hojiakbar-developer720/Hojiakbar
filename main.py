from secure_user import SecureUser

print("\n===== DEMO START =====\n")

# Create user
user = SecureUser("hoji", "test@example.com", "998901234567")

# Valid usage
print("Status:", user.identity_status())
user._identity.request_verification()
user._identity.verify()
print("Status after verification:", user.identity_status())

# Grant normal permission
user.grant_permission("VIEW_BALANCE")

# ------------------------
# ILLEGAL ACCESS ATTEMPTS
# ------------------------

# user._identity.__phone_number     # ❌ ERROR — private attribute
# user._SecureUser__audit_log        # ❌ ERROR — private

# ------------------------
# ILLEGAL STATE TRANSITIONS
# ------------------------

try:
    user._identity.verify()        # ❌ Cannot verify again
except Exception as e:
    print("Error:", e)

# ------------------------
# RESTRICTED PERMISSIONS
# ------------------------
user2 = SecureUser("ali", "ali@example.com", "998909998877")

try:
    user2.grant_permission("TRANSFER")      # ❌ Unverified user
except Exception as e:
    print("Rejected (expected):", e)

# Final state output
print("\nUser 1 Audit Log:")
for log in user.get_audit_log():
    print(" -", log)

print("\nPermissions:", user._SecureUser__access.get_permissions())

print("\n===== DEMO END =====\n")
