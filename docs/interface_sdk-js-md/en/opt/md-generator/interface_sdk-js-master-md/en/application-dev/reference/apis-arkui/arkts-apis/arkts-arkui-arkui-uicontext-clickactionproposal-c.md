# ClickActionProposal

Smart gesture click action handling. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkui-uicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkui-uicontext-gesturehandlingresolution-c.md#gesturehandlingresolution)'s **selectedProposal** to an object of this type triggers a click operation on the target component. > **NOTE：**> > - This action handling follows the "select first, then click" processing semantics. > > - If the target node is not yet selected, this handling first establishes the selected state without immediately > triggering the click.

**Inheritance/Implementation:** ClickActionProposal extends [TargetedGestureProposal](arkts-arkui-arkui-uicontext-targetedgestureproposal-c.md#targetedgestureproposal)

**Since:** 26.0.0

<!--Device-unnamed-export class ClickActionProposal--><!--Device-unnamed-export class ClickActionProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(node: FrameNode)
```

Constructor for the smart gesture click action handling.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ClickActionProposal-constructor(node: FrameNode)--><!--Device-ClickActionProposal-constructor(node: FrameNode)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
