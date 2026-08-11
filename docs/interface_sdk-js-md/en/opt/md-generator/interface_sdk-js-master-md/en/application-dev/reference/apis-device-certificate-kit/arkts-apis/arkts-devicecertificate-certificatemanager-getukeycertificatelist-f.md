# getUkeyCertificateList

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getUkeyCertificateList

```TypeScript
function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise<CMResult>
```

Obtains the list of USB Key credential . This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise<CMResult>--><!--Device-certificateManager-function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ukeyProvider | string | Yes |
| ukeyInfo | [UkeyInfo](arkts-devicecertificate-certificatemanager-ukeyinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CMResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17500011](../errorcode-certManager.md#17500011-failed-to-validate-the-input-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17500010](../errorcode-certManager.md#17500010-failed-to-access-the-usb-credential) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ukeyProvider: string = 'testProvider'; /* USB credential provider, which is omitted here. */
let ukeyInfo: certificateManager.UkeyInfo = { /* USB credential attributes. The value is omitted here. */
  certPurpose: certificateManager.CertificatePurpose.PURPOSE_DEFAULT,
}
try {
  certificateManager.getUkeyCertificateList(ukeyProvider, ukeyInfo).then((cmResult) => {
    let list: Array<certificateManager.Credential> = cmResult.credentialDetailList ?? [];
    console.info('Succeeded in getting USB key certificate list.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get USB key certificate list. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get USB key certificate list. Code: ${error.code}, message: ${error.message}`);
}
```
