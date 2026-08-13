# BuilderCallback

```TypeScript
declare type BuilderCallback<Args extends Object[] = any[]> = (...args: Args) => void
```

`BuilderCallback`是全局`@Builder`函数的类型别名，作为`mutableBuilder`函数的入参类型，用于指定待封装的全局`@Builder`函数。

**起始版本：** 22

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type BuilderCallback<Args extends Object[] = any[]> = (...args: Args) => void--><!--Device-unnamed-declare type BuilderCallback<Args extends Object[] = any[]> = (...args: Args) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Args | 是 |
