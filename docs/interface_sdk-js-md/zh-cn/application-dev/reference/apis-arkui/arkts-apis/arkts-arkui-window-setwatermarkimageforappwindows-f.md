# setWatermarkImageForAppWindows

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## setWatermarkImageForAppWindows

```TypeScript
function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>
```

设置或取消本应用进程下窗口的水印图片，使用Promise异步回调。该接口需要在 [loadContent()](arkts-arkui-window-window-i.md#loadcontent) 或[setUIContent()](arkts-arkui-window-window-i.md#setuicontent)调用生效后使 用。

**起始版本：** 21

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
