# X509CRLEntry

证书吊销条目。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface X509CRLEntry--><!--Device-cert-interface X509CRLEntry-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## getCertIssuer

```TypeScript
getCertIssuer(): DataBlob
```

表示获取被吊销证书的颁发者名称。

> **说明：**
> 
> 获取到的被吊销证书的颁发者名称数据带字符串结束符。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getCertIssuer(): DataBlob--><!--Device-X509CRLEntry-getCertIssuer(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示被吊销证书的颁发者名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 801 | 不支持该操作。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getCertIssuer

```TypeScript
getCertIssuer(encodingType: EncodingType): string
```

根据编码类型获取被吊销证书的颁发者名称。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X509CRLEntry-getCertIssuer(encodingType: EncodingType): string--><!--Device-X509CRLEntry-getCertIssuer(encodingType: EncodingType): string-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes | 表示编码类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示被吊销证书的颁发者名称，使用逗号分隔相对可分辨名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 801 | 不支持该操作。 |
| 19020003 | 参数检查失败。可能的原因： &lt;br&gt;1. encodingType的值不在EncodingType枚举范围内。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getCertIssuerX500DistinguishedName

```TypeScript
getCertIssuerX500DistinguishedName(): X500DistinguishedName
```

获取被吊销证书的颁发者的X.500可分辨名称对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getCertIssuerX500DistinguishedName(): X500DistinguishedName--><!--Device-X509CRLEntry-getCertIssuerX500DistinguishedName(): X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) | X.500可分辨名称对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

表示获取证书吊销条目的序列化数据。使用Callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getEncoded(callback: AsyncCallback<EncodingBlob>): void--><!--Device-X509CRLEntry-getEncoded(callback: AsyncCallback<EncodingBlob>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EncodingBlob&gt; | Yes | 回调函数。当获取证书吊销条目序列化数据成功时，err为undefined， data为获取到的证书吊销条目序列化数据；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

表示获取证书吊销条目的序列化数据。使用Promise方式返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getEncoded(): Promise<EncodingBlob>--><!--Device-X509CRLEntry-getEncoded(): Promise<EncodingBlob>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;EncodingBlob&gt; | Promise对象，返回证书吊销条目的序列化数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getExtensions

```TypeScript
getExtensions(): DataBlob
```

表示获取DER格式的CRL条目的扩展数据。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getExtensions(): DataBlob--><!--Device-X509CRLEntry-getExtensions(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示CRL条目的扩展数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getExtensionsObject

```TypeScript
getExtensionsObject(): CertExtension
```

获取CRL条目的扩展对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getExtensionsObject(): CertExtension--><!--Device-X509CRLEntry-getExtensionsObject(): CertExtension-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) | CRL条目的扩展对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getRevocationDate

```TypeScript
getRevocationDate(): string
```

表示获取证书被吊销的日期。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getRevocationDate(): string--><!--Device-X509CRLEntry-getRevocationDate(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示证书被吊销的日期。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSerialNumber

```TypeScript
getSerialNumber(): bigint
```

表示获取被吊销的证书的序列号。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getSerialNumber(): bigint--><!--Device-X509CRLEntry-getSerialNumber(): bigint-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| bigint | 表示证书吊销条目的序列号。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## hasExtensions

```TypeScript
hasExtensions(): boolean
```

表示判断CRL条目是否有扩展。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-hasExtensions(): boolean--><!--Device-X509CRLEntry-hasExtensions(): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true则表示CRL条目有扩展，返回false则表示无扩展。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
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

<!--Device-X509CRLEntry-hashCode(): Uint8Array--><!--Device-X509CRLEntry-hashCode(): Uint8Array-End-->

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

<!--Device-X509CRLEntry-toString(): string--><!--Device-X509CRLEntry-toString(): string-End-->

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

