# PasteButtonAttribute

Declare interfaces for the attributes of the paste button.

**Inheritance/Implementation:** PasteButtonAttribute extends [SecurityComponentMethod](securitycomponent-securitycomponentmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PasteButtonAttribute extends SecurityComponentMethod--><!--Device-unnamed-export declare interface PasteButtonAttribute extends SecurityComponentMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick(event: PasteButtonCallback | undefined): this
```

Called when the paste button is clicked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback | undefined): this--><!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attribute of the paste button. |

