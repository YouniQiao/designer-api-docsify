# push

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## push

```TypeScript
export function push(param: PushParameters, callback: AsyncCallback<void>): void
```

组件提供方向组件使用方主动发送组件和数据。适用于提供方数据更新后需主动通知使用方刷新显示的场景。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export function push(param: PushParameters, callback: AsyncCallback<void>): void--><!--Device-pluginComponentManager-export function push(param: PushParameters, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [PushParameters](arkts-arkui-plugincomponentmanager-pushparameters-i.md) | Yes | 推送组件的详细参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 此次接口调用的异步回调。 |

