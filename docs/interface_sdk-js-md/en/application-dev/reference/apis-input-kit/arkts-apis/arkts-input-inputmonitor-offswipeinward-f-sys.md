# offSwipeInward (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## offSwipeInward

```TypeScript
function offSwipeInward(receiver?: Callback<SwipeInward>): void
```

取消监听向内滑动事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offSwipeInward(receiver?: Callback<SwipeInward>): void--><!--Device-inputMonitor-function offSwipeInward(receiver?: Callback<SwipeInward>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwipeInward](arkts-input-multimodalinput-gestureevent-swipeinward-i-sys.md)&gt; | No | 需要取消监听的回调函数。若不填，则取消当前应用监听的所有回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 202 | SystemAPI permit error. |

