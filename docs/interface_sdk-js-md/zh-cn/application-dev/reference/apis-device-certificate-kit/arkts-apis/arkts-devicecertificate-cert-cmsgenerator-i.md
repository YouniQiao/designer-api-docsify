# CmsGenerator

提供生成CMS（Cryptographic Message Syntax）消息的API。

> **说明：**&gt;
> PKCS #7是用于存储签名或加密数据的标准语法。注意CMS是PKCS #7的扩展，PKCS #7支持的数据类型包括数据、签名数据、封装数据、
> 签名和封装数据、摘要数据、加密数据。常用于保护数据的完整性和机密性。

**起始版本：** 18

**系统能力：** SystemCapability.Security.Cert

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## addCert

```TypeScript
addCert(cert: X509Cert): void
```

用于添加内容类型为SIGNED_DATA的CMS的证书，例如签名证书的颁发者证书。

如果未调用addSigner接口，并且仅添加证书后，生成的CMS签名数据将只包含证书。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## addRecipientInfo

```TypeScript
addRecipientInfo(recipientInfo: CmsRecipientInfo): Promise<void>
```

为内容类型为ENVELOPED_DATA的CMS添加接收者信息。使用Promise方式返回结果。

该方法至少需要设置一个接收者。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| recipientInfo | [CmsRecipientInfo](arkts-devicecertificate-cert-cmsrecipientinfo-i.md) | 是 |

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

## addSigner

```TypeScript
addSigner(cert: X509Cert, keyInfo: PrivateKeyInfo, config: CmsSignerConfig): void
```

用于为内容类型为SIGNED_DATA的CMS添加签名者信息。

> **说明：**&gt;
> 自签名证书不能作为签名者。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | 是 |
| [keyInfo](arkts-devicecertificate-cert-cmsenvelopeddecryptionconfig-i.md) | [PrivateKeyInfo](arkts-devicecertificate-cert-privatekeyinfo-i.md) | 是 |
| config | [CmsSignerConfig](arkts-devicecertificate-cert-cmssignerconfig-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030008](../errorcode-cert.md#19030008-私钥密码错误) |

## doFinal

```TypeScript
doFinal(data: Uint8Array, options?: CmsGeneratorOptions): Promise<Uint8Array | string>
```

用于获取CMS最终数据，例如CMS签名数据或CMS封装数据。使用Promise方式返回结果。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Uint8Array | 是 |
| options | [CmsGeneratorOptions](arkts-devicecertificate-cert-cmsgeneratoroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array \ | string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## doFinalSync

```TypeScript
doFinalSync(data: Uint8Array, options?: CmsGeneratorOptions): Uint8Array | string
```

用于获取CMS消息，例如CMS签名数据或CMS封装数据。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Uint8Array | 是 |
| options | [CmsGeneratorOptions](arkts-devicecertificate-cert-cmsgeneratoroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Uint8Array \| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEncryptedContentData

```TypeScript
getEncryptedContentData(): Promise<Uint8Array>
```

用于获取内容类型为ENVELOPED_DATA的CMS的加密内容数据。使用Promise方式返回结果。

如果创建了类型为ENVELOPED_DATA的CmsGenerator并使用了数据分离来生成CMS封装数据，使用此方法来获取加密的内容数据。

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

## setRecipientEncryptionAlgorithm

```TypeScript
setRecipientEncryptionAlgorithm(algorithm: CmsRecipientEncryptionAlgorithm): void
```

为内容类型为ENVELOPED_DATA的CMS设置加密算法。

该方法应在创建ENVELOPED_DATA类型的CmsGenerator后立即调用。如果未调用此方法，则默认使用AES_256_GCM作为加密算法。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [algorithm](arkts-devicecertificate-cert-certchainvalidator-i.md) | [CmsRecipientEncryptionAlgorithm](arkts-devicecertificate-cert-cmsrecipientencryptionalgorithm-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
