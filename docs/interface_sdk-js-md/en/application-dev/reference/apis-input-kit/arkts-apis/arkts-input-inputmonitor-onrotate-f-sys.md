# onRotate (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## onRotate

```TypeScript
function onRotate(fingers: int, receiver: Callback<Rotate>): void
```

监听全局触控板的旋转事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onRotate(fingers: int, receiver: Callback<Rotate>): void--><!--Device-inputMonitor-function onRotate(fingers: int, receiver: Callback<Rotate>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | int | Yes | 旋转的手指数，手指数不能小于0，当前仅支持收到旋转手势的回调。 |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Rotate](arkts-input-multimodalinput-gestureevent-rotate-i.md)&gt; | Yes | 回调函数，异步上报旋转输入事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | SystemAPI permit error. |

