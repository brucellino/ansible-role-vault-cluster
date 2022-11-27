def test_vault_user(host):
  assert host.group("vault").exists
  assert host.user("vault").exists
  assert "vault" in host.user("vault").groups
