# openUkeyAuthDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openUkeyAuthDialog

```TypeScript
function openUkeyAuthDialog(context: common.Context, ukeyAuthRequest: UkeyAuthRequest): Promise<void>
```

Opens the PIN authentication dialog box of the USB Key credential. On the displayed page, the user can enter the PIN to authorize the USB credential. After the call is successful, the USB key credential will be unlocked. The app can use the credential to perform operations such as signing and encryption. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |
| ukeyAuthRequest | [UkeyAuthRequest](arkts-devicecertificate-certificatemanagerdialog-ukeyauthrequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29700006](../errorcode-certManagerDialog.md#29700006-failed-to-validate-the-input-parameter) |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) |
| [29700002](../errorcode-certManagerDialog.md#29700002-operation-canceled) |
| [29700003](../errorcode-certManagerDialog.md#29700003-failed-to-install-the-certificate) |
