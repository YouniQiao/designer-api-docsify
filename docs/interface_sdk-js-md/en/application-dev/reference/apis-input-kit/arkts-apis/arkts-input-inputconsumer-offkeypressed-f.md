# offKeyPressed

## Modules to Import

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## offKeyPressed

```TypeScript
function offKeyPressed(callback?: Callback<KeyEvent>): void
```

Cancels consumption of key events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputConsumer-function offKeyPressed(callback?: Callback<KeyEvent>): void--><!--Device-inputConsumer-function offKeyPressed(callback?: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | No | Callback used to return hotkey events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

