# offTouchscreenSwipe (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## offTouchscreenSwipe

```TypeScript
function offTouchscreenSwipe(fingers: int, receiver?: Callback<TouchGestureEvent>): void
```

Disables listening touchscreen swipe gesture events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offTouchscreenSwipe(fingers: int, receiver?: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function offTouchscreenSwipe(fingers: int, receiver?: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | int | Yes | Number of fingers. |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchGestureEvent](arkts-input-multimodalinput-gestureevent-touchgestureevent-i-sys.md)&gt; | No | Callback used to receive reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. 3.Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

