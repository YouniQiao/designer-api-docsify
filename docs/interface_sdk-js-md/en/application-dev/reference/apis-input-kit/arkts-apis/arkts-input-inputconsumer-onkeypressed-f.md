# onKeyPressed

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## onKeyPressed

```TypeScript
function onKeyPressed(options: KeyPressedConfig, callback: Callback<KeyEvent>): void
```

Subscribes to key press events. This API uses an asynchronous callback to return the result. If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed.

**Since:** 23

<!--Device-inputConsumer-function onKeyPressed(options: KeyPressedConfig, callback: Callback<KeyEvent>): void--><!--Device-inputConsumer-function onKeyPressed(options: KeyPressedConfig, callback: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [KeyPressedConfig](arkts-input-inputconsumer-keypressedconfig-i.md) | Yes | Key consumption settings. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | Yes | Callback used to return key events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

