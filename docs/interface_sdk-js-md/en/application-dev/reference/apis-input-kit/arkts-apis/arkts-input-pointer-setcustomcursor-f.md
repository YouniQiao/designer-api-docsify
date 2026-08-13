# setCustomCursor

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setCustomCursor

```TypeScript
function setCustomCursor(windowId: int, pixelMap: image.PixelMap, focusX?: int, focusY?: int): Promise<void>
```

Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCustomCursor). This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function setCustomCursor(windowId: int, pixelMap: image.PixelMap, focusX?: int, focusY?: int): Promise<void>--><!--Device-pointer-function setCustomCursor(windowId: int, pixelMap: image.PixelMap, focusX?: int, focusY?: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | Window ID. |
| pixelMap | image.PixelMap | Yes | Custom cursor resource. |
| focusX | int | No | Custom cursor focus X, in px. The value must be greater than or equal to 0. The default value is **0**. |
| focusY | int | No | Custom cursor focus Y, in px. The value must be greater than or equal to 0. The default value is **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon is an example resource. Configure the resource file based on the actual requirements.
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, pixelMap).then(() => {
                    console.info(`setCustomCursor success`);
                  });
                } catch (error) {
                  console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            }).catch((error: BusinessError) => {
                console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
          });
        })
    }
  }
}
```


## setCustomCursor

```TypeScript
function setCustomCursor(windowId: int, cursor: CustomCursor, config: CursorConfig): Promise<void>
```

Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCustomCursor). This API uses a promise to return the result. The cursor may be switched back to the system style in the following cases: application window layout change, hot zone switching, page redirection, moving of the cursor out of the window and then back to the window, or moving of the cursor in different areas of the window. In this case, you need to reset the cursor style.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-pointer-function setCustomCursor(windowId: int, cursor: CustomCursor, config: CursorConfig): Promise<void>--><!--Device-pointer-function setCustomCursor(windowId: int, cursor: CustomCursor, config: CursorConfig): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | Window ID. |
| cursor | [CustomCursor](arkts-input-pointer-customcursor-i.md) | Yes | Custom cursor resource. |
| config | [CursorConfig](arkts-input-pointer-cursorconfig-i.md) | Yes | Custom cursor configuration, which specifies whether to adjust the cursor size based on system settings. If **followSystem** in **CursorConfig** is set to **true**, the supported adjustment range is [size of the cursor image, 256 x 256]. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Abnormal windowId parameter passed in; &lt;br&gt;2. Abnormal pixelMap parameter passed in; 3. Abnormal focusX parameter passed in; &lt;br&gt;4. Abnormal focusY parameter passed in. |
| [26500001](../errorcode-pointer.md#26500001-invalid-window-id) | Invalid windowId. Possible causes: The window id does not belong to the current process. |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // app_icon is an example resource. Configure the resource file based on the actual requirements.
          this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
            $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
            const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
            let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
            let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, { pixelMap: pixelMap, focusX: 25, focusY: 25 },
                    { followSystem: false }).then(() => {
                    console.info(`setCustomCursor success`);
                  });
                } catch (error) {
                  console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                }
              });
            }).catch((error: BusinessError) => {
                console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
              });
          });
        })
    }
  }
}
```

