# OnWillScrollCallback

```TypeScript
export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)
```

Called before scroll to allow developer to control real offset the Scrollable can scroll.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scrollOffset | double | Yes |
| scrollState | [ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md) | Yes |
| scrollSource | [ScrollSource](arkts-arkui-scrollsource-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| (undefined \| ScrollResult) |
