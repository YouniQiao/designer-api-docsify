# toggleShownStateForAllAppWindows (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## toggleShownStateForAllAppWindows

```TypeScript
function toggleShownStateForAllAppWindows(callback: AsyncCallback<void>): void
```

Hides or restores the application's windows during quick multi-window switching. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-window-function toggleShownStateForAllAppWindows(callback: AsyncCallback<void>): void--><!--Device-window-function toggleShownStateForAllAppWindows(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

window.toggleShownStateForAllAppWindows((err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to toggle shown state for all app windows. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in toggling shown state for all app windows.');
});
```


## toggleShownStateForAllAppWindows

```TypeScript
function toggleShownStateForAllAppWindows(): Promise<void>
```

Hides or restores the application's windows during quick multi-window switching. This API uses a promise to return the result.

**Since:** 9

<!--Device-window-function toggleShownStateForAllAppWindows(): Promise<void>--><!--Device-window-function toggleShownStateForAllAppWindows(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = window.toggleShownStateForAllAppWindows();
promise.then(() => {
  console.info('Succeeded in toggling shown state for all app windows.');
}).catch((err: BusinessError) => {
  console.error(`Failed to toggle shown state for all app windows. Cause code: ${err.code}, message: ${err.message}`);
});
```
