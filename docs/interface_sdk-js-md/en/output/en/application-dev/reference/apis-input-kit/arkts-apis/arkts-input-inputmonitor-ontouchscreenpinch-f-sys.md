# onTouchscreenPinch (System API)

## onTouchscreenPinch

```TypeScript
function onTouchscreenPinch(fingers: int, receiver: Callback<TouchGestureEvent>): void
```

Enables listening touchscreen pinch gesture events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onTouchscreenPinch(fingers: int, receiver: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function onTouchscreenPinch(fingers: int, receiver: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | int | Yes | Number of fingers. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TouchGestureEvent&gt; | Yes | Callback used to receive reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.3.Parameter verification failed. |

