# NodeContent

NodeContent是ArkUI提供的ContentSlot的管理器，用于管理挂载到ContentSlot上的FrameNode节点内 容，支持动态添加、删除FrameNode节点。适用于需要通过ContentSlot动态管理FrameNode节点内容的场景，例如根据用户交互动态新增或移除文本、图片等自定义FrameNode节点。

> **说明：**&gt;
> - NodeContent对象不支持使用JSON序列化。

**继承/实现关系：** NodeContent extends Content

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addFrameNode

```TypeScript
addFrameNode(node: FrameNode): void
```

将FrameNode添加到NodeContent中，添加后FrameNode将通过关联的ContentSlot渲染显示。适用于需要动态管理ContentSlot中显示内容节点的场景，例如根据用户交互动态新增文本、图片等自定义 FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |

## constructor

```TypeScript
constructor()
```

节点内容的实体封装。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## removeFrameNode

```TypeScript
removeFrameNode(node: FrameNode): void
```

将FrameNode从NodeContent中删除，删除后FrameNode将不再通过ContentSlot显示。适用于需要动态移除已添加内容节点的场景，例如用户交互后移除指定的文本、图片等自定义FrameNode节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | 是 |
