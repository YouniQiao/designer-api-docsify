# FrameNode

提供用于实现 FrameNode 的方法。

## 汇总

### 命名空间

| 名称 | 说明 |
| --- | --- |
| [typeNode](arkts-typenode-n.md) | 提供用于实现 FrameNode 的方法。 |

### 类

| 名称 | 说明 |
| --- | --- |
| [FrameNode](arkts-framenode-c.md) | 定义FrameNode。 |
| [NodeAdapter](arkts-framenode-nodeadapter-c.md) | NodeAdapter提供FrameNode的数据懒加载能力，通过LazyForEach实现接口功能。 |
| [TypedFrameNode](arkts-framenode-typedframenode-c.md) | TypedFrameNode继承自[FrameNode](arkts-framenode-framenodeoptions-i.md)，用于声明具体类型的FrameNode。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [CrossLanguageOptions](arkts-framenode-crosslanguageoptions-i.md) | 该接口用于配置或查询FrameNode的跨语言访问权限。例如，针对ArkTS语言创建的节点，可通过该接口控制是否允许通过非ArkTS语言进行属性访问或修改。 |
| [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | FrameNode选项，可设置FrameNode是否支持多线程操作。 |
| [InteractionEventBindingInfo](arkts-framenode-interactioneventbindinginfo-i.md) | 组件的交互事件绑定状态信息。如果当前节点上绑定了所要查询的交互事件，调用查询接口时返回一个InteractionEventBindingInfo对象，指示事件绑定详细信息。 |
| [LayoutConstraint](arkts-framenode-layoutconstraint-i.md) | 描述组件的布局约束。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ChildrenCountMode](arkts-framenode-childrencountmode-e.md) | 子节点计数模式枚举。用于指定获取子节点数量时的计数方式。 |
| [ExpandMode](arkts-framenode-expandmode-e.md) | 子节点展开模式枚举。 |
| [UIState](arkts-framenode-uistate-e.md) | 多态样式状态枚举，用于处理多态样式。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [UIStatesChangeHandler](arkts-uistateschangehandler-t.md) | UI状态变化处理函数，返回当前UI状态，值为结果 的所有当前状态枚举值或计算，并且可以确定状态 通过执行&操作，如下。 如果(currentStates & UIState.PRESSED == UIState.PRESSED) 但是，请注意，对于正常的状态检查，应该直接使用equal。 如果(currentStates == UIState.NORMAL)。 |

