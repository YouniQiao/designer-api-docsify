# uninstallAllAppCertificate（系统接口）

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## uninstallAllAppCertificate

```TypeScript
function uninstallAllAppCertificate() : Promise<void>
```

卸载所有系统应用凭据和用户公共凭据，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL and ohos.permission.ACCESS_SYSTEM_APP_CERT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
