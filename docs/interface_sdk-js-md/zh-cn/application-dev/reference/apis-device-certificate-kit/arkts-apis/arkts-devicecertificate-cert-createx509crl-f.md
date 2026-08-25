# createX509CRL

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createX509CRL

```TypeScript
function createX509CRL(inStream: EncodingBlob, callback: AsyncCallback<X509CRL>): void
```

表示创建X.509证书吊销列表对象。使用Callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inStream | [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[X509CRL](arkts-devicecertificate-cert-x509crl-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |


## createX509CRL

```TypeScript
function createX509CRL(inStream: EncodingBlob): Promise<X509CRL>
```

表示创建X.509证书吊销列表对象。使用Promise方式返回结果。

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
| Promise&lt;[X509CRL](arkts-devicecertificate-cert-x509crl-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
