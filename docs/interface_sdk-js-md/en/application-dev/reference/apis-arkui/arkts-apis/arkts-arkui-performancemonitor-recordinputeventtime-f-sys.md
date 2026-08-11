# recordInputEventTime (System API)

## Modules to Import

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## recordInputEventTime

```TypeScript
function recordInputEventTime(type: ActionType, sourceType: SourceType, time: long): void
```

recordInputEventTime monitoring an application scene.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: long): void--><!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md) | Yes | Indicates the scene input event type. |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | Yes | Indicates the scene input source type. |
| time | long | Yes | Indicates the scene input time. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

