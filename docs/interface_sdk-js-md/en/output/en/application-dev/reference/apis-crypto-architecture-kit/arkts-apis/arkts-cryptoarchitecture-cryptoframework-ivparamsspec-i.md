# IvParamsSpec

Encapsulates the parameters for encryption or decryption using a block cipher mode that requires an IV. It is a child class of [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and used as a parameter in [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ for symmetric encryption or decryption. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_This is applicable to block cipher modes that require an IV, such as CBC, CTR, OFB, and CFB. > **NOTE** > > Before passing a value to > [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, specify > **algName** for its parent class [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_.

**Inheritance/Implementation:** IvParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface IvParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface IvParamsSpec extends ParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## iv

```TypeScript
iv: DataBlob
```

IV parameter for encryption/decryption. Common lengths are listed below: - In the CBC, CTR, OFB, or CFB mode of AES: The IV length is 16 bytes. - In the CBC, OFB, or CFB mode of 3DES: The IV length is 8 bytes. - In the CBC, CTR, OFB, or CFB mode of SM4\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_10+\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_: The IV length is 16 bytes.

**Type:** DataBlob

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IvParamsSpec-iv: DataBlob--><!--Device-IvParamsSpec-iv: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

