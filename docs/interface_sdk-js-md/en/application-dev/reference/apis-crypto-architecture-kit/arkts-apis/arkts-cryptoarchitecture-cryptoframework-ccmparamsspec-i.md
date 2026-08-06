# CcmParamsSpec

Encapsulates the parameters for encryption or decryption using the CCM AEAD mode, which requires an IV, AAD, and an authentication tag. It is a child class of [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and used as a parameter in  
[init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ for symmetric encryption or decryption.

\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_Applies to the CCM mode.
    **NOTE**  
    
    Before passing a value to  
    [init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, specify  
    **algName** for its parent class [ParamsSpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_.

**Inheritance/Implementation:** CcmParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface CcmParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface CcmParamsSpec extends ParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## aad

```TypeScript
aad: DataBlob
```

AAD for encryption and decryption. The AAD value contains 1 to 2,048 bytes.

**Type:** DataBlob

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CcmParamsSpec-aad: DataBlob--><!--Device-CcmParamsSpec-aad: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## authTag

```TypeScript
authTag: DataBlob
```

Authentication tag, which is of 12 bytes.

\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_When CCM mode is used for encryption, you need to extract the last 12 bytes from the  
[DataBlob]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ returned by  
[doFinal()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or  
[doFinalSync()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ and use them as **authTag** in  
**CcmParamsSpec** for  
[init()]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ or  
[initSync()]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ during decryption.

**Type:** DataBlob

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CcmParamsSpec-authTag: DataBlob--><!--Device-CcmParamsSpec-authTag: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## iv

```TypeScript
iv: DataBlob
```

IV for encryption and decryption. Only 7 bytes are supported. If the length of the input **iv** parameter exceeds7 bytes, the excess part will be truncated.

**Type:** DataBlob

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CcmParamsSpec-iv: DataBlob--><!--Device-CcmParamsSpec-iv: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

