# CcmParamsSpec

加解密参数[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)的子类，封装使用CCM AEAD模式进行加密或解密的参数，需要IV、AAD和认证标签。它是[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)的子类，用于在对称加解密时作为  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法的参数。

&lt;br&gt;适用于CCM模式。

> **说明：**
> 
> 传入[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法前需
> 要指定其algName属性（来源于父类[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)）。

**Inheritance/Implementation:** CcmParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface CcmParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface CcmParamsSpec extends ParamsSpec-End-->

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

指明加解密参数aad。aad最小长度为1字节，最大为2048字节。

**Type:** [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

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

指明加解密参数authTag，长度为12字节。

&lt;br&gt;加密时，需从  
[doFinal()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#dofinal)或  
[doFinalSync()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#dofinalsync)输出的  
[DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)中提取末尾12字节，作为解密时  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)或  
[initSync()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#initsync)方法中CcmParamsSpec的authTag。

**Type:** [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

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

指明加解密参数iv，仅支持7字节。若传入iv长度超过7字节，超出范围将被截断。

**Type:** [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CcmParamsSpec-iv: DataBlob--><!--Device-CcmParamsSpec-iv: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

