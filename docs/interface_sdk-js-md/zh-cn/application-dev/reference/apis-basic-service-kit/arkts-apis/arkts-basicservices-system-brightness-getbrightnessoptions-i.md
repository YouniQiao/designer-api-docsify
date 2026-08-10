# GetBrightnessOptions

获取屏幕亮度的参数对象。

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 7

<!--Device-unnamed-export interface GetBrightnessOptions--><!--Device-unnamed-export interface GetBrightnessOptions-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

## 导入模块

```TypeScript
import { BrightnessResponse, BrightnessModeResponse, SetBrightnessModeOptions, GetBrightnessModeOptions, SetBrightnessOptions, GetBrightnessOptions, SetKeepScreenOnOptions } from 'kits/@kit.BasicServicesKit';
```

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 7

<!--Device-GetBrightnessOptions-complete?: () => void--><!--Device-GetBrightnessOptions-complete?: () => void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。data为错误信息，code为错误码。

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 7

<!--Device-GetBrightnessOptions-fail?: (data: string, code: number) => void--><!--Device-GetBrightnessOptions-fail?: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 |  |
| code | number | 是 |  |

## success

```TypeScript
success?: (data: BrightnessResponse) => void
```

接口调用成功的回调函数。data为[BrightnessResponse](arkts-basicservices-system-brightness-brightnessresponse-i.md)类型的返回值。

**起始版本：** 3

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为3。

**废弃版本：** 7

<!--Device-GetBrightnessOptions-success?: (data: BrightnessResponse) => void--><!--Device-GetBrightnessOptions-success?: (data: BrightnessResponse) => void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [BrightnessResponse](arkts-basicservices-system-brightness-brightnessresponse-i.md) | 是 |  |

