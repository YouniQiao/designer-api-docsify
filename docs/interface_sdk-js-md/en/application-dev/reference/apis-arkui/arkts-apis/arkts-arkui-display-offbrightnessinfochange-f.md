# offBrightnessInfoChange

## Modules to Import

```TypeScript
import { display } from 'display';
```

## offBrightnessInfoChange

```TypeScript
function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void
```

Unregister the callback for brightness info changes.

**Since:** 23

<!--Device-display-function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;long, [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md)&gt; | No | Callback used to return the display corresponding brightness info. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function offBrightnessInfoChange can not work correctly due to limited device capabilities. |
| [1400004](../errorcode-display.md#1400004-parameter-error) | Parameter error. Possible cause: 1. Invalid parameter range. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

