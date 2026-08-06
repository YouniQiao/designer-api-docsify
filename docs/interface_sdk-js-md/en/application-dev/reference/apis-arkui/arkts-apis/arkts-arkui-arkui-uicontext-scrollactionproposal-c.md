# ScrollActionProposal

Class ScrollActionProposal. The default scroll direction is forward.

**Inheritance/Implementation:** ScrollActionProposal extends [TargetedGestureProposal](arkts-arkui-arkui-uicontext-targetedgestureproposal-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ScrollActionProposal extends TargetedGestureProposal--><!--Device-unnamed-export declare class ScrollActionProposal extends TargetedGestureProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(node: FrameNode, distance: double)
```

ScrollActionProposal constructor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollActionProposal-constructor(node: FrameNode, distance: double)--><!--Device-ScrollActionProposal-constructor(node: FrameNode, distance: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The node responding to scroll action. |
| distance | double | Yes | The distance to scroll or slide. |

## distance

```TypeScript
distance: double
```

Distance parameter for gesture operations. Used for actions like scrolling or sliding to specify travel distance.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollActionProposal-distance: double--><!--Device-ScrollActionProposal-distance: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

