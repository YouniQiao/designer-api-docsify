# LazyCustomLayoutAlgorithm

定义懒式自定义布局算法。

**Inheritance/Implementation:** LazyCustomLayoutAlgorithm implements [LazyLayoutAlgorithm](arkts-arkui-lazylayoutalgorithm-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class LazyCustomLayoutAlgorithm implements LazyLayoutAlgorithm--><!--Device-unnamed-export declare class LazyCustomLayoutAlgorithm implements LazyLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: LazyCustomLayoutAlgorithmOptions)
```

构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)--><!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [LazyCustomLayoutAlgorithmOptions](arkts-arkui-lazylayoutalgorithm-lazycustomlayoutalgorithmoptions-i.md) | No | 设置懒加载自定义布局算法的属性。 |

## onLayout

```TypeScript
onLayout(self: FrameNode, position: NodePosition): void
```

方法为DynamicLayout的FrameNode及其每个子节点分配一个位置。它可以用于指定DynamicLayoutdFrameNode及其子节点的布局位置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void--><!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes | DynamicLayout组件的FrameNode。 |
| position | [NodePosition](arkts-arkui-nodeposition-t.md) | Yes | 节点的位置，将在执行布局方法时使用。 |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void
```

测量DynamicLayout FrameNode及其内容，以确定测量的大小的方法。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void--><!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes | DynamicLayout组件的FrameNode。 |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | Yes | 节点的布局约束，将在测量过程中使用。 |
| helper | [LazyLayoutHelper](arkts-arkui-lazylayoutalgorithm-lazylayouthelper-c.md) | No | 懒布局算法的助手对象，提供布局方向和视图位置信息。 如果未定义，则表示当前组件未在可滚动组件下使用，不支持懒布局。 |

