# setEventHubMultithreadingEnabled

## 导入模块

```TypeScript
import { sendableContextManager } from 'kits/@kit.AbilityKit';
```

## setEventHubMultithreadingEnabled

```TypeScript
function setEventHubMultithreadingEnabled(context: common.Context, enabled: boolean): void
```

设置Context中的[EventHub](arkts-ability-eventhub-c.md)是否启用跨线程通信能力。

> **说明：**&gt;
> - 当多个Context进行通信时，需要调用该接口设置每个Context都支持EventHub跨线程数据传递功能。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |
| enabled | boolean | 是 |
