# supportsCACertDialog

## supportsCACertDialog

```TypeScript
function supportsCACertDialog(): boolean
```

Check whether the device supports the [openCertificateDetailDialog]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, [openInstallCertificateDialog]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, and [openUninstallCertificateDialog]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ interfaces to open the dialog box for managing CA certificates.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManagerDialog-function supportsCACertDialog(): boolean--><!--Device-certificateManagerDialog-function supportsCACertDialog(): boolean-End-->

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the CA certificate management dialog box can be opened. **true**: supported; **false** |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) | Internal error. Possible causes: 1. IPC communication failed;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Memory operation error; 3. File operation error. Please try again. |

**Example**

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

