# supportsCACertDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
```

## supportsCACertDialog

```TypeScript
function supportsCACertDialog(): boolean
```

Check whether the device supports the [openCertificateDetailDialog](arkts-devicecertificate-certificatemanagerdialog-opencertificatedetaildialog-f.md#openCertificateDetailDialog), [openInstallCertificateDialog](arkts-devicecertificate-certificatemanagerdialog-openinstallcertificatedialog-f.md#openInstallCertificateDialog), and [openUninstallCertificateDialog](arkts-devicecertificate-certificatemanagerdialog-openuninstallcertificatedialog-f.md#openUninstallCertificateDialog) interfaces to open the dialog box for managing CA certificates.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManagerDialog-function supportsCACertDialog(): boolean--><!--Device-certificateManagerDialog-function supportsCACertDialog(): boolean-End-->

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [29700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManagerDialog.md#29700001-internal-error) |

## Examples

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSupport: boolean = certificateManagerDialog.supportsCACertDialog();
  console.info(`Succeeded in checking whether the device supports CA dialog.`)
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to check whether the device supports CA dialog. Code: ${error.code}, message: ${error.message}`);
}
```
