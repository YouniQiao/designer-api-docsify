# getAuthorizedAppList (System API)

## Modules to Import

```TypeScript
```

## getAuthorizedAppList

```TypeScript
function getAuthorizedAppList(keyUri: string) : Promise<CMResult>
```

Obtains the list of authorized applications of a user's public credential. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function getAuthorizedAppList(keyUri: string) : Promise<CMResult>--><!--Device-certificateManager-function getAuthorizedAppList(keyUri: string) : Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

**Examples**

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* Unique identifier of the user public credential. */
try {
  certificateManager.getAuthorizedAppList(keyUri).then((cmResult: certificateManager.CMResult) => {
    if (cmResult?.appUidList == undefined) {
      console.info('The result of getting authorized app list is undefined.');
    } else {
      let appUidList: Array<string> = cmResult.appUidList;
      console.info('Succeeded in getting authorized app list.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get authorized app list. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get authorized app list. Code: ${error.code}, message: ${error.message}`);
}
```
