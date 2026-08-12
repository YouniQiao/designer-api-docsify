# sendScreenLockEvent (System API)

## Modules to Import

```TypeScript
import { screenLock } from '@kit.BasicServicesKit';
```

## sendScreenLockEvent

```TypeScript
function sendScreenLockEvent(event: String, parameter: int, callback: AsyncCallback<boolean>): void
```

The screen lock app sends the event to the screen lock service.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int, callback: AsyncCallback<boolean>): void--><!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | String | Yes | event type. |
| parameter | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | operation result of the event. |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | the callback of sendScreenLockEvent. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |
| [13200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) | the screenlock management service is abnormal. |

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
function sendScreenLockEvent(event: String, parameter: int): Promise<boolean>
```

The screen lock app sends the event to the screen lock service.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int): Promise<boolean>--><!--Device-screenLock-function sendScreenLockEvent(event: String, parameter: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | String | Yes | event type. |
| parameter | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | operation result of the event. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |
| [13200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) | the screenlock management service is abnormal. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

screenLock.sendScreenLockEvent('unlockScreenResult', 0).then((result: Boolean) => {
  console.info(`Succeeded in Sending screenlock event. result: ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to send screenlock event, Code: ${err.code}, message: ${err.message}`);
});
```

