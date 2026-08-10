# CipherSpecItem

表示加解密参数的枚举。这些参数支持通过[setCipherSpec](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#setcipherspec)接口设置，通过  
[getCipherSpec](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#getcipherspec)接口获取。

&lt;br&gt;当前只支持RSA算法和SM2算法。详细规格请参考  
[加解密规格](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-enum CipherSpecItem--><!--Device-cryptoFramework-enum CipherSpecItem-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## OAEP_MD_NAME_STR

```TypeScript
OAEP_MD_NAME_STR = 100
```

表示RSA算法中，使用PKCS1_OAEP模式时，消息摘要功能的算法名。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CipherSpecItem-OAEP_MD_NAME_STR = 100--><!--Device-CipherSpecItem-OAEP_MD_NAME_STR = 100-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## OAEP_MGF_NAME_STR

```TypeScript
OAEP_MGF_NAME_STR = 101
```

表示RSA算法中，使用PKCS1_OAEP模式时，掩码生成算法（目前仅支持MGF1）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CipherSpecItem-OAEP_MGF_NAME_STR = 101--><!--Device-CipherSpecItem-OAEP_MGF_NAME_STR = 101-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## OAEP_MGF1_MD_STR

```TypeScript
OAEP_MGF1_MD_STR = 102
```

表示RSA算法中，使用PKCS1_OAEP模式时，MGF1掩码生成功能的消息摘要算法。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CipherSpecItem-OAEP_MGF1_MD_STR = 102--><!--Device-CipherSpecItem-OAEP_MGF1_MD_STR = 102-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## OAEP_MGF1_PSRC_UINT8ARR

```TypeScript
OAEP_MGF1_PSRC_UINT8ARR = 103
```

表示RSA算法中，使用PKCS1_OAEP模式时，pSource的字节流。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CipherSpecItem-OAEP_MGF1_PSRC_UINT8ARR = 103--><!--Device-CipherSpecItem-OAEP_MGF1_PSRC_UINT8ARR = 103-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## SM2_MD_NAME_STR

```TypeScript
SM2_MD_NAME_STR = 104
```

表示SM2算法中，使用的摘要算法名。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CipherSpecItem-SM2_MD_NAME_STR = 104--><!--Device-CipherSpecItem-SM2_MD_NAME_STR = 104-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 11: SystemCapability.Security.CryptoFramework

