# getPointerStyle

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## getPointerStyle

```TypeScript
function getPointerStyle(windowId: int, callback: AsyncCallback<PointerStyle>): void
```

Obtains the mouse pointer style type of a specified window. This API can obtain only the mouse pointer style type of windows within the current application process. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-pointer-function getPointerStyle(windowId: int, callback: AsyncCallback<PointerStyle>): void--><!--Device-pointer-function getPointerStyle(windowId: int, callback: AsyncCallback<PointerStyle>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | Window ID. The value is an integer greater than or equal to **-1**. The value **-1** indicates the global window. <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is returned. <br>If the window ID is valid but the window does not exist, the global mouse pointer style is returned by default. <br>If the mouse pointer style is set for a non-existent window through [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md), this API can obtain the mouse pointer style properly. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PointerStyle&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the mouse pointer style type. Otherwise, **err** is an error object. In specific scenarios (obtaining the style on a window with a custom pointer style), **DEVELOPER_DEFINED_ICON** is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

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
              pointer.getPointerStyle(windowId, (error: BusinessError, style: pointer.PointerStyle) => {
                console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
              });
            } catch (error) {
              console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```

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
              pointer.getPointerStyle(windowId).then((style: pointer.PointerStyle) => {
                console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
              }).catch((error: BusinessError) => {
                console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
            } catch (error) {
              console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        })
    }
  }
}
```


## getPointerStyle

```TypeScript
function getPointerStyle(windowId: int): Promise<PointerStyle>
```

Obtains the mouse pointer style type. This API can obtain only the mouse pointer style type of windows within the current application process. This API uses a promise to return the result.

**Since:** 23

<!--Device-pointer-function getPointerStyle(windowId: int): Promise<PointerStyle>--><!--Device-pointer-function getPointerStyle(windowId: int): Promise<PointerStyle>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | Window ID. The value is an integer greater than or equal to **-1**. The value **-1** indicates the global window. <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is returned. <br>If the window ID is valid but the window does not exist, the global mouse pointer style is returned by default. <br>If the mouse pointer style is set for a non-existent window through [setPointerStyle](arkts-input-pointer-setpointerstyle-f.md), this API can obtain the mouse pointer style properly. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PointerStyle&gt; | Promise object, which is used to return the mouse pointer style. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

See [getPointerStyle](#getpointerstyle)

