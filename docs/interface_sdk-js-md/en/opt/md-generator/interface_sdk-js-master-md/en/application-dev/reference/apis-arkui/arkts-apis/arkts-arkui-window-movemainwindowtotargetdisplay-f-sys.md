# moveMainWindowToTargetDisplay (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## moveMainWindowToTargetDisplay

```TypeScript
function moveMainWindowToTargetDisplay(displayId: number, windowId: number, userId?: number): Promise<void>
```

Move a window to the target display. The window must be a main window.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-window-function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>--><!--Device-window-function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |
| windowId | number | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |

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
