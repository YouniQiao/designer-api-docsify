# X509Cert

提供用于X.509证书操作的API。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cert-interface X509Cert--><!--Device-cert-interface X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## checkValidityWithDate

```TypeScript
checkValidityWithDate(date: string): void
```

表示校验X.509证书有效期。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-checkValidityWithDate(date: string): void--><!--Device-X509Cert-checkValidityWithDate(date: string): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | string | Yes | 表示日期，日期采用 ASN.1 UTCTime 或 GeneralizedTime 格式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19030003 | 证书尚未生效。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |
| 19030004 | 证书过期。 |

## getBasicConstraints

ArkTS-Dyn:
```TypeScript
getBasicConstraints(): number
```

ArkTS-Sta:
```TypeScript
getBasicConstraints(): int
```

表示获取X.509证书基本约束。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getBasicConstraints(): int--><!--Device-X509Cert-getBasicConstraints(): int-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 表示X.509证书基本约束。 |

## getCRLDistributionPoint

```TypeScript
getCRLDistributionPoint(): DataArray
```

获取X.509证书CRL的分发点统一资源标识符。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getCRLDistributionPoint(): DataArray--><!--Device-X509Cert-getCRLDistributionPoint(): DataArray-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) | 表示X.509证书CRL的分发点统一资源标识符。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getCertSerialNumber

```TypeScript
getCertSerialNumber(): bigint
```

表示获取X.509证书序列号。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getCertSerialNumber(): bigint--><!--Device-X509Cert-getCertSerialNumber(): bigint-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| bigint | 表示X.509证书序列号。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

表示获取X.509证书序列化数据。使用Callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getEncoded(callback: AsyncCallback<EncodingBlob>): void--><!--Device-X509Cert-getEncoded(callback: AsyncCallback<EncodingBlob>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EncodingBlob&gt; | Yes | 回调函数。当获取X.509证书序列化数据成功时，err为undefined，data为 获取到的X.509证书序列化数据；否则为错误对象。 |

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

表示获取X.509证书序列化数据。使用Promise方式返回结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getEncoded(): Promise<EncodingBlob>--><!--Device-X509Cert-getEncoded(): Promise<EncodingBlob>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;EncodingBlob&gt; | Promise对象，返回X.509证书序列化数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getExtKeyUsage

```TypeScript
getExtKeyUsage(): DataArray
```

表示获取X.509证书扩展密钥用途。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getExtKeyUsage(): DataArray--><!--Device-X509Cert-getExtKeyUsage(): DataArray-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) | 表示X.509证书扩展密钥用途。 |

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

获取证书扩展对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getExtensionsObject(): CertExtension--><!--Device-X509Cert-getExtensionsObject(): CertExtension-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) | 证书扩展对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getIssuerAltNames

```TypeScript
getIssuerAltNames(): DataArray
```

表示获取X.509证书颁发者可选名称。

> **说明：**
> 
> 获取到的X.509证书颁发者可选名称数据带字符串结束符。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getIssuerAltNames(): DataArray--><!--Device-X509Cert-getIssuerAltNames(): DataArray-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) | 表示X.509证书颁发者可选名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getIssuerName

```TypeScript
getIssuerName(): DataBlob
```

表示获取X.509证书颁发者名称。

> **说明：**
> 
> - 获取的X.509证书颁发者名称末尾包含一个NUL终止符（值为0），请根据业务需求决定是否去除该终止符。
> - 获取的证书颁发者名称为ASCII编码，转换为字符串后，是以斜杠（/）开始，以斜杠（/）分隔相对可分辨名称的可分辨名称字符串。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getIssuerName(): DataBlob--><!--Device-X509Cert-getIssuerName(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示X.509证书颁发者名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getIssuerName

```TypeScript
getIssuerName(encodingType: EncodingType): string
```

表示根据编码类型获取X.509证书颁发者名称。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X509Cert-getIssuerName(encodingType: EncodingType): string--><!--Device-X509Cert-getIssuerName(encodingType: EncodingType): string-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes | 表示编码类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示X.509证书颁发者名称，以逗号（,）分隔。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020003 | 参数检查失败。可能的原因： &lt;br&gt;1. encodingType的值不在EncodingType枚举范围内。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getIssuerX500DistinguishedName

```TypeScript
getIssuerX500DistinguishedName(): X500DistinguishedName
```

获取X.509证书颁发者的X.500可分辨名称。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getIssuerX500DistinguishedName(): X500DistinguishedName--><!--Device-X509Cert-getIssuerX500DistinguishedName(): X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) | X.500可分辨对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getItem

