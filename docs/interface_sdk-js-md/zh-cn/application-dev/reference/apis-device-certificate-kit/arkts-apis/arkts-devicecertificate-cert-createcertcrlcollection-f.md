# createCertCRLCollection

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createCertCRLCollection

```TypeScript
function createCertCRLCollection(certs: Array<X509Cert>, crls?: Array<X509CRL>): CertCRLCollection
```

表示创建证书和证书吊销列表集合对象，并返回相应的结果。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [certs](../../apis-universal-keystore-kit/arkts-apis/arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md) | Array & lt;X509Cert & gt; | 是 |
| [crls](arkts-devicecertificate-cert-x509certrevokedparams-i.md) | Array&lt;[X509CRL](arkts-devicecertificate-cert-x509crl-i.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [CertCRLCollection](arkts-devicecertificate-cert-certcrlcollection-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
