# WindowStage

Implements a window manager, which manages each basic window unit, that is, [Window](arkts-arkui-window-n.md#window) instance. Before calling any of the following APIs, you must use [onWindowStageCreate()](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate) to create a WindowStage instance.

**Since:** 23

**Deprecated since:** -1

<!--Device-window-interface WindowStage--><!--Device-window-interface WindowStage-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## disableWindowDecor

```TypeScript
disableWindowDecor(): void
```

Disables window decorators. When window decorators are disabled and the main window transitions into full-screen mode, hovering the cursor over the hot zone of the top window's title bar will cause a floating title bar to appear. To prevent the floating title bar from appearing, call [setTitleAndDockHoverShown()](arkts-arkui-window-window-i.md#setTitleAndDockHoverShown).

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-disableWindowDecor(): void--><!--Device-WindowStage-disableWindowDecor(): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
// EntryAbility.ets
import { UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('disableWindowDecor');
    windowStage.disableWindowDecor();
  }
};
```

## removeImageForRecent

```TypeScript
removeImageForRecent(): Promise<void>
```

Removes the image that the application has set to be displayed in the multitasking view and on dock hover. The change will be effective the next time you check the application widget in the multitasking view. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.MANAGE_RECENT_SNAPSHOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-removeImageForRecent(): Promise<void>--><!--Device-WindowStage-removeImageForRecent(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setImageForRecent

```TypeScript
setImageForRecent(imageResource: number | image.PixelMap, value: ImageFit): Promise<void>
```

Sets the image displayed in the multitasking view and on dock hover. This API uses a promise to return the result. > **NOTE：**> > Before calling this API, you are advised to complete page loading via > [loadContent](arkts-arkui-window-window-i.md#loadContent) or > [setUIContent](arkts-arkui-window-window-i.md#setUIContent). If this API is called before the application > completes page loading, the intended functionality does not take effect. As a result, only the application's > launch page is displayed in the multitasking view.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.MANAGE_RECENT_SNAPSHOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-setImageForRecent(imageResource: long | image.PixelMap, value: ImageFit): Promise<void>--><!--Device-WindowStage-setImageForRecent(imageResource: long | image.PixelMap, value: ImageFit): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imageResource | number \| image.PixelMap | Yes |
| value | [ImageFit](arkts-arkui-imagefit-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setImageForRecent

```TypeScript
setImageForRecent(imgResourceId: number, value: ImageFit): Promise<void>
```

Sets the image displayed in the multitasking view. This API uses a promise to return the result.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-setImageForRecent(imgResourceId: number, value: ImageFit): Promise<void>--><!--Device-WindowStage-setImageForRecent(imgResourceId: number, value: ImageFit): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| imgResourceId | number | Yes |
| value | [ImageFit](arkts-arkui-imagefit-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    let imgResourceId = $r("app.media.startIcon").id
    try {
      let promise = windowStage.setImageForRecent(imgResourceId, ImageFit.Fill);
      promise.then(() => {
        console.info(`Succeeded in setting image for recent`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to set image for recent. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set image for recent.`);
    }
  }
};
```

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(showOnLockScreen: boolean): void
```

Sets whether to display the window of the application on the lock screen.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-setShowOnLockScreen(showOnLockScreen: boolean): void--><!--Device-WindowStage-setShowOnLockScreen(showOnLockScreen: boolean): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| showOnLockScreen | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      windowStage.setShowOnLockScreen(true);
    } catch (exception) {
      console.error(`Failed to show on lockscreen. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
};
```
