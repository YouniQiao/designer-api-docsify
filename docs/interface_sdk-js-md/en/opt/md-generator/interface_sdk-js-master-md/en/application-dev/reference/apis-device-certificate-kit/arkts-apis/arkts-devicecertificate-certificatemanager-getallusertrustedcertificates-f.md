# getAllUserTrustedCertificates

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getAllUserTrustedCertificates

```TypeScript
function getAllUserTrustedCertificates(): Promise<CMResult>
```

Obtains all user trusted root CA certificates of the device. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function getAllUserTrustedCertificates(): Promise<CMResult>--><!--Device-certificateManager-function getAllUserTrustedCertificates(): Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CMResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getAllUserTrustedCertificates().then((cmResult) => {
    if (cmResult === undefined) { // If the number of root CA certificates is 0, the returned cmResult is undefined.
      console.info('The count of the user trusted certificates is 0.');
    } else if (cmResult.certList == undefined) {
      console.info('The result of getting all user trusted certificates is undefined.');
    } else {
      let list = cmResult.certList;
      console.info('Succeeded in getting all user trusted certificates.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get all user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get all user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```


## getAllUserTrustedCertificates

```TypeScript
function getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>
```

Obtains the user root CA certificates based on the certificate scope. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>--><!--Device-certificateManager-function getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scope | [CertScope](arkts-devicecertificate-certificatemanager-certscope-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CMResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  /* Obtain the user root CA certificates of the current user. To obtain the user root CA certificates accessible to all users, pass in GLOBAL_USER. */
  let scope: certificateManager.CertScope = certificateManager.CertScope.CURRENT_USER;
  certificateManager.getAllUserTrustedCertificates(scope).then((cmResult) => {
    if (cmResult === undefined) { // If the number of root CA certificates is 0, the returned cmResult is undefined.
      console.info('The count of the user trusted certificates is 0.');
    } else if (cmResult.certList == undefined) {
      console.info('The result of getting current user trusted certificates is undefined.');
    } else {
      let list = cmResult.certList;
      console.info('Succeeded in getting current user trusted certificates.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get current user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get current user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```
