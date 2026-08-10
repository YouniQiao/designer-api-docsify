# getBrightnessInfo

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getBrightnessInfo

```TypeScript
function getBrightnessInfo(displayId: long): BrightnessInfo
```

获取指定displayId对应屏幕的亮度信息。如果屏幕不支持HDR，返回的[BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md)对象中的currentHeadroom和maxHeadroom为默认值。虚拟屏的BrightnessInfo对象中sdrNits为默认值。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-display-function getBrightnessInfo(displayId: long): BrightnessInfo--><!--Device-display-function getBrightnessInfo(displayId: long): BrightnessInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 屏幕ID。该参数仅支持整数输入，该参数大于等于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) | 返回displayId对应屏幕的亮度信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 1400004 | Parameter error. Possible cause: 1. Invalid parameter range. |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
try {
  let brightnessInfo = display.getBrightnessInfo(0);
  console.info(`brightness info: ${JSON.stringify(brightnessInfo)}`);
} catch (error) {
  console.error(`Failed to getDisplayBrightness. Code: ${error.code}, message: ${error.message}`);
}
```

