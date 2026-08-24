# CustomLayoutAlgorithm

Custom layout algorithm class.

> **NOTE：**&gt;
> The object of the **CustomLayoutAlgorithm** class can be assigned to a variable of the **LayoutAlgorithm** type as
> the input parameter of the
> [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md) component to specify the
> layout algorithm.

**Inheritance/Implementation:** CustomLayoutAlgorithm implements [LayoutAlgorithm](../../apis-default/arkts-apis/arkts-layoutalgorithm-i.md)

**Since:** 24

**Decorator:** @ObservedV2

<!--Device-unnamed-export class CustomLayoutAlgorithm--><!--Device-unnamed-export class CustomLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLayout

```TypeScript
onLayout(self: FrameNode, position: Position): void
```

Customizes the position of the child component to be arranged. When the position of the dynamic layout component is determined, the ArkUI framework will transfer the FrameNode and layout position of the component to you through **onLayout**. State variables should not be changed in this callback.

> **NOTE：**&gt;
> In this callback, you can call
> getChild() of
> FrameNode to obtain the child
> component **FrameNode** and call
> layout() of
> FrameNode to set the position of the
> child component. For details, see
> [Example 1](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md#example-1-implementing-waterfall-layout-using-a-custom-layout-algorithm).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void--><!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | Yes | Entity node of the dynamic layout component in the component tree. |
| position | [Position](arkts-arkui-position-t.md) | Yes | Position information used in layout of the dynamic layout component. |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint): void
```

Customizes the size of the child component to be measured. When the size of the dynamic layout component is determined, the ArkUI framework will transfer the FrameNode and layout constraint of the component to you through **onMeasure**. State variables should not be changed in this callback.

> **NOTE：**&gt;
> In this callback, you can call
> getChild() of
> FrameNode to obtain the child
> component **FrameNode** and call
> measure() of
> FrameNode to measure the size of the
> child component. For details, see
> [Example 1](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md#example-1-implementing-waterfall-layout-using-a-custom-layout-algorithm).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void--><!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](../../apis-default/arkts-apis/arkts-framenode-c.md) | Yes | Entity node of the dynamic layout component in the component tree. |
| constraint | [LayoutConstraint](../../apis-default/arkts-apis/arkts-framenode-layoutconstraint-i.md) | Yes | Layout constraint used by the dynamic layout component for measurement. |

