# onMouse (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## onMouse

```TypeScript
function onMouse(receiver: Callback<MouseEvent>): void
```

Listens for mouse input events.

**Since:** 23

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onMouse(receiver: Callback<MouseEvent>): void--><!--Device-inputMonitor-function onMouse(receiver: Callback<MouseEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| receiver | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MouseEvent](arkts-input-multimodalinputmouseevent-mouseevent-i.md)&gt; | Yes | Callback used to receive the reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |


## onMouse

```TypeScript
function onMouse(rect: display.Rect[], receiver: Callback<MouseEvent>): void
```

Listens for mouse input events when the mouse arrow is within the specified rectangular area.

**Since:** 23

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onMouse(rect: display.Rect[], receiver: Callback<MouseEvent>): void--><!--Device-inputMonitor-function onMouse(rect: display.Rect[], receiver: Callback<MouseEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | display.Rect[] | Yes | A specified rectangular area that can trigger a callback, with a maximum of two. |
| receiver | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MouseEvent](arkts-input-multimodalinputmouseevent-mouseevent-i.md)&gt; | Yes | Callback used to receive the reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

