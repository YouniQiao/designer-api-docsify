# on

## 导入模块

```TypeScript
import { pluginComponentManager, PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## on

```TypeScript
function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void
```

提供方监听"request"类型的事件，给使用方返回通过request接口主动请求的数据；使用方监听"push"类型的事件，接收提供方通过push接口主动推送的数据。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventType | string | 是 |
| callback | [OnPushEventCallback](arkts-arkui-plugincomponentmanager-onpusheventcallback-t.md) \| [OnRequestEventCallback](arkts-arkui-plugincomponentmanager-onrequesteventcallback-t.md) | 是 |
