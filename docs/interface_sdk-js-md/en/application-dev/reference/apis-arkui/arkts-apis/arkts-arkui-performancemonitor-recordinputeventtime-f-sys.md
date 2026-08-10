# recordInputEventTime (System API)

## Modules to Import

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## recordInputEventTime

```TypeScript
function recordInputEventTime(type: ActionType, sourceType: SourceType, time: long): void
```

记录动效场景开始前，用户输入触发事件类型与时间。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: long): void--><!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md) | Yes | 用户场景触发模式。 |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | Yes | 用户场景触发源。 |
| time | long | Yes | 场景触发时间（ms），时间戳，例如1751508570794。若传零或负值将自动转化为当前系统时间，若传正值则正常使用。不正确的传参会导致用户操作响应时延指标异常。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | not system application. |

