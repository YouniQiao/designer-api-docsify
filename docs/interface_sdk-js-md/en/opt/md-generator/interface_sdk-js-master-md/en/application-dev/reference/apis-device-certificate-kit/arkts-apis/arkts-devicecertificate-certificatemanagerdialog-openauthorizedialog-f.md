# openAuthorizeDialog

## Modules to Import

```TypeScript
```

## openAuthorizeDialog

```TypeScript
function openAuthorizeDialog(context: common.Context): Promise<string>
```

Opens the authorization page of the certificate management dialog box to grant a credential to the application. After the API is successfully called, the app can use the URI of the authorization certificate returned by the API to sign, verify the signature, and query details. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManagerDialog-function openAuthorizeDialog(context: common.Context): Promise<string>--><!--Device-certificateManagerDialog-function openAuthorizeDialog(context: common.Context): Promise<string>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) |
| [29700002](../errorcode-certManagerDialog.md#29700002-operation-canceled) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context is application context information, which is obtained by the caller. The context here is only an example. */
let context: common.Context = new UIContext().getHostContext() as common.Context;
try {
  certificateManagerDialog.openAuthorizeDialog(context).then((uri: string) => {
    console.info(`Succeeded in authorizing certificate, uri: ${uri}`)
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to authorize certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to authorize certificate. Code: ${error.code}, message: ${error.message}`);
}
```


## openAuthorizeDialog

```TypeScript
function openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>
```

Opens the Certificate Credential Authorization page of the Certificate Management dialog box. On the page that is displayed, you can authorize the application to use certificate credentials. After the API is called successfully, the app can use the URI of the authorization certificate returned by the API to sign, verify the signature, and query details. The types of certificates that can be authorized include application certificate credentials, user certificate credentials, and USB Key certificate credentials. Using Promise Asynchronous Callbacks.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManagerDialog-function openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>--><!--Device-certificateManagerDialog-function openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>-End-->

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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [29700007](../errorcode-certManagerDialog.md#29700007-no-available-authorization-certificate) |
| [29700006](../errorcode-certManagerDialog.md#29700006-failed-to-validate-the-input-parameter) |
| [29700001](../errorcode-certManagerDialog.md#29700001-internal-error) |
| [29700002](../errorcode-certManagerDialog.md#29700002-operation-canceled) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { certificateManagerDialog, certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

/* context is application context information, which is obtained by the caller. The context here is only an example. */
let context: common.Context = new UIContext().getHostContext() as common.Context;
let certTypes: Array<certificateManagerDialog.CertificateType> = [
  certificateManagerDialog.CertificateType.CREDENTIAL_USER,
  certificateManagerDialog.CertificateType.CREDENTIAL_APP,
  certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
];
let certPurpose: certificateManager.CertificatePurpose = certificateManager.CertificatePurpose.PURPOSE_DEFAULT;
let authorizeRequest: certificateManagerDialog.AuthorizeRequest = { certTypes: certTypes, certPurpose: certPurpose };
try {
  certificateManagerDialog.openAuthorizeDialog(context, authorizeRequest).then((certReference: certificateManagerDialog.CertReference) => {
    let reference = certReference;
    console.info(`Succeeded in opening authorize dialog.`)
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to open authorize dialog. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to open authorize dialog. Code: ${error.code}, message: ${error.message}`);
}
```
