# IvParamsSpec

加解密参数[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)的子类，用于在对称加解密时作为  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法的参数。

&lt;br&gt;适用于CBC、CTR、OFB、CFB这些需要iv作为参数的加解密模式。

> **说明：**
> 
> 传入[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法前需要
> 指定其algName属性（来源于父类[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)）。

**Inheritance/Implementation:** IvParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface IvParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface IvParamsSpec extends ParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## iv

```TypeScript
iv: DataBlob
```

加解密参数iv。常见长度如下：

- AES的CBC|CTR|OFB|CFB模式：iv长度为16字节。  
- 3DES的CBC|OFB|CFB模式：iv长度为8字节。  
- SM4&lt;sup&gt;10+&lt;/sup&gt;的CBC|CTR|OFB|CFB模式：iv长度为16字节。

**Type:** [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IvParamsSpec-iv: DataBlob--><!--Device-IvParamsSpec-iv: DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

