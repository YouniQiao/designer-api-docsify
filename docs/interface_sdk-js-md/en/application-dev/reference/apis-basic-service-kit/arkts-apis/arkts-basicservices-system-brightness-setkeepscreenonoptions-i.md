# SetKeepScreenOnOptions

设置屏幕常亮的参数对象。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 7

<!--Device-unnamed-export interface SetKeepScreenOnOptions--><!--Device-unnamed-export interface SetKeepScreenOnOptions-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

## Modules to Import

```TypeScript
import { BrightnessResponse, BrightnessModeResponse, SetBrightnessModeOptions, GetBrightnessModeOptions, SetBrightnessOptions, GetBrightnessOptions, SetKeepScreenOnOptions } from 'kits/@kit.BasicServicesKit';
```

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 7

<!--Device-SetKeepScreenOnOptions-complete?: () => void--><!--Device-SetKeepScreenOnOptions-complete?: () => void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。data为错误信息，code为错误码。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 7

<!--Device-SetKeepScreenOnOptions-fail?: (data: string, code: number) => void--><!--Device-SetKeepScreenOnOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: () => void
```

接口调用成功的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 7

<!--Device-SetKeepScreenOnOptions-success?: () => void--><!--Device-SetKeepScreenOnOptions-success?: () => void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

## keepScreenOn

```TypeScript
keepScreenOn: boolean
```

true表示保持屏幕常亮，false表示取消屏幕常亮。

**Type:** boolean

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 7

<!--Device-SetKeepScreenOnOptions-keepScreenOn: boolean--><!--Device-SetKeepScreenOnOptions-keepScreenOn: boolean-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

