# on_string

## Modules to Import

```TypeScript
```

## on_string

```TypeScript
export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void
```

Plugin component event listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void--><!--Device-pluginComponentManager-export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | string | Yes |  |
| callback | [OnPushEventCallback](arkts-plugincomponentmanager-onpusheventcallback-t.md) \| [OnRequestEventCallback](arkts-plugincomponentmanager-onrequesteventcallback-t.md) | Yes |  |

