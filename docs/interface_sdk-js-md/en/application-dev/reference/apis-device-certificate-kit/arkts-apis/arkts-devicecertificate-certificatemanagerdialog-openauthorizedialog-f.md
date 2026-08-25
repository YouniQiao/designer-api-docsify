# openAuthorizeDialog

## Modules to Import

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openAuthorizeDialog

```TypeScript
function openAuthorizeDialog(context: common.Context): Promise<string>
```

Opens the authorization page of the certificate management dialog box to grant a credential to the application. After the API is successfully called, the app can use the URI of the authorization certificate returned by the API to sign, verify the signature, and query details. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |

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


## openAuthorizeDialog

```TypeScript
function openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>
```

Opens the Certificate Credential Authorization page of the Certificate Management dialog box. On the page that is displayed, you can authorize the application to use certificate credentials. After the API is called successfully, the app can use the URI of the authorization certificate returned by the API to sign, verify the signature, and query details. The types of certificates that can be authorized include application certificate credentials, user certificate credentials, and USB Key certificate credentials. Using Promise Asynchronous Callbacks.

**Since:** 22

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.CertificateManagerDialog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |
| authorizeRequest | [AuthorizeRequest](arkts-devicecertificate-certificatemanagerdialog-authorizerequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CertReference](arkts-devicecertificate-certificatemanagerdialog-certreference-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) |
| [29700002](../errorcode-certManagerDialog.md#29700002-operation-canceled) |
| [29700006](../errorcode-certManagerDialog.md#29700006-failed-to-validate-the-input-parameter) |
| [29700007](../errorcode-certManagerDialog.md#29700007-no-available-authorization-certificate) |
