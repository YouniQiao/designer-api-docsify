# getPrivateCertificates

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getPrivateCertificates

```TypeScript
function getPrivateCertificates(): Promise<CMResult>
```

Obtains the credentials for installing the application. This API uses a promise to return the result asynchronously.

**Since:** 13

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**System capability:** SystemCapability.Security.CertificateManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
