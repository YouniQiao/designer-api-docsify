# offBrightnessInfoChange

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## offBrightnessInfoChange

```TypeScript
function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void
```

Unregister the callback for brightness info changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;long, BrightnessInfo&gt; | No | Callback used to return the display corresponding brightness info. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 1400004 | Parameter error. Possible cause: 1. Invalid parameter range. |
| 1400003 | This display manager service works abnormally. |

