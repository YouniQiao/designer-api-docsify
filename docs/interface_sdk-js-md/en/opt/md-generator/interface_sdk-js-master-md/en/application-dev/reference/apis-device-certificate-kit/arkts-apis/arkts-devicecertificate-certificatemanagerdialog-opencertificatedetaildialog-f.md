# openCertificateDetailDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
```

## openCertificateDetailDialog

```TypeScript
function openCertificateDetailDialog(context: common.Context,cert: Uint8Array, property: CertificateDialogProperty): Promise<void>
```

Opens the Certificate Management dialog box to display the certificate details. After the interface is invoked successfully, detailed information about the certificate, such as the basic information, validity period, issuer, and user, is displayed. Use Promise asynchronous callback.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManagerDialog-function openCertificateDetailDialog(context: common.Context,cert: Uint8Array, property: CertificateDialogProperty): Promise<void>--><!--Device-certificateManagerDialog-function openCertificateDetailDialog(context: common.Context,cert: Uint8Array, property: CertificateDialogProperty): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [29700004](../errorcode-certManagerDialog.md#29700004-operation-not-supported-by-the-device) |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) |
| [29700003](../errorcode-certManagerDialog.md#29700003-failed-to-install-the-certificate) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context is application context information, which is obtained by the caller. The context here is only an example. */
let context: common.Context = new UIContext().getHostContext() as common.Context;
/* The CA certificate data must be assigned by the service. In this example, the data is not CA certificate data. */
let caCert: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let property: certificateManagerDialog.CertificateDialogProperty = {
  showInstallButton: false /* Do not display the button for installing the certificate.*/
};
try {
  certificateManagerDialog.openCertificateDetailDialog(context, caCert, property).then(() => {
    console.info('Succeeded opening certificate detail dialog.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to open certificate detail dialog. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to open certificate detail dialog. Code: ${error.code}, message: ${error.message}`);
}
```
