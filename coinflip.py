import hashlib
import random

from solana.account import Account
from solana.program import Program
from solana.publickey import PublicKey


class CoinFlip(Program):
    # initialize the contract with the player's account and the contract owner's public key
    def __init__(self, a: Account, contract_owner: PublicKey):
        self.account = a
        self.player = a.public_key
        self.contract_owner = contract_owner
        self.balance = 0
        self.bet_amount = 0
        self.result = None

    # method to place a bet on the coin flip
    def place_bet(self, account: Account, amount: int):
        assert account.lamports >= amount, 'You must bet more than 0 Lamports.'
        assert account.owner == self.player, 'Only the player can place a bet.'
        self.bet_amount = amount

    # method to flip the coin and determine the result
    def flip(self, account: Account):
        assert account.owner == self.player, 'Only the player can flip the coin.'
        hasher = hashlib.sha256()
        hasher.update(str(random.getrandbits(256)).encode('utf-8'))
        self.result = int(hasher.hexdigest(), 16) % 2 == 0
        if not self.result:
             self.player.transfer(self.contract_owner, amount)

    # method to withdraw the bet amount if the player wins
    def withdraw(self, account: Account):
        assert account.owner == self.player, 'Only the player can withdraw the bet amount.'
        assert self.result, 'You can only withdraw the bet amount if you won.'
        self.balance = self.bet_amount * 2
        account.transfer(self.player, self.balance)


# test the contract
if __name__ == '__main__':
    # create a new account for the player
    player = PublicKey.from_hex('1111111111111111')
    account = Account(100000, 0)
    contract = CoinFlip(account)

    # place a bet on the coin flip
    contract.place_bet(1000)
    assert contract.bet_amount == 1000

    # flip the coin and determine the result
    contract.flip(account)
    assert contract.result is not None

    # withdraw the bet amount if the player wins
    contract.withdraw(account)
    assert contract.account.lamports == 99
