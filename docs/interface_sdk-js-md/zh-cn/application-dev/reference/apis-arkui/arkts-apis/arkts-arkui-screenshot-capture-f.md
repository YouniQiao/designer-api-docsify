# capture

## 导入模块

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## capture

```TypeScript
function capture(options?: CaptureOption): Promise<image.PixelMap>
```

获取屏幕全屏截图，使用Promise异步回调。此接口可以通过设置不同的displayId截取不同屏幕的截图，且只能截取全屏；[pick](arkts-arkui-screenshot-pick-f.md)接口可实现区域截屏。

**起始版本：** 14

**需要权限：** 
- API版本22+：ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本14 - 21：ohos.permission.CUSTOM_SCREEN_CAPTURE

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
