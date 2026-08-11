# begin (System API)

## Modules to Import

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## begin

```TypeScript
function begin(scene: string, startInputType: ActionType, note?: string): void
```

Marks the start of a user scene. Call this API when the scene begins.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-performanceMonitor-function begin(scene: string, startInputType: ActionType, note?: string): void--><!--Device-performanceMonitor-function begin(scene: string, startInputType: ActionType, note?: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scene | string | Yes |
| startInputType | [ActionType](../../apis-data-protection-kit/arkts-apis/arkts-dataprotection-dlppermission-actiontype-e.md) | Yes |
| note | string | No |

## Examples

Start point of the user scene where the user taps an icon to launch an application, triggered by a release event (LAST_UP).

```TypeScript
performanceMonitor.begin("LAUNCHER_APP_LAUNCH_FROM_ICON", performanceMonitor.ActionType.LAST_UP, "APP_START_BEGIN");
```
