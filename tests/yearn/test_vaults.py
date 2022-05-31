import pytest
from dotenv import load_dotenv
from .tst_yearn_constants import USDC_VAULT, CRV_VAULT

load_dotenv()


@pytest.mark.parametrize("vault", [USDC_VAULT, CRV_VAULT])
def test_wallets(vault):
    wallets = vault.wallets
    assert len(wallets) > 0


@pytest.mark.parametrize("vault", [USDC_VAULT, CRV_VAULT])
def test_describe(vault):
    info = vault.describe()
    assert len(info.topWallets) == 10
