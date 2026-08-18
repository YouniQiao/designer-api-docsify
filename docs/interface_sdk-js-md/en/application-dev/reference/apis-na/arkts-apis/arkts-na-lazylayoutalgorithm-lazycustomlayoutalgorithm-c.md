# LazyCustomLayoutAlgorithm

Defines the lazy custom layout algorithm.

**Inheritance/Implementation:** LazyCustomLayoutAlgorithm implements [LazyLayoutAlgorithm](../../apis-arkui/arkts-apis/arkts-arkui-lazylayoutalgorithm-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class LazyCustomLayoutAlgorithm--><!--Device-unnamed-export declare class LazyCustomLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: LazyCustomLayoutAlgorithmOptions)
```

Constructor.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)--><!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [LazyCustomLayoutAlgorithmOptions](../../apis-arkui/arkts-apis/arkts-arkui-lazylayoutalgorithm-lazycustomlayoutalgorithmoptions-i.md) | No | set properties of lazy custom layout algorithm. |

## onLayout

```TypeScript
onLayout(self: FrameNode, position: NodePosition): void
```

Method to assign a position to the DynamicLayout FrameNode and each of its children. It can be used to specify the layout location of the DynamicLayout FrameNode and its children.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void--><!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-na-framenode-c.md) | Yes | The FrameNode of DynamicLayout component. |
| position | [NodePosition](arkts-na-nodeposition-t.md) | Yes | The position of the node, will be used when executing layout method. |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void
```

Method to measure the DynamicLayout FrameNode and its content to determine the measured size.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void--><!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-na-framenode-c.md) | Yes | The FrameNode of DynamicLayout component. |
| constraint | [LayoutConstraint](arkts-na-framenode-layoutconstraint-i.md) | Yes | The layout constraint of the node, which will be used in measure process. |
| helper | [LazyLayoutHelper](../../apis-arkui/arkts-apis/arkts-arkui-lazylayoutalgorithm-lazylayouthelper-c.md) | No | The helper object for lazy layout algorithm, which provides layout direction and view position information. If undefined, it indicates that the current component is not used under a scrollable component and does not support lazy layout. |

