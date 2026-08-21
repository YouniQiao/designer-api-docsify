# offKeyPressed

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## offKeyPressed

```TypeScript
function offKeyPressed(callback?: Callback<KeyEvent>): void
```

Cancels consumption of key events.

**Since:** 23

<!--Device-inputConsumer-function offKeyPressed(callback?: Callback<KeyEvent>): void--><!--Device-inputConsumer-function offKeyPressed(callback?: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[KeyEvent](arkts-input-multimodalinputkeyevent-keyevent-i.md)&gt; | No | Callback used to return hotkey events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

