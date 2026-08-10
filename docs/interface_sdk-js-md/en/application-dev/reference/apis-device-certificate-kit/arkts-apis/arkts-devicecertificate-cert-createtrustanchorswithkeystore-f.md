# createTrustAnchorsWithKeyStore

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createTrustAnchorsWithKeyStore

```TypeScript
function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>
```

表示从P12中读取ca证书来构造[TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md)对象数组。使用Promise方式返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cert-function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>--><!--Device-cert-function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keystore | Uint8Array | Yes | DER格式的P12文件原始数据。 |
| pwd | string | Yes | 密码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;X509TrustAnchor&gt;&gt; | Promise对象，返回X509TrustAnchor对象数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19030002 | 证书签名验证错误。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19030003 | 证书尚未生效。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |
| 19030006 | 证书的密钥用途不含证书签名。 |
| 19030007 | 证书的密钥用途不含数字签名。 |
| 19030004 | 证书过期。 |
| 19030005 | 无法获取证书的颁发者。 |

