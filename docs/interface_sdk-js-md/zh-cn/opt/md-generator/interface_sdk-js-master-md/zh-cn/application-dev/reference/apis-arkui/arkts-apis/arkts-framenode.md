# FrameNode

typeNode提供创建具体类型的FrameNode能力，可通过FrameNode的基础接口进行自定义的挂载，使用占位容器进行显示。适用于需要通过代码动态创建具体类型组件节点并进行自定义挂载的场景。 使用typeNode创建Text、Image、 Select、Toggle节点时，当传入的 [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext)对应的UI实例销毁后，调用该接口会返回一个无效的FrameNode节点，无法正常挂载和显示。

## 汇总

### 类

| 名称 |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |
| [NodeAdapter](arkts-arkui-framenode-nodeadapter-c.md) |

### 接口

| 名称 |
| --- |
| [CrossLanguageOptions](arkts-arkui-framenode-crosslanguageoptions-i.md) |
| [InteractionEventBindingInfo](arkts-arkui-framenode-interactioneventbindinginfo-i.md) |
| [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) |
| [TypedFrameNode](arkts-arkui-framenode-typedframenode-i.md) |

### 枚举

| 名称 |
| --- |
| [ChildrenCountMode](arkts-arkui-framenode-childrencountmode-e.md) |
| [ExpandMode](arkts-arkui-framenode-expandmode-e.md) |
| [UIState](arkts-arkui-framenode-uistate-e.md) |

### 类型

| 名称 |
| --- |
| [UIStatesChangeHandler](arkts-arkui-uistateschangehandler-t.md) |
