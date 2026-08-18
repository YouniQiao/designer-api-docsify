# isInSandbox

## Modules to Import

```TypeScript
```

## isInSandbox

```TypeScript
function isInSandbox(): Promise<boolean>
```

Checks whether this application is running in a DLP sandbox environment. This API uses a promise to return the result. This API is used to determine whether the current application is running in a DLP sandbox environment. If it is, the system can perform operations or call APIs for sandbox applications.

**Since:** 10

<!--Device-dlpPermission-function isInSandbox(): Promise<boolean>--><!--Device-dlpPermission-function isInSandbox(): Promise<boolean>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.isInSandbox().then((isInSandbox) => { // Check whether the application is running in a sandbox.
  console.info('isInSandbox', isInSandbox);
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## isInSandbox

```TypeScript
function isInSandbox(callback: AsyncCallback<boolean>): void
```

Checks whether this application is running in a DLP sandbox environment. This API uses an asynchronous callback to return the result. This API is used to determine whether the current application is running in a DLP sandbox environment. If it is, the system can perform operations or call APIs for sandbox applications.

**Since:** 10

<!--Device-dlpPermission-function isInSandbox(callback: AsyncCallback<boolean>): void--><!--Device-dlpPermission-function isInSandbox(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.isInSandbox((err, isInSandbox) => {
  if (err) {
    console.error('isInSandbox error', err.code, err.message);
  } else {
    console.info('isInSandbox: ', JSON.stringify(isInSandbox));
  }
}); // Whether the application is running in a sandbox.
```
