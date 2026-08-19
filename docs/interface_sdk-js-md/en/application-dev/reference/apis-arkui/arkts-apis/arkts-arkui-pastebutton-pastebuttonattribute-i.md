# PasteButtonAttribute

Declare interfaces for the attributes of the paste button.

**Inheritance/Implementation:** PasteButtonAttribute extends SecurityComponentMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface PasteButtonAttribute--><!--Device-unnamed-export declare interface PasteButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick(event: PasteButtonCallback | undefined): this
```

Called when the paste button is clicked.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback | undefined): this--><!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteButtonAttribute](arkts-arkui-pastebutton-pastebuttonattribute-i.md) | Returns the attribute of the paste button. |

