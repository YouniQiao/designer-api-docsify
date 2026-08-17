# setPointerStyle

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## setPointerStyle

```TypeScript
function setPointerStyle(windowId: int, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void
```

Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcursor). This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function setPointerStyle(windowId: int, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void--><!--Device-pointer-function setPointerStyle(windowId: int, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | Window ID. The value is an integer greater than or equal to 0. <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be set properly. <br>If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly. <br>The result can be obtained through [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getpointerstyle). |
| pointerStyle | PointerStyle | Yes | Pointer style. Do not pass **DEVELOPER_DEFINED_ICON**. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. <br> When the windowId value is -1, the system permission is required to set the global style. |

**Examples**

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS, error => {
                console.info(`Set pointer style success`);
              });
            } catch (error) {
              console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```


## setPointerStyle

```TypeScript
function setPointerStyle(windowId: int, pointerStyle: PointerStyle): Promise<void>
```

Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of windows within the current application process. For details about how to set the mouse pointer style type of the host window through the **UIExtensionAbility** process, see [setCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setcursor). This uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function setPointerStyle(windowId: int, pointerStyle: PointerStyle): Promise<void>--><!--Device-pointer-function setPointerStyle(windowId: int, pointerStyle: PointerStyle): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | Window ID. The value is an integer greater than or equal to 0. <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be set properly. <br>If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly. <br>The result can be obtained through [getPointerStyle](arkts-input-pointer-getpointerstyle-f.md#getpointerstyle). |
| pointerStyle | PointerStyle | Yes | Pointer style. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. <br> When the windowId value is -1, the system permission is required to set the global style. |

**Examples**

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS).then(() => {
                console.info(`Set pointer style success`);
              }).catch((error: BusinessError) => {
               console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
            } catch (error) {
              console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

