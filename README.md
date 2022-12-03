# solana-coinflip
 Coinflip game for the Solana blockchain using Python

This code defines a `CoinFlip Contract` in `Python` that allows a player to `place a bet`, `flip a coin`, and `withdraw their bet amount if they lose`.
The contract is implemented using the `Program` class from the `solana` library, which provides the necessary functionality to create and execute `smart contracts` on the Solana blockchain.

The `CoinFlip` class has several methods that allow a player to interact with the contract. The `__init__` method is the constructor for the class, and it initializes the contract with the player's `Account` object and sets the initial values for the `bet_amount` and `result` attributes.

The `place_bet` method allows the player to place a bet by specifying the amount of lamports (the Solana blockchain's native token) to bet. This method checks that the player has enough balance to make the bet and that they are the owner of the contract's `Account` object. If these conditions are met, it updates the `bet_amount` attribute with the specified amount.

The `flip` method simulates the flipping of a coin by generating a random number and checking if it is even or odd. It updates the result attribute with the result of the flip.

The `withdraw` method allows the player to withdraw their bet amount if they lost the coin flip. It checks that the player is the owner of the contract's `Account` object and that the result of the coin flip is not `None`, indicating that the flip has been performed. If these conditions are met, it adds the bet amount to the player's `balance`.

# testing

The code also has a test block that shows an example of how to use the `CoinFlip` contract. It creates a player `PublicKey` and an `Account` object with an initial balance of 100,000 lamports, and then creates an instance of the CoinFlip contract using the `Account` object.

Next, it uses the `place_bet` method to place a bet of 1,000 lamports, checks that the bet_amount attribute has been updated correctly, and then uses the flip method to perform the coin flip and check that the result attribute has been set.

Finally, it uses the `withdraw` method to withdraw the bet amount if the player lost the coin flip, and checks that the player's balance has been updated correctly.