# toggleShownStateForAllAppWindows (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## toggleShownStateForAllAppWindows

```TypeScript
function toggleShownStateForAllAppWindows(callback: AsyncCallback<void>): void
```

多窗口快速切换时隐藏或者恢复应用窗口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-window-function toggleShownStateForAllAppWindows(callback: AsyncCallback<void>): void--><!--Device-window-function toggleShownStateForAllAppWindows(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

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

多窗口快速切换时隐藏或者恢复应用窗口，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-window-function toggleShownStateForAllAppWindows(): Promise<void>--><!--Device-window-function toggleShownStateForAllAppWindows(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

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

