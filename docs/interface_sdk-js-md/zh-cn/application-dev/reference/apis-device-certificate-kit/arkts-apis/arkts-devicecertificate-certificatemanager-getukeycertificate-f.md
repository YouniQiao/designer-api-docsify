# getUkeyCertificate

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getUkeyCertificate

```TypeScript
function getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>
```

获取USB Key证书凭据详细信息。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyUri | string | 是 |
| ukeyInfo | [UkeyInfo](arkts-devicecertificate-certificatemanager-ukeyinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500002](../errorcode-certManager.md#17500002-证书不存在) |
| [17500010](../errorcode-certManager.md#17500010-访问usb证书凭据失败) |
| [17500011](../errorcode-certManager.md#17500011-入参校验失败) |
