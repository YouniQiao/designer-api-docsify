# PageSwitchActionProposal

Class PageSwitchActionProposal. The default page switch direction is forward.

**Inheritance/Implementation:** PageSwitchActionProposal extends [TargetedGestureProposal](arkts-arkui-arkui-uicontext-targetedgestureproposal-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class PageSwitchActionProposal extends TargetedGestureProposal--><!--Device-unnamed-export declare class PageSwitchActionProposal extends TargetedGestureProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(node: FrameNode, pageCount: int)
```

PageSwitchActionProposal constructor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageSwitchActionProposal-constructor(node: FrameNode, pageCount: int)--><!--Device-PageSwitchActionProposal-constructor(node: FrameNode, pageCount: int)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The node responding to page switch action. |
| pageCount | int | Yes | The number of pages to navigate.The value should be an integer. |

## pageCount

```TypeScript
pageCount: int
```

Page count parameter for gesture operations. Specifies the number of pages to navigate. The value should be an integer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageSwitchActionProposal-pageCount: int--><!--Device-PageSwitchActionProposal-pageCount: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

