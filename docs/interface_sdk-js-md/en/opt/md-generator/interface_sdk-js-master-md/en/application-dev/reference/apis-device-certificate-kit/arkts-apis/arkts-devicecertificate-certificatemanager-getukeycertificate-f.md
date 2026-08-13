# getUkeyCertificate

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## getUkeyCertificate

```TypeScript
function getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>
```

Obtains the details of a USB Key credential. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>--><!--Device-certificateManager-function getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyUri | string | Yes |
| ukeyInfo | [UkeyInfo](arkts-devicecertificate-certificatemanager-ukeyinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17500011](../errorcode-certManager.md#17500011-failed-to-validate-the-input-parameter) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17500010](../errorcode-certManager.md#17500010-failed-to-access-the-usb-credential) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* Unique identifier of the USB credential. The value is omitted here. */
let ukeyInfo: certificateManager.UkeyInfo = { /* USB credential attributes. The value is omitted here. */
  certPurpose: certificateManager.CertificatePurpose.PURPOSE_DEFAULT,
}
try {
  certificateManager.getUkeyCertificate(keyUri, ukeyInfo).then((cmResult) => {
    let list = cmResult.credentialDetailList;
    console.info('Succeeded in getting detail of USB key certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get detail of USB key certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get detail of USB key certificate. Code: ${error.code}, message: ${error.message}`);
}
```
