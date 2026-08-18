# @ohos.security.cryptoFramework

The **cryptoFramework** module provides APIs for cryptographic operations, shielding the underlying hardware and algorithm library.

**Since:** 23

**Model restriction:** 
- API version 12 and later: This API can be used in both the stage model and FA model.
- API version 9 to 11: This API can be used only in the stage model.

<!--Device-unnamed-declare namespace cryptoFramework--><!--Device-unnamed-declare namespace cryptoFramework-End-->

**System capability:** SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createAsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createasykeygenerator-f.md#createasykeygenerator) |
| [createAsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md#createasykeygeneratorbyspec) |
| [createCipher](arkts-cryptoarchitecture-cryptoframework-createcipher-f.md#createcipher) |
| [createKdf](arkts-cryptoarchitecture-cryptoframework-createkdf-f.md#createkdf) |
| [createKem](arkts-cryptoarchitecture-cryptoframework-createkem-f.md#createkem) |
| [createKeyAgreement](arkts-cryptoarchitecture-cryptoframework-createkeyagreement-f.md#createkeyagreement) |
| [createMac](arkts-cryptoarchitecture-cryptoframework-createmac-f.md#createmac) |
| [createMac](arkts-cryptoarchitecture-cryptoframework-createmac-f.md#createmac) |
| [createMd](arkts-cryptoarchitecture-cryptoframework-createmd-f.md#createmd) |
| [createRandom](arkts-cryptoarchitecture-cryptoframework-createrandom-f.md#createrandom) |
| [createSign](arkts-cryptoarchitecture-cryptoframework-createsign-f.md#createsign) |
| [createSymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createsymkeygenerator-f.md#createsymkeygenerator) |
| [createVerify](arkts-cryptoarchitecture-cryptoframework-createverify-f.md#createverify) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DHKeyUtil](arkts-cryptoarchitecture-cryptoframework-dhkeyutil-c.md) |
| [ECCKeyUtil](arkts-cryptoarchitecture-cryptoframework-ecckeyutil-c.md) |
| [SM2CryptoUtil](arkts-cryptoarchitecture-cryptoframework-sm2cryptoutil-c.md) |
| [SignatureUtils](arkts-cryptoarchitecture-cryptoframework-signatureutils-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AeadParamsSpec](arkts-cryptoarchitecture-cryptoframework-aeadparamsspec-i.md) |
| [AsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-asykeygenerator-i.md) |
| [AsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md) |
| [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md) |
| [CcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-ccmparamsspec-i.md) |
| [Cipher](arkts-cryptoarchitecture-cryptoframework-cipher-i.md) |
| [CmacSpec](arkts-cryptoarchitecture-cryptoframework-cmacspec-i.md) |
| [DHCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dhcommonparamsspec-i.md) |
| [DHKeyPairSpec](arkts-cryptoarchitecture-cryptoframework-dhkeypairspec-i.md) |
| [DHPriKeySpec](arkts-cryptoarchitecture-cryptoframework-dhprikeyspec-i.md) |
| [DHPubKeySpec](arkts-cryptoarchitecture-cryptoframework-dhpubkeyspec-i.md) |
| [DSACommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dsacommonparamsspec-i.md) |
| [DSAKeyPairSpec](arkts-cryptoarchitecture-cryptoframework-dsakeypairspec-i.md) |
| [DSAPubKeySpec](arkts-cryptoarchitecture-cryptoframework-dsapubkeyspec-i.md) |
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |
| [ECCCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) |
| [ECCKeyPairSpec](arkts-cryptoarchitecture-cryptoframework-ecckeypairspec-i.md) |
| [ECCPriKeySpec](arkts-cryptoarchitecture-cryptoframework-eccprikeyspec-i.md) |
| [ECCPubKeySpec](arkts-cryptoarchitecture-cryptoframework-eccpubkeyspec-i.md) |
| [ECField](arkts-cryptoarchitecture-cryptoframework-ecfield-i.md) |
| [ECFieldFp](arkts-cryptoarchitecture-cryptoframework-ecfieldfp-i.md) |
| [ED25519KeyPairSpec](arkts-cryptoarchitecture-cryptoframework-ed25519keypairspec-i.md) |
| [ED25519PriKeySpec](arkts-cryptoarchitecture-cryptoframework-ed25519prikeyspec-i.md) |
| [ED25519PubKeySpec](arkts-cryptoarchitecture-cryptoframework-ed25519pubkeyspec-i.md) |
| [EccSignatureSpec](arkts-cryptoarchitecture-cryptoframework-eccsignaturespec-i.md) |
| [GcmParamsSpec](arkts-cryptoarchitecture-cryptoframework-gcmparamsspec-i.md) |
| [HKDFSpec](arkts-cryptoarchitecture-cryptoframework-hkdfspec-i.md) | Defines the child class of [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md#kdfspec). It is a parameter for HKDF key derivation. > **NOTE：**> > **key** is the original key material entered by the user. An empty string can be passed in for **info** and > **salt** based on the mode. > > For example, if the mode is **EXTRACT_AND_EXPAND**, all parameter values must be passed in. If the mode is > **EXTRACT_ONLY**, **info** can be empty. When **HKDFSpec** is constructed, pass in **null** to **info**. > > The default mode is **EXTRACT_AND_EXPAND**. The value **HKDF\|SHA256\|EXTRACT_AND_EXPAND** is equivalent to > **HKDF\|
| [HmacSpec](arkts-cryptoarchitecture-cryptoframework-hmacspec-i.md) |
| [IvParamsSpec](arkts-cryptoarchitecture-cryptoframework-ivparamsspec-i.md) |
| [Kdf](arkts-cryptoarchitecture-cryptoframework-kdf-i.md) |
| [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md) |
| [Kem](arkts-cryptoarchitecture-cryptoframework-kem-i.md) |
| [KemEncapResult](arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md) |
| [Key](arkts-cryptoarchitecture-cryptoframework-key-i.md) |
| [KeyAgreement](arkts-cryptoarchitecture-cryptoframework-keyagreement-i.md) |
| [KeyEncodingConfig](arkts-cryptoarchitecture-cryptoframework-keyencodingconfig-i.md) |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |
| [Mac](arkts-cryptoarchitecture-cryptoframework-mac-i.md) |
| [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md) |
| [Md](arkts-cryptoarchitecture-cryptoframework-md-i.md) |
| [PBKDF2Spec](arkts-cryptoarchitecture-cryptoframework-pbkdf2spec-i.md) |
| [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md) |
| [Point](arkts-cryptoarchitecture-cryptoframework-point-i.md) |
| [Poly1305ParamsSpec](arkts-cryptoarchitecture-cryptoframework-poly1305paramsspec-i.md) |
| [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) |
| [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) |
| [RSACommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-rsacommonparamsspec-i.md) |
| [RSAKeyPairSpec](arkts-cryptoarchitecture-cryptoframework-rsakeypairspec-i.md) |
| [RSAPubKeySpec](arkts-cryptoarchitecture-cryptoframework-rsapubkeyspec-i.md) |
| [Random](arkts-cryptoarchitecture-cryptoframework-random-i.md) |
| [SM2CipherTextSpec](arkts-cryptoarchitecture-cryptoframework-sm2ciphertextspec-i.md) |
| [ScryptSpec](arkts-cryptoarchitecture-cryptoframework-scryptspec-i.md) |
| [Sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md) |
| [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) |
| [SymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-symkeygenerator-i.md) |
| [Verify](arkts-cryptoarchitecture-cryptoframework-verify-i.md) |
| [X25519KeyPairSpec](arkts-cryptoarchitecture-cryptoframework-x25519keypairspec-i.md) |
| [X25519PriKeySpec](arkts-cryptoarchitecture-cryptoframework-x25519prikeyspec-i.md) |
| [X25519PubKeySpec](arkts-cryptoarchitecture-cryptoframework-x25519pubkeyspec-i.md) |
| [X963KdfSpec](arkts-cryptoarchitecture-cryptoframework-x963kdfspec-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AsyKeyDataItem](arkts-cryptoarchitecture-cryptoframework-asykeydataitem-e.md) |
| [AsyKeySpecItem](arkts-cryptoarchitecture-cryptoframework-asykeyspecitem-e.md) |
| [AsyKeySpecType](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md) |
| [CipherSpecItem](arkts-cryptoarchitecture-cryptoframework-cipherspecitem-e.md) |
| [CryptoMode](arkts-cryptoarchitecture-cryptoframework-cryptomode-e.md) |
| [KemAlgNameId](arkts-cryptoarchitecture-cryptoframework-kemalgnameid-e.md) |
| [Result](arkts-cryptoarchitecture-cryptoframework-result-e.md) |
| [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) |
