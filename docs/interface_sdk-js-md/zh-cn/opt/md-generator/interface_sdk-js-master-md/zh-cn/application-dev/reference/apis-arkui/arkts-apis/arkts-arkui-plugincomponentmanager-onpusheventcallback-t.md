# OnPushEventCallback

```TypeScript
type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,
    extraData: KVObject) => void
```

对应push事件的监听回调函数。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-pluginComponentManager-type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void--><!--Device-pluginComponentManager-type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| template | [PluginComponentTemplate](arkts-arkui-plugincomponent-plugincomponenttemplate-i.md) | 是 |
| data | [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md) | 是 |
| extraData | [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md) | 是 |
