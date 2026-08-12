# BuilderNode

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [BuilderNode](arkts-arkui-buildernode-c.md) | class BuilderNode\&lt;T = undefined&gt;BuilderNode支持通过无状态的UI方法[@Builder](../../../ui/state-management/arkts-builder.md)生成组件树，并持有组件树的根节点。不支持定义为状态变量。BuilderNode中持有的FrameNode仅用于将该BuilderNode作为子节点挂载到其他FrameNode上。对BuilderNode持有的FrameNode进行属性设置与子节点操作可能会产生未定义行为，因此不建议通过BuilderNode的[getFrameNode](arkts-arkui-buildernode-c.md#getFrameNode)方法和[FrameNode](FrameNode)的  [getRenderNode](arkts-arkui-framenode-c.md#getRenderNode)方法获取RenderNode，并通过[RenderNode](arkts-arkui-rendernode-c.md#RenderNode)的接口对其进行属性设置与子节点操作。 |
| [ReactiveBuilderNode](arkts-arkui-buildernode-reactivebuildernode-c.md) | ReactiveBuilderNode支持通过无状态的UI方法[@Builder](../../../ui/state-management/arkts-builder.md)生成组件树，并持有该组件树的根节点，不支持定义为状态变量。ReactiveBuilderNode中持有的[FrameNode](FrameNode)仅用于将此ReactiveBuilderNode作为子节点挂载到其他FrameNode上。对ReactiveBuilderNode持有的FrameNode进行属性设置与子节点操作可能会导致未定义行为，因此不建议通过ReactiveBuilderNode的  [getFrameNode](arkts-arkui-buildernode-c.md#getFrameNode)方法和[FrameNode](FrameNode)节点的  [getRenderNode](arkts-arkui-framenode-c.md#getRenderNode)方法获取RenderNode，并通过[RenderNode](arkts-arkui-rendernode-c.md#RenderNode)的接口对其进行属性设置与子节点操作。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [BuildOptions](arkts-arkui-buildernode-buildoptions-i.md) | build的可选参数。 |
| [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | 创建BuilderNode时的可选参数。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md) | 节点渲染类型枚举。  @Component](../../../ui/state-management/arkts-create-custom-components.md#component)修饰的自定义组件、 > [NodeContainer](node_container)以及[NodeContainer](node_container)下挂载的[FrameNode](FrameNode)和 > [RenderNode](arkts-arkui-rendernode-c.md#RenderNode)。 >  > - 使用方式可参考[同层渲染绘制](../../../web/web-same-layer.md)。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [InputEventType](arkts-arkui-inputeventtype-t.md) | [postInputEvent](arkts-arkui-buildernode-c.md#postInputEvent)的参数，定义要发送的输入事件类型。 |

