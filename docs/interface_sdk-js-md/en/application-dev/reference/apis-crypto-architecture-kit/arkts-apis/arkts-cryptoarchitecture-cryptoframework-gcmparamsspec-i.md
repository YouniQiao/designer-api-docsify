# GcmParamsSpec

加解密参数[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)的子类，封装使用GCM AEAD模式进行加密或解密的参数，需要IV、AAD和认证标签。它是[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)的子类，用于在对称加解密时作为  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法的参数。

&lt;br&gt;适用于GCM模式。

> **说明：**
> 
> 1. 传入[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法前需
> 要指定其algName属性（来源于父类[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)）。
> 2. 如果不需要aad或者aad长度为0，构造GcmParamsSpec时可以将aad的data属性设置为空的Uint8Array，
> 即aad: { data: new Uint8Array() }。

**Inheritance/Implementation:** GcmParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface GcmParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface GcmParamsSpec extends ParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## aad

```TypeScript
aad: DataBlob
```

指明加解密参数aad，长度为0~INT_MAX字节。

**Type:** [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

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

指明加解密参数authTag，长度为16字节。

&lt;br&gt;采用GCM模式加密时，需从  
[doFinal()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#dofinal)或  
[doFinalSync()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#dofinalsync)输出的  
[DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)中提取末尾16字节，作为  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)或  
[initSync()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#initsync)方法中GcmParamsSpec的authTag。

**Type:** [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

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

指明加解密参数iv，长度为1~128字节，常用为12字节。

**Type:** [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GcmParamsSpec-iv: DataBlob--><!--Device-GcmParamsSpec-iv: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

