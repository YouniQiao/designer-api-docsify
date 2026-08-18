# onSwipeInward (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## onSwipeInward

```TypeScript
function onSwipeInward(receiver: Callback<SwipeInward>): void
```

Enables listening touchPad swipe inward events.

**Since:** 23

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onSwipeInward(receiver: Callback<SwipeInward>): void--><!--Device-inputMonitor-function onSwipeInward(receiver: Callback<SwipeInward>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| receiver | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SwipeInward](arkts-input-multimodalinput-gestureevent-swipeinward-i-sys.md)&gt; | Yes | Callback used to receive the reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |

