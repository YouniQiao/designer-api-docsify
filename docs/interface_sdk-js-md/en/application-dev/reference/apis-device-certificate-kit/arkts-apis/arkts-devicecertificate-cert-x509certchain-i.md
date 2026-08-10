# X509CertChain

X.509证书链对象。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface X509CertChain--><!--Device-cert-interface X509CertChain-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## getCertList

```TypeScript
getCertList(): Array<X509Cert>
```

获取X.509证书列表。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertChain-getCertList(): Array<X509Cert>--><!--Device-X509CertChain-getCertList(): Array<X509Cert>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;X509Cert&gt; | X.509证书数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

获取DER格式数据的哈希值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertChain-hashCode(): Uint8Array--><!--Device-X509CertChain-hashCode(): Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | DER格式数据的哈希值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## toString

```TypeScript
toString(): string
```

获取对象的字符串类型数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertChain-toString(): string--><!--Device-X509CertChain-toString(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | 对象的字符串类型数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## validate

```TypeScript
validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>
```

校验证书链。使用Promise方式返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertChain-validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>--><!--Device-X509CertChain-validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [CertChainValidationParameters](arkts-devicecertificate-cert-certchainvalidationparameters-i.md) | Yes | 表示校验X.509证书链的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CertChainValidationResult&gt; | Promise对象，返回证书链校验结果。 |

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

## validate

```TypeScript
validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void
```

使用校验参数校验证书链。使用Callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CertChain-validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void--><!--Device-X509CertChain-validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [CertChainValidationParameters](arkts-devicecertificate-cert-certchainvalidationparameters-i.md) | Yes | 表示校验X.509证书链的参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CertChainValidationResult&gt; | Yes | 回调函数。当校验证书链成功时，err为undefined， data为获取到的证书链校验结果；否则为错误对象。 |

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

