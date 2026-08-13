# sendScreenLockEvent (System API)

## Modules to Import

```TypeScript
import { screenLock } from '@kit.BasicServicesKit';
```

## sendScreenLockEvent

```TypeScript
function sendScreenLockEvent(event: String, parameter: number, callback: AsyncCallback<boolean>): void
```

The screen lock app sends the event to the screen lock service.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int, callback: AsyncCallback<boolean>): void--><!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | String | Yes |
| parameter | number | Yes |
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

screenLock.sendScreenLockEvent('unlockScreenResult', 0, (err: BusinessError, result: Boolean) => {
  if (err) {
    console.error(`Failed to send screenlock event, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in Sending screenlock event. result: ${result}`);
});
```


## sendScreenLockEvent

```TypeScript
function sendScreenLockEvent(event: String, parameter: number): Promise<boolean>
```

The screen lock app sends the event to the screen lock service.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int): Promise<boolean>--><!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | String | Yes |
| parameter | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

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

screenLock.sendScreenLockEvent('unlockScreenResult', 0).then((result: Boolean) => {
  console.info(`Succeeded in Sending screenlock event. result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to send screenlock event, Code: ${err.code}, message: ${err.message}`);
});
```
