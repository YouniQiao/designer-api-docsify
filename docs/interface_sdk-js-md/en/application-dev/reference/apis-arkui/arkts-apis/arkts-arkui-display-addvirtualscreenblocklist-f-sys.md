# addVirtualScreenBlocklist (System API)

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## addVirtualScreenBlocklist

```TypeScript
function addVirtualScreenBlocklist(windowIds: Array<int>): Promise<void>
```

将窗口添加到禁止投屏显示的名单中，被添加的窗口无法在投屏时显示。仅对应用主窗或系统窗口生效。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-display-function addVirtualScreenBlocklist(windowIds: Array<int>): Promise<void>--><!--Device-display-function addVirtualScreenBlocklist(windowIds: Array<int>): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowIds | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | 窗口id列表，传入子窗窗口id时不生效。窗口id为大于0的整数。推荐使用 [getWindowProperties()](../../../reference/apis-arkui/arkts-apis-window-Window.md#getwindowproperties9)方法获取窗口 id属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. Function addVirtualScreenBlocklist can not work correctly due to limited device capabilities. |
| 1400003 | This display manager service works abnormally. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { display, window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage) {
    // ...
    let windowId = windowStage.getMainWindowSync().getWindowProperties().id; // Obtain the window IDs.
    let windowIds = [windowId];

    // Add windows to the list of windows that are not allowed to be displayed during casting.
    let promise = display.addVirtualScreenBlocklist(windowIds);
    promise.then(() => {
      console.info('Succeeded in adding virtual screen blocklist.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to add virtual screen blocklist. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

