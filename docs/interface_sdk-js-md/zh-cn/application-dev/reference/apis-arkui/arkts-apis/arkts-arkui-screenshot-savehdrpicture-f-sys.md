# saveHdrPicture（系统接口）

## 导入模块

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## saveHdrPicture

```TypeScript
function saveHdrPicture(options?: HdrScreenshotOptions): Promise<Array<image.PixelMap>>
```

获取屏幕截图，使用Promise异步回调。SDR为标准动态范围图，HDR为高动态范围图。  
- 当物理屏存在HDR资源（包括HDR资源被遮挡）时，无论HDR是否开启，该接口返回一个包含SDR和HDR的PixelMap数组。  
- 当物理屏不存在HDR资源时，与[save](arkts-arkui-screenshot-save-f-sys.md)  
接口返回一个SDR的PixelMap不同，该接口返回包含一个SDR的PixelMap数组。同时该接口不具备 [save](arkts-arkui-screenshot-save-f-sys.md)接口的裁剪、拉伸、旋转功能。

**起始版本：** 20

**需要权限：** 
- API版本22+：ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本20 - 21：ohos.permission.CAPTURE_SCREEN

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [HdrScreenshotOptions](arkts-arkui-screenshot-hdrscreenshotoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;image.PixelMap & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
| [1400004](../errorcode-display.md#1400004-参数异常) |
