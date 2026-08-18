# PasteButton

**PasteButton** is a security component that provides paste functionality. When users tap this component, the application temporarily gains pasteboard read permissions. <br>**Description**</br>

## Key Enums <li>[PasteIconStyle](arkts-arkui-pasteiconstyle-e.md#pasteiconstyle): Enumeration of icon styles for the paste button. Specifies the icon style displayed.</li> <li>[PasteDescription](arkts-arkui-pastedescription-e.md#pastedescription): Enumeration of text descriptions for the paste button. Specifies the text description displayed.</li> <li>[PasteButtonOnClickResult](arkts-arkui-pastebuttononclickresult-e.md#pastebuttononclickresult): Enumeration of click results for the paste button. Indicates whether authorization succeeds after a click.</li> ###### Key APIs <li>[PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md#pastebuttonoptions): Configuration object for the paste button. Defines properties including icon, text and button type.</li> <li>[PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md#pastebuttoncallback): Callback for paste button clicks. Returns click events, authorization results and error messages.</li> ###### Child Components <li>Not supported.</li></ul>

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md) | Yes |

## Summary

- [PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md)
- [PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md)
- [PasteButtonOnClickResult](arkts-arkui-pastebuttononclickresult-e.md)
- [PasteDescription](arkts-arkui-pastedescription-e.md)
- [PasteIconStyle](arkts-arkui-pasteiconstyle-e.md)
