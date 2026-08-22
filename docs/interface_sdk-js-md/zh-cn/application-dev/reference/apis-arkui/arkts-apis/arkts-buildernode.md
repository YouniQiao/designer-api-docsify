# BuilderNode

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [BuilderNode](arkts-arkui-buildernode-c.md) | 提供能够挂载系统组件的自定义节点BuilderNode。BuilderNode仅可作为叶子节点使用，支持通过@Builder生成组件树、实现组件复用与回收、跨节点事件分发以及状态同步，适用于在应用内动态创建和管理自定义组件节点的场景。 使用方式参考[BuilderNode开发指南](../../../ui/arkts-user-defined-arktsNode-builderNode.md)。 |
| [ReactiveBuilderNode](arkts-arkui-buildernode-reactivebuildernode-c.md) | ReactiveBuilderNode支持通过无状态的UI方法[@Builder](../../../ui/state-management/arkts-builder.md)生成组件树，并持有该组件树的根节点，不支持定义为状态变 量。ReactiveBuilderNode中持有的FrameNode仅用于将此ReactiveBuilderNode作为子节点挂载到其他FrameNode上。对 ReactiveBuilderNode持有的FrameNode进行属性设置与子节点操作可能会导致未定义行为，因此不建议通过ReactiveBuilderNode的 [getFrameNode](../../apis-default/arkts-apis/arkts-buildernode-c.md#getframenode)方法和FrameNode节点的 [getRenderNode](../../apis-default/arkts-apis/arkts-framenode-c.md#getrendernode)方法获取RenderNode，并通过 [RenderNode](../../apis-default/arkts-apis/arkts-rendernode-c.md)的接口对其进行属性设置与子节点操作。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [BuildOptions](arkts-arkui-buildernode-buildoptions-i.md) | build的可选参数。 |
| [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | 创建BuilderNode时的可选参数。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md) | 节点渲染类型枚举。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [InputEventType](arkts-arkui-inputeventtype-t.md) | [postInputEvent](../../apis-default/arkts-apis/arkts-buildernode-c.md#postinputevent)的参数，定义要发送的输入事件类型。 |

