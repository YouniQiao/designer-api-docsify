# StackLayoutAlgorithm

Defines the stack layout algorithm.

@implements LayoutAlgorithm

**Inheritance/Implementation:** StackLayoutAlgorithm implements [LayoutAlgorithm](arkts-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-unnamed-export declare class StackLayoutAlgorithm--><!--Device-unnamed-export declare class StackLayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: StackLayoutAlgorithmOptions)
```

Constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StackLayoutAlgorithm-constructor(option?: StackLayoutAlgorithmOptions)--><!--Device-StackLayoutAlgorithm-constructor(option?: StackLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [StackLayoutAlgorithmOptions](arkts-layoutalgorithm-stacklayoutalgorithmoptions-i.md) | No | set properties of stack layout algorithm. |

## alignContent

```TypeScript
@Trace public alignContent?: LocalizedAlignment
```

The align rules of child components in stack layout algorithm.

**Type:** [LocalizedAlignment](arkts-enums-localizedalignment-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StackLayoutAlgorithm-@Trace public alignContent?: LocalizedAlignment--><!--Device-StackLayoutAlgorithm-@Trace public alignContent?: LocalizedAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

