# openUninstallCertificateDialog

## openUninstallCertificateDialog

```TypeScript
function openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>
```

打开证书管理卸载证书向导，显示相应的页面。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-certificateManagerDialog-function openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>--><!--Device-certificateManagerDialog-function openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>-End-->

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |
| certType | [CertificateType](arkts-devicecertificate-certificatemanagerdialog-certificatetype-e.md) | 是 |
| certUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [29700005](../errorcode-certManagerDialog.md#29700005-操作不符合设备安全策略) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [29700004](../errorcode-certManagerDialog.md#29700004-设备类型不支持) |
| [29700001](../errorcode-certManagerDialog.md#29700001-内部错误) |
| [29700003](../errorcode-certManagerDialog.md#29700003-证书安装失败错误) |
| [29700002](../errorcode-certManagerDialog.md#29700002-操作取消) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* certificateType为证书类型，此处赋值CA_CERT，即删除CA证书 */
let certificateType: certificateManagerDialog.CertificateType = certificateManagerDialog.CertificateType.CA_CERT;
/* certUri为业务安装证书返回的唯一标识符，此处仅为示例 */
let certUri: string = "test";
try {
  certificateManagerDialog.openUninstallCertificateDialog(context, certificateType, certUri).then(() => {
    console.info('Succeeded in opening uninstall certificate');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to open uninstall certificate dialog. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to open uninstall certificate dialog. Code: ${error.code}, message: ${error.message}`);
}
```
