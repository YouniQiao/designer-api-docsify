# setCustomCursor

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setCustomCursor

```TypeScript
function setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>
```

Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCustomCursor). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function setCustomCursor(windowId: int, pixelMap: image.PixelMap, focusX?: int, focusY?: int): Promise<void>--><!--Device-pointer-function setCustomCursor(windowId: int, pixelMap: image.PixelMap, focusX?: int, focusY?: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |
| pixelMap | image.PixelMap | Yes |
| [focusX](arkts-input-pointer-customcursor-i.md) | number | No |
| [focusY](arkts-input-pointer-customcursor-i.md) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

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
            // Create a PixelMap
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  pointer.setCustomCursor(windowId, pixelMap).then(() => {
                    console.info(`Succeeded in setting custom cursor.`);
                  });
                } catch (error) {
                  console.error(`Failed to set custom cursor, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                }
              });
            }).catch((error: BusinessError) => {
                console.error(`Failed to create pixel map promise, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              });
          });
        })
    }
  }
}
```


## setCustomCursor

```TypeScript
function setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>
```

Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows within the current application process. For details about how to set the custom pointer style of the host window through the **UIExtensionAbility** process, see [setCustomCursor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md#setCustomCursor). This API uses a promise to return the result. The cursor may be switched back to the system style in the following cases: application window layout change, hot zone switching, page redirection, moving of the cursor out of the window and then back to the window, or moving of the cursor in different areas of the window. In this case, you need to reset the cursor style.

**Since:** 23

**Deprecated since:** -1

<!--Device-pointer-function setCustomCursor(windowId: int, cursor: CustomCursor, config: CursorConfig): Promise<void>--><!--Device-pointer-function setCustomCursor(windowId: int, cursor: CustomCursor, config: CursorConfig): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |
| cursor | [CustomCursor](arkts-input-pointer-customcursor-i.md) | Yes |
| config | [CursorConfig](arkts-input-pointer-cursorconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [26500001](../errorcode-pointer.md#26500001-invalid-window-id) |

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
            // Create a PixelMap
            svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
              // Get the most recent window within the application
              window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
                let windowId = win.getWindowProperties().id;
                try {
                  // Set a custom pointer
                  pointer.setCustomCursor(windowId, { pixelMap: pixelMap, focusX: 25, focusY: 25 },
                    { followSystem: false }).then(() => {
                    console.info(`Succeeded in setting custom cursor.`);
                  });
                } catch (error) {
                  console.error(`Failed to set custom cursor, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                }
              });
            }).catch((error: BusinessError) => {
                console.error(`Failed to create pixel map promise, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              });
          });
        })
    }
  }
}
```
