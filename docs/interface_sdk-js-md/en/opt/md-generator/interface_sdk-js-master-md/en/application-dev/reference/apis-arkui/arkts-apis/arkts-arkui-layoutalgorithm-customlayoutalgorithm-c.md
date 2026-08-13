# CustomLayoutAlgorithm

Custom layout algorithm class. > **NOTE：**> > The object of the **CustomLayoutAlgorithm** class can be assigned to a variable of the **LayoutAlgorithm** type as > the input parameter of the > [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md) component to specify the > layout algorithm.

**Inheritance/Implementation:** CustomLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md#LayoutAlgorithm)

**Since:** 24

**Deprecated since:** -1

<!--Device-unnamed-export class CustomLayoutAlgorithm--><!--Device-unnamed-export class CustomLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLayout

```TypeScript
onLayout(self: FrameNode, position: Position): void
```

Customizes the position of the child component to be arranged. When the position of the dynamic layout component is determined, the ArkUI framework will transfer the FrameNode and layout position of the component to you through **onLayout**. State variables should not be changed in this callback. > **NOTE：**> > In this callback, you can call > getChild() of > FrameNode to obtain the child > component **FrameNode** and call > layout() of > FrameNode to set the position of the > child component. For details, see > [Example 1](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md#example-1-implementing-waterfall-layout-using-a-custom-layout-algorithm).

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void--><!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| position | [Position](arkts-arkui-position-t.md) | Yes |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint): void
```

Customizes the size of the child component to be measured. When the size of the dynamic layout component is determined, the ArkUI framework will transfer the FrameNode and layout constraint of the component to you through **onMeasure**. State variables should not be changed in this callback. > **NOTE：**> > In this callback, you can call > getChild() of > FrameNode to obtain the child > component **FrameNode** and call > measure() of > FrameNode to measure the size of the > child component. For details, see > [Example 1](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md#example-1-implementing-waterfall-layout-using-a-custom-layout-algorithm).

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void--><!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | Yes |
