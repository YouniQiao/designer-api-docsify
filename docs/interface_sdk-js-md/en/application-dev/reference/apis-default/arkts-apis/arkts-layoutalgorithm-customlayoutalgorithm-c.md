# CustomLayoutAlgorithm

Defines the custom layout algorithm.

@implements LayoutAlgorithm

**Inheritance/Implementation:** CustomLayoutAlgorithm implements [LayoutAlgorithm](arkts-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-unnamed-export declare class CustomLayoutAlgorithm--><!--Device-unnamed-export declare class CustomLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLayout

```TypeScript
onLayout(self: FrameNode, position: NodePosition): void
```

Method to assign a position to the DynamicLayout FrameNode and each of its children. It can be used to specify how the DynamicLayout FrameNode and its child nodes are positioned and sized within the layout.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void--><!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | The FrameNode of DynamicLayout component. |
| position | [NodePosition](arkts-nodeposition-t.md) | Yes | The position of the node, will be used when executing layout method. |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint): void
```

Method to measure the DynamicLayout FrameNode and its content to determine the measured size.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void--><!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Yes | The FrameNode of DynamicLayout component. |
| constraint | [LayoutConstraint](../../apis-arkui/arkts-apis/arkts-arkui-framenode-layoutconstraint-i.md) | Yes | The layout constraint of the node, which will be used in measure process. |

