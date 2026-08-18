# onBrightnessInfoChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onBrightnessInfoChange

```TypeScript
function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void
```

Register the callback for brightness info changes.

**Since:** 23

<!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;long, [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md)&gt; | Yes | Callback used to return the display if and corresponding brightness info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function onBrightnessInfoChange can not work correctly due to limited device capabilities. |
| [1400004](../errorcode-display.md#1400004-parameter-error) | Parameter error. Possible cause: 1. Invalid parameter range. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

