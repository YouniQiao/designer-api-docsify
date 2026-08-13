# ForEach

ForEach接口基于数组类型数据进行循环渲染，可基于数组数据快速生成结构相同、内容不同的子组件，适用于动态列表、批量数据展示等场景，需与容器组件配合使用。 开发者指南见：[ForEach开发者指南](../../../ui/rendering-control/arkts-rendering-control-foreach.md)。

## ForEach

```TypeScript
ForEach(
    arr: Array<any>,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string,
  )
```

该接口需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，ListItem组件要求ForEach的父容器组件必须为 List组件或ListItemGroup组件。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ForEachInterface-(    arr: Array<any>,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,  ): ForEachAttribute--><!--Device-ForEachInterface-(    arr: Array<any>,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,  ): ForEachAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | Array & lt;any & gt; | 是 |
| itemGenerator | (item: any, index: number) = & gt; void | 是 |
| keyGenerator | (item: any, index: number) = & gt; string | 否 |

## 汇总
