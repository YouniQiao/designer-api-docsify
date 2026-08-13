# LazyCustomLayoutAlgorithm

Defines the lazy custom layout algorithm.

**Inheritance/Implementation:** LazyCustomLayoutAlgorithm implements [LazyLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-lazylayoutalgorithm-i.md#LazyLayoutAlgorithm)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class LazyCustomLayoutAlgorithm--><!--Device-unnamed-export class LazyCustomLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: LazyCustomLayoutAlgorithmOptions)
```

Constructor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)--><!--Device-LazyCustomLayoutAlgorithm-constructor(option?: LazyCustomLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [LazyCustomLayoutAlgorithmOptions](../../apis-na/arkts-apis/arkts-na-lazylayoutalgorithm-lazycustomlayoutalgorithmoptions-i.md) | No | set properties of lazy custom layout algorithm. |

## onLayout

```TypeScript
onLayout(self: FrameNode, position: Position): void
```

Method to assign a position to the DynamicLayout FrameNode and each of its children. It can be used to specify the layout location of DynamicLayout FrameNode and its children.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void--><!--Device-LazyCustomLayoutAlgorithm-onLayout(self: FrameNode, position: Position): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes | The FrameNode of DynamicLayout component. |
| position | [Position](arkts-arkui-position-t.md) | Yes | The position of the node, will be used when executing layout method. |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void
```

Method to measure the DynamicLayout FrameNode and its content to determine the measured size.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void--><!--Device-LazyCustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes | The FrameNode of DynamicLayout component. |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | Yes | The layout constraint of the node, which will be used in measure process. |
| helper | [LazyLayoutHelper](../../apis-na/arkts-apis/arkts-na-lazylayoutalgorithm-lazylayouthelper-c.md) | No | The helper object for lazy layout algorithm, which provides layout direction and view position information. If undefined, it indicates that the current component is not used under a scrollable component and does not support lazy layout. |

