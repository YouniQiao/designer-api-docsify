# offTouchscreenPinch (System API)

## Modules to Import

```TypeScript
```

## offTouchscreenPinch

```TypeScript
function offTouchscreenPinch(fingers: number, receiver?: Callback<TouchGestureEvent>): void
```

Disables listening touchscreen pinch gesture events.

**Since:** 23

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offTouchscreenPinch(fingers: int, receiver?: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function offTouchscreenPinch(fingers: int, receiver?: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fingers | number | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchGestureEvent](arkts-input-multimodalinput-gestureevent-touchgestureevent-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
