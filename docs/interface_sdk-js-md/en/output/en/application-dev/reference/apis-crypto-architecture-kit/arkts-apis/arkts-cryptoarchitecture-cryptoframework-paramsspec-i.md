# ParamsSpec

Encapsulates the parameters used for encryption or decryption. You need to construct its child class object and pass it to [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ for symmetric encryption or decryption. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_It applies to the symmetric block cipher modes that require parameters such as the initialization vector (IV). If the IV is not required (for example, the ECB mode), pass in **null** to [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. > **NOTE** > > An initialization vector (IV) is a byte sequence used to introduce randomness or uniqueness in symmetric > encryption modes (such as CBC, CTR, OFB, CFB, GCM, CCM, and ChaCha20-Poly1305). It ensures that different > ciphertexts are generated for the same plaintext under the same key. > **NOTE** > > The **params** parameter in > [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ is of the > **ParamsSpec** type (parent class). However, a child class object (such as > [IvParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_) needs to be passed in. When constructing the child class > object, you must set **algName** for its parent class **ParamsSpec** to specify the child class object to be > passed to **init()**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface ParamsSpec--><!--Device-cryptoFramework-interface ParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## algName

```TypeScript
algName: string
```

Algorithm for symmetric encryption or decryption. The value can be: - **IvParamsSpec**: applicable to the CBC, CTR, OFB, and CFB modes. - **GcmParamsSpec**: applicable to the GCM mode. - **CcmParamsSpec**: applicable to the CCM mode. - **AeadParamsSpec**: applicable to the AES-GCM, AES-CCM, SM4-GCM and ChaCha20-Poly1305 algorithm.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ParamsSpec-algName: string--><!--Device-ParamsSpec-algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

