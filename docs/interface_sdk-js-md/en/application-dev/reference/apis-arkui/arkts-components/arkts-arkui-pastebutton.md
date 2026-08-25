# PasteButton

**PasteButton** is a security component that provides paste functionality. When users tap this component, the application temporarily gains pasteboard read permissions. 
**Description**</br>

## Key Enums

&lt;li&gt;[PasteIconStyle](arkts-arkui-pasteiconstyle-e.md): Enumeration of icon styles for the paste button. Specifies the icon style displayed.&lt;/li&gt; &lt;li&gt;[PasteDescription](arkts-arkui-pastedescription-e.md): Enumeration of text descriptions for the paste button. Specifies the text description displayed.&lt;/li&gt; &lt;li&gt;[PasteButtonOnClickResult](arkts-arkui-pastebuttononclickresult-e.md): Enumeration of click results for the paste button. Indicates whether authorization succeeds after a click.&lt;/li&gt;

## Key APIs

&lt;li&gt;[PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md): Configuration object for the paste button. Defines properties including icon, text and button type.&lt;/li&gt; &lt;li&gt;[PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md): Callback for paste button clicks. Returns click events, authorization results and error messages.&lt;/li&gt;

## Child Components

&lt;li&gt;Not supported.&lt;/li&gt;&lt;/ul&gt;

## PasteButton

```TypeScript
PasteButton()
```

Creates a **PasteButton** component with an icon, text, and background by default. After creation, the system triggers an authorization check when the button is tapped. Upon successful authorization, the application gains permission to read the current clipboard content.   
**Description**&lt;/br&gt; &lt;ul&gt;&lt;li&gt;You may want to learn the [restrictions on security component styles](../../../security/AccessToken/security-component-overview.md#constraints) to avoid authorization failures caused by incompliant styles.&lt;/li&gt;&lt;/ul&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PasteButton

```TypeScript
PasteButton(options: PasteButtonOptions)
```

Creates a paste button with the specified icon, text and button type. After creation, the system triggers an authorization check when the button is tapped. Upon successful authorization, the app gains temporary permission to read the clipboard.   
**Description**&lt;/br&gt; &lt;ul&gt;&lt;li&gt;You may want to learn the [restrictions on security component styles](../../../security/AccessToken/security-component-overview.md#constraints) to avoid authorization failures caused by incompliant styles.&lt;/li&gt;&lt;/ul&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [PasteButtonOptions](arkts-arkui-pastebuttonoptions-i.md) | Yes |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
