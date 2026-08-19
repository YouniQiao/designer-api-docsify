# onKeyPressed (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## onKeyPressed

```TypeScript
function onKeyPressed(keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void
```

Enables listening for release events of specified keys, such as the logo, power, and volume keys.

**Since:** 23

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onKeyPressed(keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void--><!--Device-inputMonitor-function onKeyPressed(keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | Yes | Key list. |
| receiver | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | Yes | Callback used to receive the reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [4100001](../errorcode-inputmonitor.md#4100001-event-listening-not-supported-for-the-key) | Event listening not supported for the key. |

