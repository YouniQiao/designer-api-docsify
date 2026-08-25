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

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authUri | string | Yes |
| spec | [CMSignatureSpec](arkts-devicecertificate-certificatemanager-cmsignaturespec-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CMHandle](arkts-devicecertificate-certificatemanager-cmhandle-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [17500005](../errorcode-certManager.md#17500005-application-not-authorized) |


## init

```TypeScript
function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>
```

Initializes the signing or signature verification operation using the specified credential. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authUri | string | Yes |
| spec | [CMSignatureSpec](arkts-devicecertificate-certificatemanager-cmsignaturespec-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CMHandle](arkts-devicecertificate-certificatemanager-cmhandle-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [17500005](../errorcode-certManager.md#17500005-application-not-authorized) |
