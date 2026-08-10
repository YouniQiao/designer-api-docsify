# OnRequestEventCallback

```TypeScript
export type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult
```

对应request事件的监听回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult--><!--Device-pluginComponentManager-export type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | request请求发送方相关信息。 |
| name | string | Yes | 请求的组件名称。 |
| data | [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md) | Yes | request事件中传递的数据内容，以键值对形式存储，键和值类型由业务定义。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RequestEventResult](arkts-arkui-plugincomponentmanager-requesteventresult-i.md) | 注册request监听方法后，接收到请求事件时回应请求的数据类型。 |

