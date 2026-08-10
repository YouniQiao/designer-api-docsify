# moveMainWindowToTargetDisplay (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## moveMainWindowToTargetDisplay

```TypeScript
function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>
```

将指定的主窗口迁移到指定的屏幕上。使用Promise异步回调。

- 对于[主屏](../../../displaymanager/display-terminology.md#主屏)/  
[扩展屏](../../../displaymanager/display-terminology.md#扩展屏)与  
[虚拟屏](../../../displaymanager/display-terminology.md#虚拟屏)之间以及虚拟屏与虚拟屏之间的窗口迁移，仅主窗及其子窗会一起被迁移到对应屏幕上且被抬升，如果存在子窗，最上层可获焦子窗会获取焦点，否则主窗口获焦。  
- 对于主屏与扩展屏之间的窗口迁移，只会将主窗口迁移到对应屏幕，抬升并获取焦点。

&lt;!--RP3--&gt;&lt;!--RP3End--&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-window-function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>--><!--Device-window-function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 目标屏幕的ID，用于指定要迁移到的屏幕。该参数应为非负整数，可通过 [getWindowProperties](arkts-arkui-window-window-i.md#getwindowproperties)接口获取到 [properties](arkts-arkui-window-windowproperties-i.md)后，再通过properties.displayId获取；也可通过获取 [Display](arkts-arkui-display-displaystate-e.md)对象的 [id](../../../reference/apis-arkui/js-apis-display.md#属性)属性获取此参数。 |
| windowId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标主窗口的ID，用于指定要迁移的窗口。该参数应为大于0的整数，通过 [getWindowProperties](arkts-arkui-window-window-i.md#getwindowproperties)接口获取到 [properties](arkts-arkui-window-windowproperties-i.md)后，再通过properties.id获取。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not found or has been destroyed. |
| 1300016 | Parameter error. Possible cause: 1. The userId is not exist. |
| 1300004 | Unauthorized operation. Possible cause: The window is not a main window. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 1300008 | Invalid display. Possible cause: 1. DisplayId is a negative number or not exists. |

## Examples

```TypeScript
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { display, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      if (err.code) {
        console.error(`Failed to load content for main window. Cause code: ${err.code}, message: ${err.message}`);
      }
      let displayClass: display.Display | null = null;
      displayClass = display.getDefaultDisplaySync();
      let mainWindow = windowStage.getMainWindowSync();
      try {
        window.moveMainWindowToTargetDisplay(displayClass.id, mainWindow.getWindowProperties().id).then(() => {
          console.info(`Succeeded in moving window id: ${mainWindow.getWindowProperties().id} to target display id: ${mainWindow.getWindowProperties().displayId}`);
        }).catch((err: BusinessError) => {
          console.error(`Failed to move window to target display. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to move window to target display. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
}
```

