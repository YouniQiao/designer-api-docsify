# InputEventListener

```TypeScript
export declare type InputEventListener = (
  event: RawInputEventWrapper
) => InputEventInterceptResult
```

Defines the input event listener callback function type.Performance Warning: Do not perform time-consuming operations in the callback, otherwise it may cause the application to freeze.The listener executes synchronously in the UI thread and will directly block the event processing flow. It is recommended to only perform simple judgments and calculations, avoiding: - Synchronous I/O operations - Complex data processing - Network requests - Massive log output

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type InputEventListener = (  event: RawInputEventWrapper) => InputEventInterceptResult--><!--Device-unnamed-export declare type InputEventListener = (  event: RawInputEventWrapper) => InputEventInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [RawInputEventWrapper](arkts-common-rawinputeventwrapper-c.md) | Yes | Input event wrapper |

**Return value:**

| Type | Description |
| --- | --- |
| [InputEventInterceptResult](arkts-common-inputeventinterceptresult-i.md) | Event intercept result |

