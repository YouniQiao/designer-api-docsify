# X509CRLEntry

证书吊销条目。

**起始版本：** 11

<!--Device-cert-interface X509CRLEntry--><!--Device-cert-interface X509CRLEntry-End-->

**系统能力：** SystemCapability.Security.Cert

## getCertIssuer

```TypeScript
getCertIssuer(): DataBlob
```

表示获取被吊销证书的颁发者名称。

> **说明：**
> 
> 获取到的被吊销证书的颁发者名称数据带字符串结束符。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getCertIssuer(): DataBlob--><!--Device-X509CRLEntry-getCertIssuer(): DataBlob-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getCertIssuer

```TypeScript
getCertIssuer(encodingType: EncodingType): string
```

根据编码类型获取被吊销证书的颁发者名称。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getCertIssuer(encodingType: EncodingType): string--><!--Device-X509CRLEntry-getCertIssuer(encodingType: EncodingType): string-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getCertIssuerX500DistinguishedName

```TypeScript
getCertIssuerX500DistinguishedName(): X500DistinguishedName
```

获取被吊销证书的颁发者的X.500可分辨名称对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getCertIssuerX500DistinguishedName(): X500DistinguishedName--><!--Device-X509CRLEntry-getCertIssuerX500DistinguishedName(): X500DistinguishedName-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

表示获取证书吊销条目的序列化数据。使用Callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getEncoded(callback: AsyncCallback<EncodingBlob>): void--><!--Device-X509CRLEntry-getEncoded(callback: AsyncCallback<EncodingBlob>): void-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EncodingBlob&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

表示获取证书吊销条目的序列化数据。使用Promise方式返回结果。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getEncoded(): Promise<EncodingBlob>--><!--Device-X509CRLEntry-getEncoded(): Promise<EncodingBlob>-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Promise&lt;EncodingBlob&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getExtensions

```TypeScript
getExtensions(): DataBlob
```

表示获取DER格式的CRL条目的扩展数据。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getExtensions(): DataBlob--><!--Device-X509CRLEntry-getExtensions(): DataBlob-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getExtensionsObject

```TypeScript
getExtensionsObject(): CertExtension
```

获取CRL条目的扩展对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getExtensionsObject(): CertExtension--><!--Device-X509CRLEntry-getExtensionsObject(): CertExtension-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getRevocationDate

```TypeScript
getRevocationDate(): string
```

表示获取证书被吊销的日期。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getRevocationDate(): string--><!--Device-X509CRLEntry-getRevocationDate(): string-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSerialNumber

```TypeScript
getSerialNumber(): bigint
```

表示获取被吊销的证书的序列号。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-getSerialNumber(): bigint--><!--Device-X509CRLEntry-getSerialNumber(): bigint-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## hasExtensions

```TypeScript
hasExtensions(): boolean
```

表示判断CRL条目是否有扩展。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-hasExtensions(): boolean--><!--Device-X509CRLEntry-hasExtensions(): boolean-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

获取DER格式数据的哈希值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-hashCode(): Uint8Array--><!--Device-X509CRLEntry-hashCode(): Uint8Array-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## toString

```TypeScript
toString(): string
```

获取对象的字符串类型数据。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRLEntry-toString(): string--><!--Device-X509CRLEntry-toString(): string-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
