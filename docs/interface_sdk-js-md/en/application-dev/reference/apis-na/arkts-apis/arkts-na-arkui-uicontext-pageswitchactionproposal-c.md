# PageSwitchActionProposal

Class PageSwitchActionProposal. The default page switch direction is forward.

**Inheritance/Implementation:** PageSwitchActionProposal extends [TargetedGestureProposal](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-targetedgestureproposal-c.md#TargetedGestureProposal)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class PageSwitchActionProposal--><!--Device-unnamed-export declare class PageSwitchActionProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(node: FrameNode, pageCount: int)
```

PageSwitchActionProposal constructor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageSwitchActionProposal-constructor(node: FrameNode, pageCount: int)--><!--Device-PageSwitchActionProposal-constructor(node: FrameNode, pageCount: int)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | FrameNode | Yes | The node responding to page switch action. |
| pageCount | int | Yes | The number of pages to navigate. The value should be an integer. |

## pageCount

```TypeScript
pageCount: int
```

Page count parameter for gesture operations. Specifies the number of pages to navigate. The value should be an integer.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageSwitchActionProposal-pageCount: int--><!--Device-PageSwitchActionProposal-pageCount: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

