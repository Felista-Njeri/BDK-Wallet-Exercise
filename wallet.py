import bdkpython as bdk

print("Generating mnemonic seed...")
mnemonic = bdk.Mnemonic(bdk.WordCount.WORDS12)
print(f"Mnemonic: {mnemonic}")

descriptor = bdk.Descriptor(f"wpkh({mnemonic.to_seed_normalized('')[0:64]}/84'/1'/0'/0/*)", bdk.Network.TESTNET)
change_descriptor = bdk.Descriptor(f"wpkh({mnemonic.to_seed_normalized('')[0:64]}/84'/1'/0'/1/*)", bdk.Network.TESTNET)
wallet = bdk.Wallet(descriptor, change_descriptor, bdk.Network.TESTNET, bdk.MemoryDatabase())

print("\nGenerated Addresses:")
for i in range(3):
    address = wallet.get_address(bdk.AddressIndex.NEW).address
    print(f"Address {i+1}: {address}")