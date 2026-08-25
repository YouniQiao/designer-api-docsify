# setWaterMarkImage（系统接口）

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## setWaterMarkImage

```TypeScript
function setWaterMarkImage(pixelMap: image.PixelMap, enable: boolean): Promise<void>
```

设置屏幕水印图片显示状态。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap | 是 |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |


## setWaterMarkImage

```TypeScript
function setWaterMarkImage(pixelMap: image.PixelMap, enable: boolean, priority: number): Promise<void>
```

设置屏幕水印图片的显示状态，并设定水印的优先级。使用Promise异步回调。当priority等于0时，当前接口与 [setWaterMarkImage](#setwatermarkimage系统接口) 等价。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap | 是 |
| enable | boolean | 是 |
| priority | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |


## setWaterMarkImage

```TypeScript
function setWaterMarkImage(pixelMap: image.PixelMap, enable: boolean, callback: AsyncCallback<void>): void
```

设置屏幕水印图片显示状态。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap | 是 |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
