# installPublicCertificate（系统接口）

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## installPublicCertificate

```TypeScript
function installPublicCertificate(keystore: Uint8Array, keystorePwd: string) : Promise<CMResult>
```

安装用户的公共凭据，仅证书管理应用调用。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keystore | Uint8Array | 是 |
| keystorePwd | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500003](../errorcode-certManager.md#17500003-证书或凭据无效) |
| [17500004](../errorcode-certManager.md#17500004-证书或凭据数量达到上限) |
| [17500008](../errorcode-certManager.md#17500008-密码错误) |
