# CustomLayoutAlgorithm

Defines the custom layout algorithm.

**Inheritance/Implementation:** CustomLayoutAlgorithm implements [LayoutAlgorithm](layoutalgorithm-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class CustomLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class CustomLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLayout

```TypeScript
onLayout(self: FrameNode, position: NodePosition): void
```

Method to assign a position to the DynamicLayout FrameNode and each of its children.It can be used to specify how the DynamicLayout FrameNode and its child nodes are positioned and sized within the layout.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void--><!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The FrameNode of DynamicLayout component. |
| position | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The position of the node, will be used when executing layout method. |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint): void
```

Method to measure the DynamicLayout FrameNode and its content to determine the measured size.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void--><!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The FrameNode of DynamicLayout component. |
| constraint | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The layout constraint of the node, which will be used in measure process. |