```TypeScript
getItem(itemType: CertItemType): DataBlob
```

表示获取X.509证书对应的字段。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getItem(itemType: CertItemType): DataBlob--><!--Device-X509Cert-getItem(itemType: CertItemType): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [CertItemType](arkts-devicecertificate-cert-certitemtype-e.md) | Yes | 表示需要获取的证书字段。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示X.509证书对应的字段，返回值为DER格式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getKeyUsage

```TypeScript
getKeyUsage(): DataBlob
```

表示获取X.509证书密钥用途。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getKeyUsage(): DataBlob--><!--Device-X509Cert-getKeyUsage(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示X.509证书密钥用途。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getNotAfterTime

```TypeScript
getNotAfterTime(): string
```

表示获取X.509证书过期时间。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getNotAfterTime(): string--><!--Device-X509Cert-getNotAfterTime(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示X.509证书过期时间，日期采用 ASN.1 UTCTime 或 GeneralizedTime 格式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getNotBeforeTime

```TypeScript
getNotBeforeTime(): string
```

表示获取X.509证书生效时间。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getNotBeforeTime(): string--><!--Device-X509Cert-getNotBeforeTime(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示X.509证书生效时间，日期采用 ASN.1 UTCTime 或 GeneralizedTime 格式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getPublicKey

```TypeScript
getPublicKey(): cryptoFramework.PubKey
```

表示获取X.509证书公钥。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getPublicKey(): cryptoFramework.PubKey--><!--Device-X509Cert-getPublicKey(): cryptoFramework.PubKey-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| cryptoFramework.PubKey | 表示X.509证书公钥对象。该对象仅用于**X509Cert**的**verify()**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSerialNumber

```TypeScript
getSerialNumber(): number
```

表示获取X.509证书序列号。

> **说明：**
> 
> 从API version 9开始支持，从API version 10开始废弃，建议使用
> [X509Cert.getCertSerialNumber()](arkts-devicecertificate-cert-x509cert-i.md#getcertserialnumber)替代。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** ohos.security.cert.X509Cert.getCertSerialNumber

<!--Device-X509Cert-getSerialNumber(): number--><!--Device-X509Cert-getSerialNumber(): number-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| number | 表示X.509证书序列号。 |

## getSignature

```TypeScript
getSignature(): DataBlob
```

表示获取X.509证书签名数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getSignature(): DataBlob--><!--Device-X509Cert-getSignature(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示X.509证书签名数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSignatureAlgName

```TypeScript
getSignatureAlgName(): string
```

表示获取X.509证书签名算法名称。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getSignatureAlgName(): string--><!--Device-X509Cert-getSignatureAlgName(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示X.509证书签名算法名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSignatureAlgOid

```TypeScript
getSignatureAlgOid(): string
```

表示获取X.509证书签名算法的对象标识符（OID）。OID由国际标准化组织（ISO）分配。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getSignatureAlgOid(): string--><!--Device-X509Cert-getSignatureAlgOid(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示签名算法OID。当长度超过127字节时会被截断。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSignatureAlgParams

```TypeScript
getSignatureAlgParams(): DataBlob
```

表示获取X.509证书签名算法参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getSignatureAlgParams(): DataBlob--><!--Device-X509Cert-getSignatureAlgParams(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示X.509证书签名算法参数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 801 | 不支持该操作。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSubjectAltNames

```TypeScript
getSubjectAltNames(): DataArray
```

表示获取X.509证书主体可选名称。

> **说明：**
> 
> 获取到的X.509证书主体可选名称数据带字符串结束符。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getSubjectAltNames(): DataArray--><!--Device-X509Cert-getSubjectAltNames(): DataArray-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) | 表示X.509证书主体可选名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSubjectName

```TypeScript
getSubjectName(encodingType?: EncodingType): DataBlob
```

表示获取X.509证书主体名称。

> **说明：**
> 
> - 若不设置encodingType参数，获取的证书主体名称末尾包含一个NUL终止符（值为0），请根据业务需求决定是否去除该终止符。
> - 若不设置encodingType参数，获取的证书主体名称为ASCII编码，转换为字符串后，是以斜杠（/）开始，以斜杠（/）分隔相对可分辨名称的
> 可分辨名称字符串。
> - 建议设置encodingType参数为EncodingType.ENCODING_UTF8，获取的证书主体名称是以逗号（,）分隔相对可分辨名称的可分辨名称字符串。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getSubjectName(encodingType?: EncodingType): DataBlob--><!--Device-X509Cert-getSubjectName(encodingType?: EncodingType): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | No | 表示编码类型。设置该参数时，获取UTF-8格式的主体名称； 不设置时，默认获取ASCII编码格式的主体名称。&lt;br&gt;该参数从API version 12开始可用。<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 表示X.509证书主体名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 参数类型不正确； &lt;br&gt;2. 参数校验失败。<br>**Applicable version:** 12 and later |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getSubjectX500DistinguishedName

```TypeScript
getSubjectX500DistinguishedName(): X500DistinguishedName
```

获取X.509证书主体的X.500可分辨名称。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getSubjectX500DistinguishedName(): X500DistinguishedName--><!--Device-X509Cert-getSubjectX500DistinguishedName(): X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) | X.500可分辨对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## getVersion

ArkTS-Dyn:
```TypeScript
getVersion(): number
```

ArkTS-Sta:
```TypeScript
getVersion(): int
```

表示获取X.509证书版本号。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-getVersion(): int--><!--Device-X509Cert-getVersion(): int-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 表示X.509证书版本号。 |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

获取DER格式数据的哈希值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-hashCode(): Uint8Array--><!--Device-X509Cert-hashCode(): Uint8Array-End-->

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

## match

```TypeScript
match(param: X509CertMatchParameters): boolean
```

判断证书是否与输入参数匹配。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-match(param: X509CertMatchParameters): boolean--><!--Device-X509Cert-match(param: X509CertMatchParameters): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [X509CertMatchParameters](arkts-devicecertificate-cert-x509certmatchparameters-i.md) | Yes | 表示需要匹配的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当参数匹配时，该方法返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
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

<!--Device-X509Cert-toString(): string--><!--Device-X509Cert-toString(): string-End-->

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

## toString

```TypeScript
toString(encodingType: EncodingType): string
```

根据编码类型获取对象的字符串类型数据。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X509Cert-toString(encodingType: EncodingType): string--><!--Device-X509Cert-toString(encodingType: EncodingType): string-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes | 表示编码类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 表示对象的字符串类型数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 19020003 | 参数检查失败。可能的原因： &lt;br&gt;1. encodingType的值不在EncodingType枚举范围内。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void
```

表示对证书验签。使用Callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void--><!--Device-X509Cert-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | Yes | 用于验签的公钥对象。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当验签成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19030001 | 调用三方算法库API出错。 |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey): Promise<void>
```

表示对证书验签。使用Promise方式返回结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509Cert-verify(key: cryptoFramework.PubKey): Promise<void>--><!--Device-X509Cert-verify(key: cryptoFramework.PubKey): Promise<void>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | Yes | 用于验签的公钥对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 19030001 | 调用三方算法库API出错。 |

