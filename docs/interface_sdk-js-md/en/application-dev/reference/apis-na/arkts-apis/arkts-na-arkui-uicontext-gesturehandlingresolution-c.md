# GestureHandlingResolution

Class GestureHandlingResolution. Represents the developer's decision result for smart gesture handling.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class GestureHandlingResolution--><!--Device-unnamed-export declare class GestureHandlingResolution-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(isConsumed: boolean)
```

GestureHandlingResolution constructor.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureHandlingResolution-constructor(isConsumed: boolean)--><!--Device-GestureHandlingResolution-constructor(isConsumed: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isConsumed | boolean | Yes | Whether to consume the current gesture event. |

## isConsumed

```TypeScript
isConsumed: boolean
```

Determines whether to consume the current gesture event. If the gesture is not consumed, it will inform the consumer that the gesture is not supported.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureHandlingResolution-isConsumed: boolean--><!--Device-GestureHandlingResolution-isConsumed: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedProposal

```TypeScript
selectedProposal?: BaseGestureHandlingProposal
```

The final gesture handling proposal selected by the developer.

**Type:** [BaseGestureHandlingProposal](arkts-na-arkui-uicontext-basegesturehandlingproposal-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureHandlingResolution-selectedProposal?: BaseGestureHandlingProposal--><!--Device-GestureHandlingResolution-selectedProposal?: BaseGestureHandlingProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

