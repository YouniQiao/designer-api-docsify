# createCertChainValidator

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createCertChainValidator

```TypeScript
function createCertChainValidator(algorithm: string): CertChainValidator
```

表示创建证书链校验器对象。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [algorithm](arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [CertChainValidator](arkts-devicecertificate-cert-certchainvalidator-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
