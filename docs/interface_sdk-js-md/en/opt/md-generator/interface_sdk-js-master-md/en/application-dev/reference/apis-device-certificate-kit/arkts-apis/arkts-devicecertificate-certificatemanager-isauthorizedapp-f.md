# isAuthorizedApp

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## isAuthorizedApp

```TypeScript
function isAuthorizedApp(keyUri: string): Promise<boolean>
```

Checks whether this application is authorized by the specified user credential. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function isAuthorizedApp(keyUri: string): Promise<boolean>--><!--Device-certificateManager-function isAuthorizedApp(keyUri: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* Unique identifier of the credential. The process for authorizing the credential to the application is omitted here. */
try {
  certificateManager.isAuthorizedApp(uri).then((res) => {
    if (res) {
      console.info('The application is authorized by the user.');
    } else {
      console.info('The application is not authorized by the user.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to check if the application is authorized. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to check if the application is authorized. Code: ${error.code}, message: ${error.message}`);
}
```
