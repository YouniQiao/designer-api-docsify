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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-screenLock-function unlock(callback: AsyncCallback<boolean>): void--><!--Device-screenLock-function unlock(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | the callback of unlock. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |
| [13200003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-screenlock.md#13200003-invalid-use) | Invalid use. |
| [13200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) | the screenlock management service is abnormal. |

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-screenLock-function unlock(): Promise<boolean>--><!--Device-screenLock-function unlock(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |
| [13200003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-screenlock.md#13200003-invalid-use) | Invalid use. |
| [13200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) | the screenlock management service is abnormal. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

screenLock.unlock().then((data: Boolean) => {
  console.info(`Succeeded in unlocking the screen. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
});
```

