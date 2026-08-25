# getAllUserTrustedCertificates

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getAllUserTrustedCertificates

```TypeScript
function getAllUserTrustedCertificates(): Promise<CMResult>
```

表示获取当前用户和设备公共位置的所有用户根CA证书列表。使用Promise异步回调。

**起始版本：** 12

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


## getAllUserTrustedCertificates

```TypeScript
function getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>
```

表示根据证书的位置获取用户根CA证书列表。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scope | [CertScope](arkts-devicecertificate-certificatemanager-certscope-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
