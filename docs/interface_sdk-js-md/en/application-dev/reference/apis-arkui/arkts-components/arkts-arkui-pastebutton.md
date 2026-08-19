# PasteButton

**PasteButton** is a security component that provides paste functionality. When users tap this component, the application temporarily gains pasteboard read permissions. <br>**Description**</br>

## Key Enums <li>[PasteIconStyle](arkts-arkui-pasteiconstyle-e.md): Enumeration of icon styles for the paste button. Specifies the icon style displayed.</li> <li>[PasteDescription](arkts-arkui-pastedescription-e.md): Enumeration of text descriptions for the paste button. Specifies the text description displayed.</li> <li>[PasteButtonOnClickResult](arkts-arkui-pastebuttononclickresult-e.md): Enumeration of click results for the paste button. Indicates whether authorization succeeds after a click.</li> ###### Key APIs <li>[PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md): Configuration object for the paste button. Defines properties including icon, text and button type.</li> <li>[PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md): Callback for paste button clicks. Returns click events, authorization results and error messages.</li> ###### Child Components <li>Not supported.</li></ul>

## PasteButton

```TypeScript
PasteButton()
```

Creates a **PasteButton** component with an icon, text, and background by default. After creation, the system triggers an authorization check when the button is tapped. Upon successful authorization, the application gains permission to read the current clipboard content. <br>**Description**&lt;/br&gt; &lt;ul&gt;&lt;li&gt;You may want to learn the [restrictions on security component styles](../../../security/AccessToken/security-component-overview.md#constraints) to avoid authorization failures caused by incompliant styles.&lt;/li&gt;&lt;/ul&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteButtonInterface-(): PasteButtonAttribute--><!--Device-PasteButtonInterface-(): PasteButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PasteButton

```TypeScript
PasteButton(options: PasteButtonOptions)
```

Creates a paste button with the specified icon, text and button type. After creation, the system triggers an authorization check when the button is tapped. Upon successful authorization, the app gains temporary permission to read the clipboard. <br>**Description**&lt;/br&gt; &lt;ul&gt;&lt;li&gt;You may want to learn the [restrictions on security component styles](../../../security/AccessToken/security-component-overview.md#constraints) to avoid authorization failures caused by incompliant styles.&lt;/li&gt;&lt;/ul&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteButtonInterface-(options: PasteButtonOptions): PasteButtonAttribute--><!--Device-PasteButtonInterface-(options: PasteButtonOptions): PasteButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md) | Yes | Configuration options for the paste button, used to set properties such as icon, text and button type. <br>You are advised to explicitly set at least one of **icon** or **text** to help users identify the button. <br>If neither **icon** nor **text** is specified, **options** does not take effect and the button is displayed in the default style.<br>{<br>icon: PasteIconStyle.LINES,<br>text:PasteDescription.PASTE, <br>buttonType: ButtonType.Capsule <br>}. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md) | Defines options for the paste button, including icon, text and button type. &gt; **NOTE：**&gt; &gt; - You are advised to specify at least one of **icon** or **text**. &gt; - If neither **icon** nor **text** is specified, **PasteButton** is created with default styles as follows: &gt; **PasteIconStyle** defaults to **LINES**, **PasteDescription** to **PASTE**, and **ButtonType** to **Capsule**. &gt; - The **icon**, **text**, and **buttonType** parameters do not support dynamic modification. Styles and properties &gt; of security components are verified by the system upon creation. Dynamic changes may cause the component to &gt; violate specifications for security components and invalidate authorization. |

### Types

| Name | Description |
| --- | --- |
| [PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md) | Triggered when the **PasteButton** component is clicked. |

### Enums

| Name | Description |
| --- | --- |
| [PasteButtonOnClickResult](arkts-arkui-pastebuttononclickresult-e.md) | Enumerates the authorization results after the **PasteButton** component is tapped. |
| [PasteDescription](arkts-arkui-pastedescription-e.md) | Enumerates the text that can be displayed on the paste button. |
| [PasteIconStyle](arkts-arkui-pasteiconstyle-e.md) | Enumerates icon styles of the **PasteButton** component. |

