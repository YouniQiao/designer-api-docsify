# AeadParamsSpec

用于AEAD（带附加数据的认证加密）对称加解密的  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法参数，继承自  
[ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)。

&lt;br&gt;适用于[AES算法](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md#aes)的CCM和GCM分组模式。&lt;br&gt;适用于[SM4算法](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md#sm4)的GCM分组模式。&lt;br&gt;适用于  
[ChaCha20-Poly1305算法](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md#chacha20)分组模式。

> **说明：**
> 
> 在AES-CCM模式下使用AeadParamsSpec加密时：
> - 如果加密时指定了tag长度，解密时也必须传入相同的长度。
> 
> - CCM模式下[update](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#update)与[doFinal](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#dofinal)只能调用其
> 中一个进行加密或者解密，且每个方法只能调用一次。

**Inheritance/Implementation:** AeadParamsSpec extends [ParamsSpec](arkts-cryptoarchitecture-cryptoframework-paramsspec-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cryptoFramework-interface AeadParamsSpec extends ParamsSpec--><!--Device-cryptoFramework-interface AeadParamsSpec extends ParamsSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## authenticatedData

```TypeScript
authenticatedData?: Uint8Array
```

指定可选的附加认证数据。

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AeadParamsSpec-authenticatedData?: Uint8Array--><!--Device-AeadParamsSpec-authenticatedData?: Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## nonce

```TypeScript
nonce: Uint8Array
```

指明加解密参数nonce。

> **说明：**
> - 对于AES-CCM，nonce长度的取值范围为7~13字节。
> - 对于AES-GCM，nonce长度范围为1~128字节，推荐使用12字节。
> - 对于SM4-GCM，nonce长度范围为1~128字节，推荐使用12字节。
> - 对于ChaCha20-Poly1305，nonce长度必须为12字节。

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AeadParamsSpec-nonce: Uint8Array--><!--Device-AeadParamsSpec-nonce: Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## tagLen

```TypeScript
tagLen?: int
```

认证标签长度，单位为字节。

&lt;br&gt;加密时，标签将被添加到密文末尾。&lt;br&gt;解密时，标签应位于密文末尾。&lt;br&gt;取值应为整数。

> **说明：**
> - 对于AES-CCM，默认值为12。支持的取值为4、6、8、10、12、14和16。
> - 对于AES-GCM，默认值为16。支持的取值为4、8、12、13、14、15和16。
> - 对于SM4-GCM，默认值为16。支持的取值为4、8、12、13、14、15和16。
> - 对于ChaCha20-Poly1305，默认值为16。支持的取值为16。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AeadParamsSpec-tagLen?: int--><!--Device-AeadParamsSpec-tagLen?: int-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

