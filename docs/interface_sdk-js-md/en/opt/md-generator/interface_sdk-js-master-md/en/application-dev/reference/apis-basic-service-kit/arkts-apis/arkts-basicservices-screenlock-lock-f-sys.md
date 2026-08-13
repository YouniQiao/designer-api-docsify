# lock (System API)

## Modules to Import

```TypeScript
import { screenLock } from '@kit.BasicServicesKit';
```

## lock

```TypeScript
function lock(callback: AsyncCallback<boolean>): void
```

Lock the screen.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function lock(callback: AsyncCallback<boolean>): void--><!--Device-screenLock-function lock(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

screenLock.lock((err: BusinessError, data: Boolean) => {
  if (err) {
    console.error(`Failed to lock the screen, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in locking the screen. result: ${data}`);
});
```


## lock

```TypeScript
function lock(): Promise<boolean>
```

Lock the screen.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function lock(): Promise<boolean>--><!--Device-screenLock-function lock(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

screenLock.lock().then((data: Boolean) => {
  console.info(`Succeeded in locking the screen. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to lock the screen, Code: ${err.code}, message: ${err.message}`);
});
```
