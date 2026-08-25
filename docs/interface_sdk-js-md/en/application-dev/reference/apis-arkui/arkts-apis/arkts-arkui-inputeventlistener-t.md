# InputEventListener

```TypeScript
export declare type InputEventListener = (
  event: RawInputEventWrapper
) => InputEventInterceptResult
```

Defines the input event listener callback function type.Performance Warning: Do not perform time-consuming operations in the callback, otherwise it may cause the application to freeze.The listener executes synchronously in the UI thread and will directly block the event processing flow. It is recommended to only perform simple judgments and calculations, avoiding: - Synchronous I/O operations - Complex data processing - Network requests - Massive log output

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [RawInputEventWrapper](arkts-arkui-common-rawinputeventwrapper-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputEventInterceptResult](arkts-arkui-common-inputeventinterceptresult-i.md) |
