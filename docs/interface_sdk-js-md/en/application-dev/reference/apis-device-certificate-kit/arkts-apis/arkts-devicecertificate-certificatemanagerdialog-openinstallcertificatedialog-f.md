# openInstallCertificateDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openInstallCertificateDialog

```TypeScript
function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>
```

Opens the Certificate Management Install Certificate dialog box. After the certificate is successfully installed, the unique identifier of the certificate is returned. Applications can use the identifier to use the certificate. Use Promise asynchronous callback.

**Since:** 14

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |
| certType | [CertificateType](arkts-devicecertificate-certificatemanagerdialog-certificatetype-e.md) | Yes |
| certScope | [CertificateScope](arkts-devicecertificate-certificatemanagerdialog-certificatescope-e.md) | Yes |
| cert | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) |
| [29700002](../errorcode-certManagerDialog.md#29700002-operation-canceled) |
| [29700003](../errorcode-certManagerDialog.md#29700003-failed-to-install-the-certificate) |
| [29700004](../errorcode-certManagerDialog.md#29700004-operation-not-supported-by-the-device) |
| [29700005](../errorcode-certManagerDialog.md#29700005-non-secure-operation) |
