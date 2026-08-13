# setWatermarkImageForAppWindows

## setWatermarkImageForAppWindows

```TypeScript
function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>
```

设置或取消本应用进程下窗口的水印图片，使用Promise异步回调。该接口需要在 [loadContent()](arkts-arkui-window-window-i.md#loadContent) 或[setUIContent()](arkts-arkui-window-window-i.md#setUIContent)调用生效后使 用。

**起始版本：** 23

**废弃版本：** -1

<!--Device-window-function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>--><!--Device-window-function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>-End-->

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## 示例

```TypeScript
import { image } from "@kit.ImageKit";
import { BusinessError } from "@kit.BasicServicesKit";

let color: ArrayBuffer = new ArrayBuffer(96);
let initializationOptions: image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.RGBA_8888,
  size: {
    height: 4,
    width: 6,
  },
};
image.createPixelMap(color, initializationOptions).then((pixelMap: image.PixelMap) => {
  console.info("Succeeded in creating pixelmap.");
  try {
    let promise = window.setWatermarkImageForAppWindows(pixelMap);
    promise.then(() => {
        console.info("Succeeded in setting watermark image.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to set watermark image. Cause code: ${err.code}, message: ${err.message}`);
    });
  } catch (exception) {
    console.error(`Failed to set watermark image. Exception code: ${exception.code}, message: ${exception.message}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to create PixelMap. Cause code: ${err.code}, message: ${err.message}`);
});
```
