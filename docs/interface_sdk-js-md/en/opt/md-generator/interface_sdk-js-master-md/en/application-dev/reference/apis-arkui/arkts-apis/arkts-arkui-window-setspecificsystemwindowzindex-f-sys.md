# setSpecificSystemWindowZIndex (System API)

## Modules to Import

```TypeScript
```

## setSpecificSystemWindowZIndex

```TypeScript
function setSpecificSystemWindowZIndex(windowType: WindowType, zIndex: number): Promise<void>
```

Sets the z-level of a system window. This API uses a promise to return the result. Adjusts the **zIndex** of all system windows of the specified type to the configured value. Before and after the adjustment, the relative z-level of these windows remains unchanged, and the focus window does not change. After the application is closed, the z-level of specified windows is restored to the default value. You are advised to set different **zIndex** values for different types of windows. If there are windows with the same **zIndex**, the relative z-level of windows remains unchanged before and after the setting.

**Since:** 23

<!--Device-window-function setSpecificSystemWindowZIndex(windowType: WindowType, zIndex: int): Promise<void>--><!--Device-window-function setSpecificSystemWindowZIndex(windowType: WindowType, zIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowType | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | Yes |
| zIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  window.setSpecificSystemWindowZIndex(window.WindowType.TYPE_WALLET_SWIPE_CARD, 200).then(() => {
    console.info('Succeeded in setting zIndex');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set zIndex. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to set zIndex. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
