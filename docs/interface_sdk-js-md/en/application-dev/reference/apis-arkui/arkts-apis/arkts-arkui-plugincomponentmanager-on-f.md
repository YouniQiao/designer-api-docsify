# on

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## on

```TypeScript
export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void
```

Plugin component event listener.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void--><!--Device-pluginComponentManager-export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | string | Yes |  |
| callback | [OnPushEventCallback](arkts-arkui-plugincomponentmanager-onpusheventcallback-t.md) \| OnRequestEventCallback | Yes |  |

