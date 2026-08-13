# X509CertChain

X.509证书链对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-cert-interface X509CertChain--><!--Device-cert-interface X509CertChain-End-->

**系统能力：** SystemCapability.Security.Cert

## getCertList

```TypeScript
getCertList(): Array<X509Cert>
```

获取X.509证书列表。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CertChain-getCertList(): Array<X509Cert>--><!--Device-X509CertChain-getCertList(): Array<X509Cert>-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| Array&lt;[X509Cert](arkts-devicecertificate-cert-x509cert-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

获取DER格式数据的哈希值。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CertChain-hashCode(): Uint8Array--><!--Device-X509CertChain-hashCode(): Uint8Array-End-->

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

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X509CertChain-toString(): string--><!--Device-X509CertChain-toString(): string-End-->

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

## validate

```TypeScript
validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>
```

校验证书链。使用Promise方式返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CertChain-validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>--><!--Device-X509CertChain-validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [CertChainValidationParameters](arkts-devicecertificate-cert-certchainvalidationparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CertChainValidationResult](arkts-devicecertificate-cert-certchainvalidationresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030002](../errorcode-cert.md#19030002-证书签名验证错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030006](../errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |

## validate

```TypeScript
validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void
```

使用校验参数校验证书链。使用Callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-X509CertChain-validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void--><!--Device-X509CertChain-validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [CertChainValidationParameters](arkts-devicecertificate-cert-certchainvalidationparameters-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CertChainValidationResult](arkts-devicecertificate-cert-certchainvalidationresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030002](../errorcode-cert.md#19030002-证书签名验证错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030006](../errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |
