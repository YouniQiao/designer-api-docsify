# openInstallCertificateDialog

## 导入模块

```TypeScript
```

## openInstallCertificateDialog

```TypeScript
function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>
```

打开证书管理安装证书向导，显示相应的页面。证书安装成功后，返回证书的唯一标识符，应用可通过该标识符对证书进行使用。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManagerDialog-function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>--><!--Device-certificateManagerDialog-function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>-End-->

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
| [29700005](../errorcode-certManagerDialog.md#29700005-操作不符合设备安全策略) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29700004](../errorcode-certManagerDialog.md#29700004-设备类型不支持) |
| [29700001](../errorcode-certManagerDialog.md#29700001-内部错误) |
| [29700003](../errorcode-certManagerDialog.md#29700003-证书安装失败错误) |
| [29700002](../errorcode-certManagerDialog.md#29700002-操作取消) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* certificateType为证书类型，此处赋值CA_CERT，即安装CA证书 */
let certificateType: certificateManagerDialog.CertificateType = certificateManagerDialog.CertificateType.CA_CERT;
/* certificateScope为证书使用范围，此处赋值CURRENT_USER，即当前用户下可用 */
let certificateScope: certificateManagerDialog.CertificateScope = certificateManagerDialog.CertificateScope.CURRENT_USER;
/* 安装的CA证书数据需要业务赋值，本例数据非CA证书数据 */
let caCert: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
try {
  certificateManagerDialog.openInstallCertificateDialog(context, certificateType, certificateScope, caCert).then((uri: string) => {
    console.info('Succeeded in opening install certificate');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to open install certificate dialog. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to open install certificate dialog. Code: ${error.code}, message: ${error.message}`);
}
```
