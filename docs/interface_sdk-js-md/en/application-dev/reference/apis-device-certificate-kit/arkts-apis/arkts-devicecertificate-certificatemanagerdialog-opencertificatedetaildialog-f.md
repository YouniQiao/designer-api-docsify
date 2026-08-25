# openCertificateDetailDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openCertificateDetailDialog

```TypeScript
function openCertificateDetailDialog(context: common.Context,cert: Uint8Array, property: CertificateDialogProperty): Promise<void>
```

Opens the Certificate Management dialog box to display the certificate details. After the interface is invoked successfully, detailed information about the certificate, such as the basic information, validity period, issuer, and user, is displayed. Use Promise asynchronous callback.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |
| cert | Uint8Array | Yes |
| property | [CertificateDialogProperty](arkts-devicecertificate-certificatemanagerdialog-certificatedialogproperty-i.md) | Yes |

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
| [29700003](../errorcode-certManagerDialog.md#29700003-failed-to-install-the-certificate) |
| [29700004](../errorcode-certManagerDialog.md#29700004-operation-not-supported-by-the-device) |
