# WindowProxy

The proxy of the UIExtension window.

**Since:** 12

<!--Device-uiExtension-interface WindowProxy--><!--Device-uiExtension-interface WindowProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiExtension } from 'kits/@kit.ArkUI';
```

## hideNonSecureWindows

```TypeScript
hideNonSecureWindows(shouldHide: boolean): Promise<void>
```

Sets whether to hide non-secure windows. This API uses a promise to return the result.

> **NOTE：**
> 
> - A non-secure window refers to any window that may obstruct the
> [EmbeddedComponent](../../apis-arkui/arkts-components/arkts-arkui-embedded_component-i) or
> [UIExtensionComponent](../../apis-arkui/arkts-components/arkts-arkui-ui_extension_component-i), such as global floating windows
> , host subwindows, and dialog box windows created by the host application (excluding windows of these types
> created by system applications).
> 
> - When using the **EmbeddedComponent** or **UIExtensionComponent** to display sensitive information, call this
> API to hide non-secure windows and prevent information obstruction. Hidden non-secure windows will reappear
> when the **EmbeddedComponent** or **UIExtensionComponent** is hidden or destroyed.
> 
> - On PCs/2-in-1 devices, global floating windows within non-secure windows remain visible when
> **hideNonSecureWindows(true)** is called.

**Since:** 12

**Required permissions:** ohos.permission.ALLOW_SHOW_NON_SECURE_WINDOWS

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowProxy-hideNonSecureWindows(shouldHide: boolean): Promise<void>--><!--Device-WindowProxy-hideNonSecureWindows(shouldHide: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shouldHide | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
// ExtensionProvider.ets

import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Hide non-secure windows.
    extensionHostWindow.hideNonSecureWindows(true).then(()=> {
      console.info(`Succeeded in hiding the non-secure windows.`);
    }).catch((err: BusinessError)=> {
      console.error(`Failed to hide the non-secure windows. Cause:${JSON.stringify(err)}`);
    });
  }
  
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Unhide non-secure windows.
    extensionHostWindow.hideNonSecureWindows(false).then(()=> {
      console.info(`Succeeded in showing the non-secure windows.`);
    }).catch((err: BusinessError)=> {
      console.error(`Failed to show the non-secure windows. Cause:${JSON.stringify(err)}`);
    });
  }
}
```

## setWaterMarkFlag

```TypeScript
setWaterMarkFlag(enable: boolean): Promise<void>
```

Adds or deletes the watermark flag for this window. This API uses a promise to return the result.

> **NOTE：**
> 
> With the watermark flag added, the watermark is applied on the full screen when the window is in the foreground
> , regardless of whether the window is displayed in full screen, floating, and split screen mode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowProxy-setWaterMarkFlag(enable: boolean): Promise<void>--><!--Device-WindowProxy-setWaterMarkFlag(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |

## Examples

```TypeScript
// ExtensionProvider.ets
import { UIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Add the watermark flag.
    extensionHostWindow.setWaterMarkFlag(true).then(() => {
      console.info(`Succeeded in setting water mark flag of window.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to set water mark flag of window. Cause:${JSON.stringify(err)}`);
    });
  }
  onSessionDestroy(session: UIExtensionContentSession) {
    const extensionHostWindow = session.getUIExtensionHostWindowProxy();
    // Delete the watermark flag.
    extensionHostWindow.setWaterMarkFlag(false).then(() => {
      console.info(`Succeeded in deleting water mark flag of window.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to delete water mark flag of window. Cause:${JSON.stringify(err)}`);
    });
  }
}
```
