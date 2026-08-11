# onSystemEvent (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## onSystemEvent

```TypeScript
function onSystemEvent(callback: Callback<SystemEvent>): boolean
```

Register system event related to screen lock service.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function onSystemEvent(callback: Callback<SystemEvent>): boolean--><!--Device-screenLock-function onSystemEvent(callback: Callback<SystemEvent>): boolean-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SystemEvent&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSuccess = screenLock.onSystemEvent((event: screenLock.SystemEvent) => {
    console.info(`Succeeded in Registering the system event which related to screenlock. eventType: ${event.eventType}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to register the system event which related to screenlock, Code: ${error.code}, message: ${error.message}`);
}
```
