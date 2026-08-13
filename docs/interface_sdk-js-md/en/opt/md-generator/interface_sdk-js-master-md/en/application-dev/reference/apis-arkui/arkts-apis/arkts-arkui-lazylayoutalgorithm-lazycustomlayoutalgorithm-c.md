# LazyCustomLayoutAlgorithm

Defines the lazy custom layout algorithm.

**Inheritance/Implementation:** LazyCustomLayoutAlgorithm implements [LazyLayoutAlgorithm](arkts-arkui-lazylayoutalgorithm-i.md#LazyLayoutAlgorithm)

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-unnamed-export class LazyCustomLayoutAlgorithm--><!--Device-unnamed-export class LazyCustomLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: LazyCustomLayoutAlgorithmOptions)
```

Constructor.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)--><!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [LazyCustomLayoutAlgorithmOptions](arkts-arkui-lazylayoutalgorithm-lazycustomlayoutalgorithmoptions-i.md) | No |

## onLayout

```TypeScript
onLayout(self: FrameNode, position: Position): void
```

Method to assign a position to the DynamicLayout FrameNode and each of its children. It can be used to specify the layout location of DynamicLayout FrameNode and its children.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void--><!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| position | [Position](arkts-arkui-position-t.md) | Yes |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void
```

Method to measure the DynamicLayout FrameNode and its content to determine the measured size.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void--><!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | Yes |
| helper | [LazyLayoutHelper](arkts-arkui-lazylayoutalgorithm-lazylayouthelper-c.md) | No |
