# createCertChainValidator

## createCertChainValidator

```TypeScript
function createCertChainValidator(algorithm: string): CertChainValidator
```

表示创建证书链校验器对象。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-cert-function createCertChainValidator(algorithm: string): CertChainValidator--><!--Device-cert-function createCertChainValidator(algorithm: string): CertChainValidator-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| algorithm | string | 是 |

**返回值：**

| 类型 |
| --- |
| [CertChainValidator](arkts-devicecertificate-cert-certchainvalidator-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## 示例

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let validator = cert.createCertChainValidator('PKIX');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`createCertChainValidator failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```
