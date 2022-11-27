def test_vault_user(host):
    assert host.group("vault").exists
    assert host.user("vault").exists
    assert "vault" in host.user("vault").groups


def test_vault_config_dir(host):
    """
    Ensure that the vault configuration directory is present and properly configured
    """
    vault_config_dir = host.file("/etc/vault.d")
    assert vault_config_dir.exists
    assert vault_config_dir.is_directory
    assert vault_config_dir.user == "vault"
    assert vault_config_dir.group == "vault"
    assert vault_config_dir.mode == "0o644"
