# grantPublicCertificate (System API)

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## grantPublicCertificate

```TypeScript
function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>
```

Grants the permission for an application to use the public credentials of a user. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>--><!--Device-certificateManager-function grantPublicCertificate(keyUri: string, clientAppUid: int) : Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyUri | string | Yes | Unique identifier of a user's public credential. |
| clientAppUid | int | Yes | Application UID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; | Promise used to return the operation result, that is, **uri** in the [CMResult]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter verification failed. &lt;br&gt; Possible causes: the URI is null or the URI format is wrong. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt; The application does not have the permission required to call the API. |
| [17500002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500002-certificate-not-exist) | Indicates that the certificate does not exist. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [17500001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-internal-error) | Internal error. Possible causes: 1. IPC communication failed; &lt;br&gt;2. Memory operation error; 3. File operation error. Please try again. |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* Unique identifier of the user public credential. */
let clientAppUid: number = 1001; /* Application UID */
try {
    certificateManager.grantPublicCertificate(keyUri, clientAppUid).then((cmResult: certificateManager.CMResult) => {
        let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
        console.info('Succeeded in granting public certificate.');
    }).catch((err: BusinessError) => {
        console.error(`Failed to grant public certificate. Code: ${err.code}, message: ${err.message}`);
    })
} catch (error: BusinessError) {
    console.error(`Failed to grant public certificate. Code: ${error.code}, message: ${error.message}`);
}
```

