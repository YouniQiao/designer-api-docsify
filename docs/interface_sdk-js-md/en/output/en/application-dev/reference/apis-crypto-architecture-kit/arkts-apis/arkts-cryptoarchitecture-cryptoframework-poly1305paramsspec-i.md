# Poly1305ParamsSpec

Encapsulates the parameters for encryption or decryption using the ChaCha20-Poly1305 AEAD mode, which requires a nonce, AAD, and an authentication tag. It is a child class of [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and used as a parameter in [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ for symmetric encryption or decryption. \_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_Applicable to \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. > **NOTE** > > Before passing a value to > [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, specify > **algName** for its parent class [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_. > > When the Poly1305 mode is used for encryption, you need to extract the last 16 bytes from the > [DataBlob]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ returned by > [doFinal()]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ or > [doFinalSync()]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ and use them as **authTag** in > [Poly1305ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ for > [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ or > [initSync()]\_\_\_JSDOC\_LINK\_DESC\_USD\_10\_\_\_ during decryption.

**Inheritance/Implementation:** Poly1305ParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface Poly1305ParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface Poly1305ParamsSpec extends ParamsSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## aad

```TypeScript
aad: DataBlob
```

Additional authenticated data.

**Type:** DataBlob

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Poly1305ParamsSpec-aad: DataBlob--><!--Device-Poly1305ParamsSpec-aad: DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## authTag

```TypeScript
authTag: DataBlob
```

Authentication tag, which is of 16 bytes.

**Type:** DataBlob

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Poly1305ParamsSpec-authTag: DataBlob--><!--Device-Poly1305ParamsSpec-authTag: DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## iv

```TypeScript
iv: DataBlob
```

Nonce (passed as the **iv** field), which is of 12 bytes.

**Type:** DataBlob

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Poly1305ParamsSpec-iv: DataBlob--><!--Device-Poly1305ParamsSpec-iv: DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

