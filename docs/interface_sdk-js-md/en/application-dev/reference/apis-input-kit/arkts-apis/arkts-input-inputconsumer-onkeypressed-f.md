# onKeyPressed

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## onKeyPressed

```TypeScript
function onKeyPressed(options: KeyPressedConfig, callback: Callback<KeyEvent>): void
```

Subscribes to key press events. This API uses an asynchronous callback to return the result.If the current application is in the foreground focus window, a callback is triggered when the specified key is pressed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputConsumer-function onKeyPressed(options: KeyPressedConfig, callback: Callback<KeyEvent>): void--><!--Device-inputConsumer-function onKeyPressed(options: KeyPressedConfig, callback: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [KeyPressedConfig](arkts-input-inputconsumer-keypressedconfig-i.md) | Yes | Key consumption settings. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | Yes | Callback used to return key events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

