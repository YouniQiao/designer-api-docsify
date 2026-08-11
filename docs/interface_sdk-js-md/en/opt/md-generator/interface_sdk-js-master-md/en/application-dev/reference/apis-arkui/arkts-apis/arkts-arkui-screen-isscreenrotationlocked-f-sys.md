# isScreenRotationLocked (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## isScreenRotationLocked

```TypeScript
function isScreenRotationLocked(callback: AsyncCallback<boolean>): void
```

Checks whether auto rotate is locked. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-screen-function isScreenRotationLocked(callback: AsyncCallback<boolean>): void--><!--Device-screen-function isScreenRotationLocked(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Check whether auto screen rotation is locked.
screen.isScreenRotationLocked((err: BusinessError, isLocked: boolean) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to get the screen rotation lock status. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting the screen rotation lock status. isLocked: ${isLocked}`);
});
```


## isScreenRotationLocked

```TypeScript
function isScreenRotationLocked(): Promise<boolean>
```

Checks whether auto rotate is locked. This API uses a promise to return the result.

**Since:** 9

<!--Device-screen-function isScreenRotationLocked(): Promise<boolean>--><!--Device-screen-function isScreenRotationLocked(): Promise<boolean>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Check whether auto screen rotation is locked.
screen.isScreenRotationLocked().then((isLocked: boolean) => {
  console.info(`Succeeded in getting the screen rotation lock status. isLocked: ${isLocked}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get the screen rotation lock status. Code: ${err.code}, message: ${err.message}`);
});
```
