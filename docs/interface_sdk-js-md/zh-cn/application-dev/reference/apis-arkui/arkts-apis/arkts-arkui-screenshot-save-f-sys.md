# save（系统接口）

## 导入模块

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## save

```TypeScript
function save(options: ScreenshotOptions, callback: AsyncCallback<image.PixelMap>): void
```

获取屏幕截图，使用callback异步回调。

**起始版本：** 7

**需要权限：** 
- API版本26.0.0+：ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本22 - 24：ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本7 - 21：ohos.permission.CAPTURE_SCREEN

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ScreenshotOptions](arkts-arkui-screenshot-screenshotoptions-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |


## save

```TypeScript
function save(callback: AsyncCallback<image.PixelMap>): void
```

获取屏幕截图，使用callback异步回调。

**起始版本：** 7

**需要权限：** 
- API版本26.0.0+：ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本22 - 24：ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本7 - 21：ohos.permission.CAPTURE_SCREEN

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## save

```TypeScript
function save(options?: ScreenshotOptions): Promise<image.PixelMap>
```

获取屏幕截图，使用Promise异步回调。

**起始版本：** 7

**需要权限：** 
- API版本26.0.0+：ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本22 - 24：ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API版本7 - 21：ohos.permission.CAPTURE_SCREEN

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ScreenshotOptions](arkts-arkui-screenshot-screenshotoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
