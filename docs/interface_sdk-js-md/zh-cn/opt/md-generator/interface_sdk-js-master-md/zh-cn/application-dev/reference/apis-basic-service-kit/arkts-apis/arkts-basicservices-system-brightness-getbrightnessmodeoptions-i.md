# GetBrightnessModeOptions

获取屏幕亮度模式的参数对象。

**起始版本：** 3

**废弃版本：** 7

<!--Device-unnamed-export interface GetBrightnessModeOptions--><!--Device-unnamed-export interface GetBrightnessModeOptions-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**起始版本：** 3

**废弃版本：** 7

<!--Device-GetBrightnessModeOptions-complete?: () => void--><!--Device-GetBrightnessModeOptions-complete?: () => void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。data为错误信息，code为错误码。

**起始版本：** 3

**废弃版本：** 7

<!--Device-GetBrightnessModeOptions-fail?: (data: string, code: number) => void--><!--Device-GetBrightnessModeOptions-fail?: (data: string, code: number) => void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |
| code | number | 是 |

## success

```TypeScript
success?: (data: BrightnessModeResponse) => void
```

接口调用成功的回调函数。data为[BrightnessModeResponse](arkts-basicservices-system-brightness-brightnessmoderesponse-i.md#BrightnessModeResponse)类型的返回值。

**起始版本：** 3

**废弃版本：** 7

<!--Device-GetBrightnessModeOptions-success?: (data: BrightnessModeResponse) => void--><!--Device-GetBrightnessModeOptions-success?: (data: BrightnessModeResponse) => void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [BrightnessModeResponse](arkts-basicservices-system-brightness-brightnessmoderesponse-i.md) | 是 |
