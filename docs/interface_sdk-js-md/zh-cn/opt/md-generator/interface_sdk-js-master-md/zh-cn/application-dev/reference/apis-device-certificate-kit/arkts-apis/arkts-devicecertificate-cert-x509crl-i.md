# X509CRL

提供用于X.509证书吊销列表操作的API。

**起始版本：** 23

**废弃版本：** -1

<!--Device-cert-interface X509CRL--><!--Device-cert-interface X509CRL-End-->

**系统能力：** SystemCapability.Security.Cert

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

表示获取X.509证书吊销列表的序列化数据。使用Callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getEncoded(callback: AsyncCallback<EncodingBlob>): void--><!--Device-X509CRL-getEncoded(callback: AsyncCallback<EncodingBlob>): void-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

表示获取X.509证书吊销列表的序列化数据。使用Promise方式返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getEncoded(): Promise<EncodingBlob>--><!--Device-X509CRL-getEncoded(): Promise<EncodingBlob>-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getExtensions

```TypeScript
getExtensions(): DataBlob
```

表示获取CRL扩展的DER格式数据。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getExtensions(): DataBlob--><!--Device-X509CRL-getExtensions(): DataBlob-End-->

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

获取CRL扩展对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getExtensionsObject(): CertExtension--><!--Device-X509CRL-getExtensionsObject(): CertExtension-End-->

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

## getIssuerName

```TypeScript
getIssuerName(): DataBlob
```

表示获取X.509证书吊销列表颁发者名称。 > **说明：** > > 获取到的X.509证书吊销列表颁发者名称数据带字符串结束符。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getIssuerName(): DataBlob--><!--Device-X509CRL-getIssuerName(): DataBlob-End-->

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

## getIssuerName

```TypeScript
getIssuerName(encodingType: EncodingType): string
```

根据编码类型获取X.509证书吊销列表颁发者名称。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getIssuerName(encodingType: EncodingType): string--><!--Device-X509CRL-getIssuerName(encodingType: EncodingType): string-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [encodingType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audiostreaminfo-i.md) | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getIssuerX500DistinguishedName

```TypeScript
getIssuerX500DistinguishedName(): X500DistinguishedName
```

获取CRL颁发者的X.500可分辨名称对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getIssuerX500DistinguishedName(): X500DistinguishedName--><!--Device-X509CRL-getIssuerX500DistinguishedName(): X500DistinguishedName-End-->

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

## getLastUpdate

```TypeScript
getLastUpdate(): string
```

表示获取X.509证书吊销列表最后一次更新日期。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getLastUpdate(): string--><!--Device-X509CRL-getLastUpdate(): string-End-->

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

## getNextUpdate

```TypeScript
getNextUpdate(): string
```

表示获取证书吊销列表下一次更新的日期。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getNextUpdate(): string--><!--Device-X509CRL-getNextUpdate(): string-End-->

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

## getRevokedCert

```TypeScript
getRevokedCert(serialNumber: bigint): X509CRLEntry
```

表示通过指定证书序列号获取证书吊销条目。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getRevokedCert(serialNumber: bigint): X509CRLEntry--><!--Device-X509CRL-getRevokedCert(serialNumber: bigint): X509CRLEntry-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| serialNumber | bigint | 是 |

**返回值：**

