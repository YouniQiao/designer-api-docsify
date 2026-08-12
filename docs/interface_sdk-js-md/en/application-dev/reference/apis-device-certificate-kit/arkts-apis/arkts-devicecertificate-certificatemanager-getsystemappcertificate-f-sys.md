# getSystemAppCertificate (System API)

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## getSystemAppCertificate

```TypeScript
function getSystemAppCertificate(keyUri: string) : Promise<CMResult>
```

Obtains the credential details of the system application. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_SYSTEM_APP_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function getSystemAppCertificate(keyUri: string) : Promise<CMResult>--><!--Device-certificateManager-function getSystemAppCertificate(keyUri: string) : Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyUri | string | Yes | Unique identifier of a system application credential. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; | Promise used to return the operation result, that is, **credential** in the [CMResult]{ |

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

let keyUri: string = 'test'; /* Unique identifier of the system application credential. */
try {
    certificateManager.getSystemAppCertificate(keyUri).then((cmResult: certificateManager.CMResult) => {
        if (cmResult?.credential == undefined) {
            console.info('The result of getting system app certificate is undefined.');
        } else {
        let cred: certificateManager.Credential = cmResult.credential;
            console.info('Succeeded in getting system app certificate.');
        }
    }).catch((err: BusinessError) => {
        console.error(`Failed to get system app certificate. Code: ${err.code}, message: ${err.message}`);
    })
} catch (error: BusinessError) {
    console.error(`Failed to get system app certificate. Code: ${error.code}, message: ${error.message}`);
}
```

