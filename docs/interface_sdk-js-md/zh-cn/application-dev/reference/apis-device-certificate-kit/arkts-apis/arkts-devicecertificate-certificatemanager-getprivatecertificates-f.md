# getPrivateCertificates

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getPrivateCertificates

```TypeScript
function getPrivateCertificates(): Promise<CMResult>
```

表示获取应用安装的凭据列表。使用Promise异步回调。

**起始版本：** 13

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
