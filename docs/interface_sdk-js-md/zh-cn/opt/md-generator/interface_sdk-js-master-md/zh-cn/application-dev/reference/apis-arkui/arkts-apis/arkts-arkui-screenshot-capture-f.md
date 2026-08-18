# capture

## 导入模块

```TypeScript
```

## capture

```TypeScript
function capture(options?: CaptureOption): Promise<image.PixelMap>
```

获取屏幕全屏截图，使用Promise异步回调。 此接口可以通过设置不同的displayId截取不同屏幕的截图，且只能截取全屏；[pick](arkts-arkui-screenshot-pick-f.md#pick)接口可实现区域截屏。

**起始版本：** 23

**需要权限：** 
- API版本22+：ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本14 - 21：ohos.permission.CUSTOM_SCREEN_CAPTURE

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-screenshot-function capture(options?: CaptureOption): Promise<image.PixelMap>--><!--Device-screenshot-function capture(options?: CaptureOption): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CaptureOption](arkts-arkui-screenshot-captureoption-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// 配置截图参数，指定截取displayId为0的屏幕
let captureOption: screenshot.CaptureOption = {
  displayId: 0
};
try {
  // 调用capture接口获取全屏截图
  let promise = screenshot.capture(captureOption);
  promise.then((pixelMap: image.PixelMap) => {
    console.info(`Succeeded in saving screenshot. Pixel bytes number: ${pixelMap.getPixelBytesNumber()}`);
    pixelMap.release(); // PixelMap使用完后及时释放内存
  }).catch((err: BusinessError) => {
    console.error(`Failed to save screenshot. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to save screenshot. Code: ${exception.code}, message: ${exception.message}`);
}
```
