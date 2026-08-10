# createSign

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createSign

```TypeScript
function createSign(algName: string): Sign
```

创建签名实例。

&lt;br&gt;支持的规格详见[签名验签规格](../../../security/CryptoArchitectureKit/crypto-sign-sig-verify-overview.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createSign(algName: string): Sign--><!--Device-cryptoFramework-function createSign(algName: string): Sign-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algName | string | Yes | 指定签名算法。当前支持RSA、ECC、DSA、SM2&lt;sup&gt;10+&lt;/sup&gt;，Ed25519&lt;sup&gt;11+&lt;/sup&gt;和 ML-DSA&lt;sup&gt;26.0.0+&lt;/sup&gt;。 &lt;br&gt;使用RSA PKCS1模式时需设置摘要；使用RSA PSS模式时需设置摘要和掩码摘要。签名时，通过设置OnlySign参数可传入数据摘要仅作签名。 &lt;br&gt;支持的规格详见 [签名验签规格](../../../security/CryptoArchitectureKit/crypto-sign-sig-verify-overview.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md) | 返回对应算法的Sign实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 801 | 该操作不支持。 |
| 17620001 | 内存操作失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let signer1 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');

let signer2 = cryptoFramework.createSign('RSA1024|PSS|SHA256|MGF1_SHA256');

let signer3 = cryptoFramework.createSign('ECC224|SHA256');

let signer4 = cryptoFramework.createSign('DSA2048|SHA256');

let signer5 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256|OnlySign');
```

