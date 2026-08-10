# createVerify

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createVerify

```TypeScript
function createVerify(algName: string): Verify
```

创建验签实例。

&lt;br&gt;支持的规格详见[签名验签规格](../../../security/CryptoArchitectureKit/crypto-sign-sig-verify-overview.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createVerify(algName: string): Verify--><!--Device-cryptoFramework-function createVerify(algName: string): Verify-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algName | string | Yes | 指定签名验证算法。当前支持RSA、ECC、DSA、SM2&lt;sup&gt;10+&lt;/sup&gt;，Ed25519&lt;sup&gt;11+&lt;/sup&gt;和 ML-DSA&lt;sup&gt;26.0.0+&lt;/sup&gt;。 &lt;br&gt;使用RSA PKCS1模式时需设置摘要；使用RSA PSS模式时需设置摘要和掩码摘要。使用RSA算法验签时，设置recover参数可支持验签恢复。 &lt;br&gt;支持的规格详见 [签名验签规格](../../../security/CryptoArchitectureKit/crypto-sign-sig-verify-overview.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Verify](arkts-cryptoarchitecture-cryptoframework-verify-i.md) | 返回对应算法的Verify实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 801 | 该操作不支持。 |
| 17620001 | 内存操作失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let verifier1 = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');

let verifier2 = cryptoFramework.createVerify('RSA1024|PSS|SHA256|MGF1_SHA256');

let verifier3 = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256|Recover');
```

