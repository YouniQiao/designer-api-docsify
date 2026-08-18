# getSnapshot（系统接口）

## 导入模块

```TypeScript
```

## getSnapshot

```TypeScript
function getSnapshot(windowId: number): Promise<image.PixelMap>
```

获取指定窗口相同尺寸截图，使用Promise异步回调。若当前窗口设置为隐私模式（可通过 [setWindowPrivacyMode](arkts-arkui-window-window-i.md#setwindowprivacymode) 接口设置），截图结果为白屏。

**起始版本：** 23

<!--Device-window-function getSnapshot(windowId: int): Promise<image.PixelMap>--><!--Device-window-function getSnapshot(windowId: int): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

try {
  // 此处仅示意，请使用getWindowProperties获取对应窗口ID再进行使用
  let windowId: number = 40;
  let promise = window.getSnapshot(windowId);
  promise.then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in getting snapshot window. Pixel bytes number:' + pixelMap.getPixelBytesNumber());
    pixelMap.release();
  }).catch((err: BusinessError) =>{
    console.error(`Failed to get snapshot. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get snapshot. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
