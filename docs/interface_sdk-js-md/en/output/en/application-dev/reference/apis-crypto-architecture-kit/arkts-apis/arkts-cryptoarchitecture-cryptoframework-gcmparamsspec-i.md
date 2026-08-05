# GcmParamsSpec

Encapsulates the parameters for encryption or decryption using the GCM AEAD mode, which requires an IV, AAD, and an authentication tag. It is a child class of [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and used as a parameter in [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ for symmetric encryption or decryption. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_Applies to the GCM mode. > **NOTE** > > 1. Before passing a value to > [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, specify > **algName** for its parent class [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. > 2. If **aad** is not required or the **aad** length is 0, you can set its **data** attribute to an empty > Uint8Array in the **aad: { data: new Uint8Array() }** format when constructing **GcmParamsSpec**.

**Inheritance/Implementation:** GcmParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface GcmParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface GcmParamsSpec extends ParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## aad

```TypeScript
aad: DataBlob
```

Additional authentication data (AAD), which is of 0 to INT\_MAX bytes.

**Type:** DataBlob

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GcmParamsSpec-aad: DataBlob--><!--Device-GcmParamsSpec-aad: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## authTag

```TypeScript
authTag: DataBlob
```

Authentication tag, which is of 16 bytes. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_When GCM mode is used for encryption, you need to extract the last 16 bytes from the [DataBlob]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ returned by [doFinal()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or [doFinalSync()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ and use them as **authTag** in **GcmParamsSpec** for [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ or [initSync()]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_.

**Type:** DataBlob

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GcmParamsSpec-authTag: DataBlob--><!--Device-GcmParamsSpec-authTag: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## iv

```TypeScript
iv: DataBlob
```

IV, which is of 1 to 128 bytes. A 12-byte IV is commonly used.

**Type:** DataBlob

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GcmParamsSpec-iv: DataBlob--><!--Device-GcmParamsSpec-iv: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

