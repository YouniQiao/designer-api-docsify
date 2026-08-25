# setCustomCursorSync

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## setCustomCursorSync

```TypeScript
function setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void
```

设置指定窗口的自定义光标样式，使用同步方式进行设置。此接口仅支持设置本应用进程内窗口的自定义光标样式，如需通过UIExtensionAbility进程设置宿主窗口的自定义光标样式，请参阅 [setCustomCursor](../../../reference/apis-arkui/arkts-apis-uicontext-cursorcontroller.md#setcustomcursor)。应用窗口布局改变、热区切换、页面跳转、光标移出再回到窗口、光标在窗口不同区域移动， 以上场景可能导致光标切换回系统样式，需要开发者重新设置光标样式。

**起始版本：** 11

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| pixelMap | image.PixelMap | 是 |
| [focusX](arkts-input-pointer-customcursor-i.md) | number | 否 |
| [focusY](arkts-input-pointer-customcursor-i.md) | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
