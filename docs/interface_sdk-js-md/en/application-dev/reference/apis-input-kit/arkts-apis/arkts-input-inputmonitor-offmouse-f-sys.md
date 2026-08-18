# offMouse (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## offMouse

```TypeScript
function offMouse(receiver?: Callback<MouseEvent>): void
```

Cancel listening for mouse input events.

**Since:** 23

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offMouse(receiver?: Callback<MouseEvent>): void--><!--Device-inputMonitor-function offMouse(receiver?: Callback<MouseEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| receiver | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MouseEvent](arkts-input-multimodalinput-mouseevent-mouseevent-i.md)&gt; | No | Callback used to receive the reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

