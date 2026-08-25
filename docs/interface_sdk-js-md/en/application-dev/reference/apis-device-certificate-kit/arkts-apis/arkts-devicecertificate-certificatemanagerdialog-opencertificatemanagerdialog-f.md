# openCertificateManagerDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openCertificateManagerDialog

```TypeScript
function openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise<void>
```

Opens the certificate management dialog box and displays the page of the specified type. After the interface is invoked successfully, you can view, install, and uninstall the certificate in the dialog box that is displayed. This API uses a promise to return the result.

**Since:** 13

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |
| pageType | [CertificateDialogPageType](arkts-devicecertificate-certificatemanagerdialog-certificatedialogpagetype-e.md) | Yes |

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
