# init

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## init

```TypeScript
function init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void
```

Indicates the initialization of signature and signature verification using credentials. This is the first step in the signature verification process. Later, the update and finish interfaces need to be invoked in sequence to complete the operations. Use Callback to return the result asynchronously.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void--><!--Device-certificateManager-function init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authUri | string | Yes |
| spec | [CMSignatureSpec](arkts-devicecertificate-certificatemanager-cmsignaturespec-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CMHandle&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
| [17500005](../errorcode-certManager.md#17500005-application-not-authorized) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';

let uri: string = 'test'; /* The service needs to use the unique identifier of the credential to initialize signing and signature verification, which is not elaborated here. */
const req: certificateManager.CMSignatureSpec = {
  purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_SIGN,
  padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
  digest: certificateManager.CmKeyDigest.CM_DIGEST_SHA256
}
try {
  certificateManager.init(uri, req, (err, cmHandle) => {
    if (err != null) {
      console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in initiating.');
    }
  })
} catch (error) {
  console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
}
```


## init

```TypeScript
function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>
```

Initializes the signing or signature verification operation using the specified credential. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>--><!--Device-certificateManager-function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authUri | string | Yes |
| spec | [CMSignatureSpec](arkts-devicecertificate-certificatemanager-cmsignaturespec-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CMHandle&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
| [17500005](../errorcode-certManager.md#17500005-application-not-authorized) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* The service needs to use the unique identifier of the credential to initialize signing and signature verification, which is not elaborated here. */
const req: certificateManager.CMSignatureSpec = {
  purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_VERIFY,
  padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
  digest: certificateManager.CmKeyDigest.CM_DIGEST_MD5
}
try {
  certificateManager.init(uri, req).then((handle) => {
    console.info('Succeeded in initiating.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
}
```
