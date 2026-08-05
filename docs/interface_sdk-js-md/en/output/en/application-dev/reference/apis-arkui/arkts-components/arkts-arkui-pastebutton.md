# PasteButton

**PasteButton** is a security component that provides paste functionality. When users tap this component, the application temporarily gains pasteboard read permissions. <br>**Description**</br>

## Key Enums <li>[PasteIconStyle]{@link PasteIconStyle}: Enumeration of icon styles for the paste button. Specifies the icon style displayed.</li> <li>[PasteDescription]{@link PasteDescription}: Enumeration of text descriptions for the paste button. Specifies the text description displayed.</li> <li>[PasteButtonOnClickResult]{@link PasteButtonOnClickResult}: Enumeration of click results for the paste button. Indicates whether authorization succeeds after a click.</li> ###### Key APIs <li>[PasteButtonOptions]{@link PasteButtonOptions}: Configuration object for the paste button. Defines properties including icon, text and button type.</li> <li>[PasteButtonCallback]{@link PasteButtonCallback}: Callback for paste button clicks. Returns click events, authorization results and error messages.</li> ###### Child Components <li>Not supported.</li></ul>

## PasteButton

```TypeScript
PasteButton()
```

Creates a **PasteButton** component with an icon, text, and background by default. After creation, the system triggers an authorization check when the button is tapped. Upon successful authorization, the application gains permission to read the current clipboard content. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**Description**\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_You may want to learn the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to avoid authorization failures caused by incompliant styles.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteButtonInterface-(): PasteButtonAttribute--><!--Device-PasteButtonInterface-(): PasteButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PasteButton

```TypeScript
PasteButton(options: PasteButtonOptions)
```

Creates a paste button with the specified icon, text and button type. After creation, the system triggers an authorization check when the button is tapped. Upon successful authorization, the app gains temporary permission to read the clipboard. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**Description**\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_You may want to learn the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to avoid authorization failures caused by incompliant styles.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteButtonInterface-(options: PasteButtonOptions): PasteButtonAttribute--><!--Device-PasteButtonInterface-(options: PasteButtonOptions): PasteButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Configuration options for the paste button, used to set properties such as icon, text and button type. \_\_\_HTML\_TAG\_USD\_0\_\_\_You are advised to explicitly set at least one of **icon** or **text** to help users identify the button. \_\_\_HTML\_TAG\_USD\_1\_\_\_If neither **icon** nor **text** is specified, **options** does not take effect and the button is displayed in the default style.\_\_\_HTML\_TAG\_USD\_2\_\_\_{\_\_\_HTML\_TAG\_USD\_3\_\_\_icon: PasteIconStyle.LINES,\_\_\_HTML\_TAG\_USD\_4\_\_\_text:PasteDescription.PASTE, \_\_\_HTML\_TAG\_USD\_5\_\_\_buttonType: ButtonType.Capsule \_\_\_HTML\_TAG\_USD\_6\_\_\_}.  |

## Summary

