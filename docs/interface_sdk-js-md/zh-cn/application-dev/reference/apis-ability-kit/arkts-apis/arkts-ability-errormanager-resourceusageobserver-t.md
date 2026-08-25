# ResourceUsageObserver

```TypeScript
export type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: number, detailInfo?: Record<string, number>) => void
```

定义应用资源使用情况的观察者回调函数，作为 [errorManager.setDefaultResourceUsageObserver](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md)的入参，用于监听各类资源占用变化， 并支持应用执行自定义资源处理逻辑。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [resourceType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-sceneresource-i.md) | [ResourceType](arkts-ability-errormanager-resourcetype-e.md) | 是 |
| resourceSize | number | 是 |
| detailInfo | Record & lt;string, number & gt; | 否 |
