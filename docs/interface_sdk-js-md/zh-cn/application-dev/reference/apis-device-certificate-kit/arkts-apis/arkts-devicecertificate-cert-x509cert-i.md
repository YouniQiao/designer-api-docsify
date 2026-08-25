# X509Cert

提供用于X.509证书操作的API。

**起始版本：** 9

**系统能力：** SystemCapability.Security.Cert

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## checkValidityWithDate

```TypeScript
checkValidityWithDate(date: string): void
```

表示校验X.509证书有效期。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |

## getBasicConstraints

```TypeScript
getBasicConstraints(): number
```

表示获取X.509证书基本约束。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| number |

## getCertSerialNumber

```TypeScript
getCertSerialNumber(): bigint
```

表示获取X.509证书序列号。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| bigint |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |

## getCRLDistributionPoint

```TypeScript
getCRLDistributionPoint(): DataArray
```

获取X.509证书CRL的分发点统一资源标识符。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

表示获取X.509证书序列化数据。使用Callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

表示获取X.509证书序列化数据。使用Promise方式返回结果。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getExtensionsObject

```TypeScript
getExtensionsObject(): CertExtension
```

获取证书扩展对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getExtKeyUsage

```TypeScript
getExtKeyUsage(): DataArray
```

表示获取X.509证书扩展密钥用途。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getIssuerAltNames

```TypeScript
getIssuerAltNames(): DataArray
```

表示获取X.509证书颁发者可选名称。

> **说明：**&gt;
> 获取到的X.509证书颁发者可选名称数据带字符串结束符。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getIssuerName

```TypeScript
getIssuerName(): DataBlob
```

表示获取X.509证书颁发者名称。

> **说明：**&gt;
> - 获取的X.509证书颁发者名称末尾包含一个NUL终止符（值为0），请根据业务需求决定是否去除该终止符。
> - 获取的证书颁发者名称为ASCII编码，转换为字符串后，是以斜杠（/）开始，以斜杠（/）分隔相对可分辨名称的可分辨名称字符串。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getIssuerName

```TypeScript
getIssuerName(encodingType: EncodingType): string
```

表示根据编码类型获取X.509证书颁发者名称。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getIssuerX500DistinguishedName

```TypeScript
getIssuerX500DistinguishedName(): X500DistinguishedName
```

获取X.509证书颁发者的X.500可分辨名称。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getItem

```TypeScript
getItem(itemType: CertItemType): DataBlob
```

表示获取X.509证书对应的字段。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [CertItemType](arkts-devicecertificate-cert-certitemtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getKeyUsage

```TypeScript
getKeyUsage(): DataBlob
```

表示获取X.509证书密钥用途。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getNotAfterTime

```TypeScript
getNotAfterTime(): string
```

表示获取X.509证书过期时间。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getNotBeforeTime

```TypeScript
getNotBeforeTime(): string
```

表示获取X.509证书生效时间。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getPublicKey

```TypeScript
getPublicKey(): cryptoFramework.PubKey
```

表示获取X.509证书公钥。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| cryptoFramework.PubKey |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSerialNumber

```TypeScript
getSerialNumber(): number
```

表示获取X.509证书序列号。

> **说明：**&gt;
> 从API version 9开始支持，从API version 10开始废弃，建议使用
> [X509Cert.getCertSerialNumber()](#getcertserialnumber)替代。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [getCertSerialNumber](#getcertserialnumber)

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| number |

## getSignature

```TypeScript
getSignature(): DataBlob
```

表示获取X.509证书签名数据。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSignatureAlgName

```TypeScript
getSignatureAlgName(): string
```

表示获取X.509证书签名算法名称。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSignatureAlgOid

```TypeScript
getSignatureAlgOid(): string
```

表示获取X.509证书签名算法的对象标识符（OID）。OID由国际标准化组织（ISO）分配。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSignatureAlgParams

```TypeScript
getSignatureAlgParams(): DataBlob
```

表示获取X.509证书签名算法参数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSubjectAltNames

```TypeScript
getSubjectAltNames(): DataArray
```

表示获取X.509证书主体可选名称。

> **说明：**&gt;
> 获取到的X.509证书主体可选名称数据带字符串结束符。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getSubjectName

```TypeScript
getSubjectName(encodingType?: EncodingType): DataBlob
```

表示获取X.509证书主体名称。

> **说明：**&gt;
> - 若不设置encodingType参数，获取的证书主体名称末尾包含一个NUL终止符（值为0），请根据业务需求决定是否去除该终止符。
> - 若不设置encodingType参数，获取的证书主体名称为ASCII编码，转换为字符串后，是以斜杠（/）开始，以斜杠（/）分隔相对可分辨名称的
> 可分辨名称字符串。
> - 建议设置encodingType参数为EncodingType.ENCODING_UTF8，获取的证书主体名称是以逗号（,）分隔相对可分辨名称的可分辨名称字符串。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [encodingType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audiostreaminfo-i.md) | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getSubjectX500DistinguishedName

```TypeScript
getSubjectX500DistinguishedName(): X500DistinguishedName
```

获取X.509证书主体的X.500可分辨名称。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getVersion

```TypeScript
getVersion(): number
```

表示获取X.509证书版本号。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## match

```TypeScript
match(param: X509CertMatchParameters): boolean
```

判断证书是否与输入参数匹配。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [X509CertMatchParameters](arkts-devicecertificate-cert-x509certmatchparameters-i.md) | 是 |

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

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## toString

```TypeScript
toString(encodingType: EncodingType): string
```

根据编码类型获取对象的字符串类型数据。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void
```

表示对证书验签。使用Callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | cryptoFramework.PubKey | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey): Promise<void>
```

表示对证书验签。使用Promise方式返回结果。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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
