# on

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## on

```TypeScript
export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void
```

提供方监听"request"类型的事件，给使用方返回通过request接口主动请求的数据；使用方监听"push"类型的事件，接收提供方通过push接口主动推送的数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void--><!--Device-pluginComponentManager-export function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | string | Yes | 监听的事件类型，可选值为："push"、"request"。"push"：指组件提供方向使用方主动推送数据。"request"：指组件使用方向提供方主动请求数据。 |
| callback | [OnPushEventCallback](arkts-arkui-plugincomponentmanager-onpusheventcallback-t.md) \| OnRequestEventCallback | Yes | 对应监听回调， push事件对应回调类型为OnPushEventCallback，request事件对应回调类型为OnRequestEventCallback。 |

