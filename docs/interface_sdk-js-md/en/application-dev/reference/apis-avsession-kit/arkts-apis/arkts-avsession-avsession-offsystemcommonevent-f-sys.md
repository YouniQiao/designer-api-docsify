# offSystemCommonEvent (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## offSystemCommonEvent

```TypeScript
function offSystemCommonEvent(callback?: EventProcess): void
```

取消注册通用事件回调监听

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function offSystemCommonEvent(callback?: EventProcess): void--><!--Device-avSession-function offSystemCommonEvent(callback?: EventProcess): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [EventProcess](arkts-avsession-avsession-eventprocess-t.md) | No | 处理事件回调 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 202 | Not System App. |

