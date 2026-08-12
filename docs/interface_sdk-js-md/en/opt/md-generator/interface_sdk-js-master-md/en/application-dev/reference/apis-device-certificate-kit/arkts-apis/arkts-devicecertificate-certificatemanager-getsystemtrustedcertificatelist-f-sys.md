# getSystemTrustedCertificateList (System API)

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## getSystemTrustedCertificateList

```TypeScript
function getSystemTrustedCertificateList(): Promise<CMResult>
```

Obtains the list of CA certificates trusted by the system. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function getSystemTrustedCertificateList(): Promise<CMResult>--><!--Device-certificateManager-function getSystemTrustedCertificateList(): Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17500001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getSystemTrustedCertificateList().then((cmResult: certificateManager.CMResult) => {
    if (cmResult === undefined) { // If the number of trusted CA certificates is 0, the returned cmResult is undefined.
      console.info('The count of system trusted certificates is 0.');
    } else if (cmResult.certList == undefined) {
      console.info('The result of getting system trusted certificates is undefined.');
    } else {
      let list: Array<certificateManager.CertAbstract> = cmResult.certList;
      console.info('Succeeded in getting system trusted certificates.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get system trusted certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get system trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```
