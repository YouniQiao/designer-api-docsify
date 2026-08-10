# offTouchscreenPinch (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## offTouchscreenPinch

```TypeScript
function offTouchscreenPinch(fingers: int, receiver?: Callback<TouchGestureEvent>): void
```

取消监听触摸屏捏合手势事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offTouchscreenPinch(fingers: int, receiver?: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function offTouchscreenPinch(fingers: int, receiver?: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | int | Yes | 捏合手势的手指数，取值范围：[4,5]。 |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchGestureEvent](arkts-input-multimodalinput-gestureevent-touchgestureevent-i-sys.md)&gt; | No | 需要取消监听的回调函数。若不填，则取消当前应用监听的所有回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. 3.Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |

