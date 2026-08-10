# end (System API)

## Modules to Import

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## end

```TypeScript
function end(scene: string): void
```

用于标记用户场景结束，用户场景结束时调用此接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-performanceMonitor-function end(scene: string): void--><!--Device-performanceMonitor-function end(scene: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scene | string | Yes | 用户场景id，与begin配对严格保持一致，否则本次场景监测无效。 |

