# PasteButton properties/events

This component can only inherit the [universal attributes of security components]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Only the following events are supported.

**Inheritance/Implementation:** PasteButtonAttribute extends [SecurityComponentMethod<PasteButtonAttribute>](SecurityComponentMethod<PasteButtonAttribute>)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class PasteButtonAttribute extends SecurityComponentMethod<PasteButtonAttribute>--><!--Device-unnamed-declare class PasteButtonAttribute extends SecurityComponentMethod<PasteButtonAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick(event: PasteButtonCallback)
```

Triggered when the paste button is clicked, returning the authorization result. Upon successful authorization, the application obtains temporary permission to read clipboard content. > **NOTE** > - You may want to learn the > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ > to avoid authorization failures caused by incompliant styles.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback): PasteButtonAttribute--><!--Device-PasteButtonAttribute-onClick(event: PasteButtonCallback): PasteButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback for the click event, used to handle the authorization result after the paste button is clicked.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Starting from API version 18, **PasteButtonCallback** is adopted uniformly, which additionally provides error information.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 18 |

