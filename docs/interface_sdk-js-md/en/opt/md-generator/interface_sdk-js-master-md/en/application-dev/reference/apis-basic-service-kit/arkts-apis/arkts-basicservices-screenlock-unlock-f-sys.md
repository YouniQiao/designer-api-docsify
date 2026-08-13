# unlock (System API)

## Modules to Import

```TypeScript
import { screenLock } from '@kit.BasicServicesKit';
```

## unlock

```TypeScript
function unlock(callback: AsyncCallback<boolean>): void
```

Unlock the screen.

**Since:** 23

**Deprecated since:** -1

<!--Device-screenLock-function unlock(callback: AsyncCallback<boolean>): void--><!--Device-screenLock-function unlock(callback: AsyncCallback<boolean>): void-End-->

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200003](../../apis-basic-services-kit/errorcode-screenlock.md#13200003-invalid-use) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

screenLock.unlock((err: BusinessError, data: Boolean) => {
  if (err) {
    console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in unlocking the screen. result: ${data}`);
});
```


## unlock

```TypeScript
function unlock(): Promise<boolean>
```

Unlock the screen.

**Since:** 23

**Deprecated since:** -1

<!--Device-screenLock-function unlock(): Promise<boolean>--><!--Device-screenLock-function unlock(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200003](../../apis-basic-services-kit/errorcode-screenlock.md#13200003-invalid-use) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

screenLock.unlock().then((data: Boolean) => {
  console.info(`Succeeded in unlocking the screen. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
});
```
