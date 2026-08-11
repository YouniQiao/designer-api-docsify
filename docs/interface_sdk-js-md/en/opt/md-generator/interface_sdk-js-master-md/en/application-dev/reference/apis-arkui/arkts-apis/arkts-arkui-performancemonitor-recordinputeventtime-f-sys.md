# recordInputEventTime (System API)

## Modules to Import

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## recordInputEventTime

```TypeScript
function recordInputEventTime(type: ActionType, sourceType: SourceType, time: number): void
```

Records the trigger event type and time before the start of the animation scene.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: number): void--><!--Device-performanceMonitor-function recordInputEventTime(type: ActionType, sourceType: SourceType, time: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ActionType](../../apis-data-protection-kit/arkts-apis/arkts-dataprotection-dlppermission-actiontype-e.md) | Yes |
| sourceType | [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md) | Yes |
| time | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { systemDateTime, BusinessError } from '@kit.BasicServicesKit';
import { performanceMonitor } from '@kit.ArkUI';

// Obtain the current system time.
let time = systemDateTime.getTime(false);
// Update the user trigger event type and time.
performanceMonitor.recordInputEventTime(performanceMonitor.ActionType.LAST_UP, performanceMonitor.SourceType.PERF_MOUSE_EVENT, time);
```
