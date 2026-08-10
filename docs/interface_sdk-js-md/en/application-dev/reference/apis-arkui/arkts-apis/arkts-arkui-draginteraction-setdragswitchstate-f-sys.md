# setDragSwitchState (System API)

## Modules to Import

```TypeScript
import { dragInteraction } from 'kits/@kit.ArkUI';
```

## setDragSwitchState

```TypeScript
function setDragSwitchState(enabled: boolean): void
```

控制统一拖拽功能总开关。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-dragInteraction-function setDragSwitchState(enabled: boolean): void--><!--Device-dragInteraction-function setDragSwitchState(enabled: boolean): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 设置开关状态。&lt;br&gt;false：关闭，true：开启。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |

