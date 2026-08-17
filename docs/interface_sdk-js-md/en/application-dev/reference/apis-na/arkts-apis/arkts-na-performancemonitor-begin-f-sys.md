# begin (System API)

## begin

```TypeScript
function begin(scene: string, startInputType: ActionType, note?: string): void
```

Begin monitoring an application scene.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-performanceMonitor-function begin(scene: string, startInputType: ActionType, note?: string): void--><!--Device-performanceMonitor-function begin(scene: string, startInputType: ActionType, note?: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scene | string | Yes | Indicates the scene name. |
| startInputType | ActionType | Yes | Indicates the scene input event type. |
| note | string | No | Indicates the app expected info delivered. |

