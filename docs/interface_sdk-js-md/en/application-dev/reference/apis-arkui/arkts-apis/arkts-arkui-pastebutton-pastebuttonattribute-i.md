# PasteButtonAttribute

Declare interfaces for the attributes of the paste button.@extends SecurityComponentMethod @interface PasteButtonAttribute

**Inheritance/Implementation:** PasteButtonAttribute extends SecurityComponentMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick(event: PasteButtonCallback | undefined): this
```

Called when the paste button is clicked.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteButtonAttribute](arkts-arkui-pastebutton-pastebuttonattribute-i.md) |
