# openUninstallCertificateDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openUninstallCertificateDialog

```TypeScript
function openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>
```

Open the Certificate Management Uninstall Certificate dialog. The corresponding page is displayed. Use Promise asynchronous callbacks.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |
| certType | [CertificateType](arkts-devicecertificate-certificatemanagerdialog-certificatetype-e.md) | Yes |
| certUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) |
| [29700002](../errorcode-certManagerDialog.md#29700002-operation-canceled) |
| [29700003](../errorcode-certManagerDialog.md#29700003-failed-to-install-the-certificate) |
| [29700004](../errorcode-certManagerDialog.md#29700004-operation-not-supported-by-the-device) |
| [29700005](../errorcode-certManagerDialog.md#29700005-non-secure-operation) |
