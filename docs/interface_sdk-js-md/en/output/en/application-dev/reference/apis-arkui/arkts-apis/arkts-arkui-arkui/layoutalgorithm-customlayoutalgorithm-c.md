# CustomLayoutAlgorithm

Custom layout algorithm class. > **NOTE** > > The object of the **CustomLayoutAlgorithm** class can be assigned to a variable of the **LayoutAlgorithm** type as > the input parameter of the > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ component to specify the > layout algorithm.

**Inheritance/Implementation:** CustomLayoutAlgorithm implements [LayoutAlgorithm](layoutalgorithm-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export class CustomLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export class CustomLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLayout

```TypeScript
onLayout(self: FrameNode, position: Position): void
```

Customizes the position of the child component to be arranged. When the position of the dynamic layout component is determined, the ArkUI framework will transfer the FrameNode and layout position of the component to you through **onLayout**. State variables should not be changed in this callback. > **NOTE** > > In this callback, you can call > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ of > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ to obtain the child > component **FrameNode** and call > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ of > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ to set the position of the > child component. For details, see > \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void--><!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Entity node of the dynamic layout component in the component tree. |
| position | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Position information used in layout of the dynamic layout component. |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint): void
```

Customizes the size of the child component to be measured. When the size of the dynamic layout component is determined, the ArkUI framework will transfer the FrameNode and layout constraint of the component to you through **onMeasure**. State variables should not be changed in this callback. > **NOTE** > > In this callback, you can call > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ of > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ to obtain the child > component **FrameNode** and call > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ of > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ to measure the size of the > child component. For details, see > \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void--><!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Entity node of the dynamic layout component in the component tree. |
| constraint | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Layout constraint used by the dynamic layout component for measurement. |

