# createX509CertChain

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createX509CertChain

```TypeScript
function createX509CertChain(inStream: EncodingBlob): Promise<X509CertChain>
```

表示创建X.509证书链对象。使用Promise方式返回结果。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inStream | [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[X509CertChain](arkts-devicecertificate-cert-x509certchain-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |


## createX509CertChain

```TypeScript
function createX509CertChain(inStream: EncodingBlob, callback: AsyncCallback<X509CertChain>): void
```

表示创建X.509证书链对象。使用Callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inStream | [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CertChain](arkts-devicecertificate-cert-x509certchain-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |


## createX509CertChain

```TypeScript
function createX509CertChain(certs: Array<X509Cert>): X509CertChain
```

表示使用X509Cert数组方式创建X.509证书链对象，并同步返回结果。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [certs](../../apis-universal-keystore-kit/arkts-apis/arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md) | Array & lt;X509Cert & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [X509CertChain](arkts-devicecertificate-cert-x509certchain-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
