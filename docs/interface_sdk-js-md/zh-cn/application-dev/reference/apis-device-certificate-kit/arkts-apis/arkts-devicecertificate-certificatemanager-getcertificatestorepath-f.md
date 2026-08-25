# getCertificateStorePath

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getCertificateStorePath

```TypeScript
function getCertificateStorePath(property: CertStoreProperty): string
```

表示获取证书的存储路径。

**起始版本：** 18

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [CertStoreProperty](arkts-devicecertificate-certificatemanager-certstoreproperty-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500009](../errorcode-certManager.md#17500009-不支持指定的证书存储路径) |
