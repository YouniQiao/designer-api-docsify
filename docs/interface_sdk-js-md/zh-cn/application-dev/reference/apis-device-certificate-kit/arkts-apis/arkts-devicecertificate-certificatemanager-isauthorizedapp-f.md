# isAuthorizedApp

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## isAuthorizedApp

```TypeScript
function isAuthorizedApp(keyUri: string): Promise<boolean>
```

表示当前应用是否由指定的用户凭据授权。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
