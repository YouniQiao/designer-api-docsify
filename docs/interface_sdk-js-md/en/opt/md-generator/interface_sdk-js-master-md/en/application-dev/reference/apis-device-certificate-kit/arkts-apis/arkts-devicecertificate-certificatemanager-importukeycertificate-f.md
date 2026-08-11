# importUkeyCertificate

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## importUkeyCertificate

```TypeScript
function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>
```

Import the certificate to the USB Key.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>--><!--Device-certificateManager-function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyUri | string | Yes |
| cert | Uint8Array | Yes |
| ukeyInfo | [UkeyInfo](arkts-devicecertificate-certificatemanager-ukeyinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17500011](../errorcode-certManager.md#17500011-failed-to-validate-the-input-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17500010](../errorcode-certManager.md#17500010-failed-to-access-the-usb-credential) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* keyUri and cert must be assigned based on the service. The data in this example is for reference only. */
let keyUri: string = 'test'; /* URI of the USB key certificate, which can be obtained using the getUkeyCertificateList API. */
let certData: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let ukeyInfo: certificateManager.UkeyInfo = {
  certPurpose: certificateManager.CertificatePurpose.PURPOSE_SIGN,
};
try {
  certificateManager.importUkeyCertificate(keyUri, certData, ukeyInfo).then(() => {
    console.info('Succeeded in importing USB key certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to import USB key certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to import USB key certificate. Code: ${error.code}, message: ${error.message}`);
}
```
