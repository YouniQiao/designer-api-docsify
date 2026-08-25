# openInstallCertificateDialog

## 导入模块

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openInstallCertificateDialog

```TypeScript
function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>
```

打开证书管理安装证书向导，显示相应的页面。证书安装成功后，返回证书的唯一标识符，应用可通过该标识符对证书进行使用。使用Promise异步回调。

**起始版本：** 14

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |
| certType | [CertificateType](arkts-devicecertificate-certificatemanagerdialog-certificatetype-e.md) | 是 |
| certScope | [CertificateScope](arkts-devicecertificate-certificatemanagerdialog-certificatescope-e.md) | 是 |
| cert | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29700001](../errorcode-certManagerDialog.md#29700001-内部错误) |
| [29700002](../errorcode-certManagerDialog.md#29700002-操作取消) |
| [29700003](../errorcode-certManagerDialog.md#29700003-证书安装失败错误) |
| [29700004](../errorcode-certManagerDialog.md#29700004-设备类型不支持) |
| [29700005](../errorcode-certManagerDialog.md#29700005-操作不符合设备安全策略) |
