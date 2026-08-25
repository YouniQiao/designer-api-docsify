# CmsParser

提供解析、验签和解封装CMS消息的API。

> **说明：**&gt;
> PKCS #7是用于存储签名或加密数据的标准语法。注意CMS是PKCS #7的扩展，PKCS #7支持的数据类型包括数据、签名数据、封装数据、
> 签名和封装数据、摘要数据、加密数据。常用于保护数据的完整性和机密性。

**起始版本：** 22

**系统能力：** SystemCapability.Security.Cert

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## decryptEnvelopedData

```TypeScript
decryptEnvelopedData(config: CmsEnvelopedDecryptionConfig): Promise<Uint8Array>
```

用于解密封装数据类型的CMS消息。使用Promise方式返回结果。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [CmsEnvelopedDecryptionConfig](arkts-devicecertificate-cert-cmsenvelopeddecryptionconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getCerts

```TypeScript
getCerts(type: CmsCertType): Promise<Array<X509Cert>>
```

传入枚举值，用于从签名数据类型的CMS消息中获取证书。当前支持获取签名者证书或全部证书。使用Promise方式返回结果。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [CmsCertType](arkts-devicecertificate-cert-cmscerttype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;X509Cert & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getContentData

```TypeScript
getContentData(): Promise<Uint8Array>
```

用于从签名数据类型的CMS消息中获取内容数据。使用Promise方式返回结果。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getContentType

```TypeScript
getContentType(): CmsContentType
```

用于获取CMS内容类型。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [CmsContentType](arkts-devicecertificate-cert-cmscontenttype-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## setRawData

```TypeScript
setRawData(data: Uint8Array | string, cmsFormat: CmsFormat): Promise<void>
```

设置CMS消息数据。使用Promise方式返回结果。

> **说明：**&gt;
> 支持PEM和DER格式的CMS消息。**string**对应PEM格式，**Uint8Array**对应DER格式。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Uint8Array \| string | 是 |
| cmsFormat | [CmsFormat](arkts-devicecertificate-cert-cmsformat-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## verifySignedData

```TypeScript
verifySignedData(config: CmsVerificationConfig): Promise<void>
```

用于验证签名数据类型的CMS消息。使用Promise方式返回结果。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [CmsVerificationConfig](arkts-devicecertificate-cert-cmsverificationconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |
