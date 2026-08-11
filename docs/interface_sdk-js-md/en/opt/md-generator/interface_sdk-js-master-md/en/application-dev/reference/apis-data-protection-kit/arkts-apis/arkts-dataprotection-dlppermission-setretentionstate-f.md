# setRetentionState

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setRetentionState

```TypeScript
function setRetentionState(docUris: Array<string>): Promise<void>
```

Sets the retention state for sandbox applications. By default, when a DLP file is opened, the system automatically creates a sandbox environment. After the file is closed, the sandbox is automatically destroyed. After the retention state is set, the sandbox environment is retained even if the DLP file is closed, allowing the system to quickly reopen the same DLP file. This is applicable to scenarios where the same DLP file needs to be frequently operated, improving the file opening efficiency. This API uses a promise to return the result.

**Since:** 10

<!--Device-dlpPermission-function setRetentionState(docUris: Array<string>): Promise<void>--><!--Device-dlpPermission-function setRetentionState(docUris: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| docUris | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100006](../errorcode-dlp.md#19100006-access-denied-for-a-nondlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
dlpPermission.isInSandbox().then(async (inSandbox) => {
  if (inSandbox) {
    await dlpPermission.setRetentionState([uri]); // Set the sandbox retention state.
  }
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
}); // Whether the application is running in a sandbox.
```


## setRetentionState

```TypeScript
function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void
```

Sets the retention state for sandbox applications. By default, when a DLP file is opened, the system automatically creates a sandbox environment. After the file is closed, the sandbox is automatically destroyed. After the retention state is set, the sandbox environment is retained even if the DLP file is closed, allowing the system to quickly reopen the same DLP file. This is applicable to scenarios where the same DLP file needs to be frequently operated, improving the file opening efficiency.

**Since:** 10

<!--Device-dlpPermission-function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void--><!--Device-dlpPermission-function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| docUris | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100006](../errorcode-dlp.md#19100006-access-denied-for-a-nondlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
dlpPermission.isInSandbox().then((inSandbox) => { // Check whether the application is running in a sandbox.
  if (inSandbox) {
    dlpPermission.setRetentionState([uri], (err) => {
      if (err) {
        console.error(`Failed to set retention state. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('setRetentionState success');
      }
    }); // Set the sandbox retention state.
  }
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```