| 类型 |
| --- |
| [X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getRevokedCertWithCert

```TypeScript
getRevokedCertWithCert(cert: X509Cert): X509CRLEntry
```

表示通过指定证书对象获取证书吊销条目。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getRevokedCertWithCert(cert: X509Cert): X509CRLEntry--><!--Device-X509CRL-getRevokedCertWithCert(cert: X509Cert): X509CRLEntry-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](arkts-devicecertificate-cert-x509cert-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getRevokedCerts

```TypeScript
getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void
```

表示获取证书吊销条目列表。使用Callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void--><!--Device-X509CRL-getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getRevokedCerts

```TypeScript
getRevokedCerts(): Promise<Array<X509CRLEntry>>
```

表示获取证书吊销条目列表。使用Promise方式返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getRevokedCerts(): Promise<Array<X509CRLEntry>>--><!--Device-X509CRL-getRevokedCerts(): Promise<Array<X509CRLEntry>>-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSignature

```TypeScript
getSignature(): DataBlob
```

表示获取X.509证书吊销列表的签名数据。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getSignature(): DataBlob--><!--Device-X509CRL-getSignature(): DataBlob-End-->

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

## getSignatureAlgName

```TypeScript
getSignatureAlgName(): string
```

表示获取X.509证书吊销列表签名的算法名称。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getSignatureAlgName(): string--><!--Device-X509CRL-getSignatureAlgName(): string-End-->

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

## getSignatureAlgOid

```TypeScript
getSignatureAlgOid(): string
```

表示获取X.509证书吊销列表签名算法的对象标识符OID（Object Identifier）。OID是由国际标准化组织（ISO）的名称注册机构分配。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getSignatureAlgOid(): string--><!--Device-X509CRL-getSignatureAlgOid(): string-End-->

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

## getSignatureAlgParams

```TypeScript
getSignatureAlgParams(): DataBlob
```

表示获取X.509证书吊销列表签名的算法参数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getSignatureAlgParams(): DataBlob--><!--Device-X509CRL-getSignatureAlgParams(): DataBlob-End-->

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

## getTBSInfo

```TypeScript
getTBSInfo(): DataBlob
```

表示获取证书吊销列表的tbsCertList信息。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getTBSInfo(): DataBlob--><!--Device-X509CRL-getTBSInfo(): DataBlob-End-->

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

## getType

```TypeScript
getType(): string
```

表示获取证书吊销列表类型。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getType(): string--><!--Device-X509CRL-getType(): string-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

## getVersion

```TypeScript
getVersion(): number
```

表示获取X.509证书吊销列表的版本号。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-getVersion(): int--><!--Device-X509CRL-getVersion(): int-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| number |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

获取DER格式数据的哈希值。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-hashCode(): Uint8Array--><!--Device-X509CRL-hashCode(): Uint8Array-End-->

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

## isRevoked

```TypeScript
isRevoked(cert: X509Cert): boolean
```

表示检查证书是否吊销。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-isRevoked(cert: X509Cert): boolean--><!--Device-X509CRL-isRevoked(cert: X509Cert): boolean-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](arkts-devicecertificate-cert-x509cert-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## match

```TypeScript
match(param: X509CRLMatchParameters): boolean
```

判断证书吊销列表是否与输入参数匹配。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-match(param: X509CRLMatchParameters): boolean--><!--Device-X509CRL-match(param: X509CRLMatchParameters): boolean-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [X509CRLMatchParameters](arkts-devicecertificate-cert-x509crlmatchparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## toString

```TypeScript
toString(): string
```

获取对象的字符串类型数据。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-toString(): string--><!--Device-X509CRL-toString(): string-End-->

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

## toString

```TypeScript
toString(encodingType: EncodingType): string
```

根据编码类型获取对象的字符串类型数据。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-toString(encodingType: EncodingType): string--><!--Device-X509CRL-toString(encodingType: EncodingType): string-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [encodingType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audiostreaminfo-i.md) | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void
```

表示对X.509证书吊销列表进行验签。使用Callback异步回调。验签支持RSA算法。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void--><!--Device-X509CRL-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | cryptoFramework.PubKey | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey): Promise<void>
```

表示对X.509证书吊销列表进行验签。使用Promise方式返回结果。验签支持RSA算法。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CRL-verify(key: cryptoFramework.PubKey): Promise<void>--><!--Device-X509CRL-verify(key: cryptoFramework.PubKey): Promise<void>-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | cryptoFramework.PubKey | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
