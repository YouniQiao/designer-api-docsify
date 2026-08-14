# supportsCACertDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'certificateManagerDialog';
```

## supportsCACertDialog

```TypeScript
function supportsCACertDialog(): boolean
```

Check whether the device supports the [openCertificateDetailDialog](arkts-devicecertificate-certificatemanagerdialog-opencertificatedetaildialog-f.md#openCertificateDetailDialog), [openInstallCertificateDialog](arkts-devicecertificate-certificatemanagerdialog-openinstallcertificatedialog-f.md#openInstallCertificateDialog), and [openUninstallCertificateDialog](arkts-devicecertificate-certificatemanagerdialog-openuninstallcertificatedialog-f.md#openUninstallCertificateDialog) interfaces to open the dialog box for managing CA certificates.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManagerDialog-function supportsCACertDialog(): boolean--><!--Device-certificateManagerDialog-function supportsCACertDialog(): boolean-End-->

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the CA certificate management dialog box can be opened. **true**: supported; **false** : not supported |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) | Internal error. Possible causes: 1. IPC communication failed; <br>2. Memory operation error; 3. File operation error. Please try again. |

## Examples

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSupport: boolean = certificateManagerDialog.supportsCACertDialog();
  console.info(`Success to check whether the device supports CA dialog.`)
} catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to check whether the device supports CA dialog. Code: ${error.code}, message: ${error.message}`);
}
```

