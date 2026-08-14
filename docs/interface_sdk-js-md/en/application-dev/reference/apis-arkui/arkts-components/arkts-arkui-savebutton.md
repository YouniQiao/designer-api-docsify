# SaveButton

**SaveButton** is a system API for the save security control. It applies to scenarios where apps need temporary media library access permissions to save images or videos, such as saving images to albums and exporting media content. After the **SaveButton** component is integrated into an app, a confirmation dialog will appear when the user taps the component for the first time. If the user allows access, the app obtains temporary authorization to call media library APIs. For related APIs, see [Interface (PhotoAccessHelper)](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#PhotoAccessHelper). If the user denies access or dismisses the dialog, authorization will not be granted for this operation. No more dialog box is displayed for authorization. <br> For API version 19 and earlier, the authorization duration is 10 seconds. For API version 20 and later, the authorization duration is 1 minute. You need to call media library APIs to obtain file handles and complete temporary-authorized operations such as creating media resources within the authorization period. After authorization expires, existing file handles acquired during the valid period remain available for read and write operations. <br>**Description**</br>

## Key Enums <li>[SaveIconStyle](arkts-arkui-saveiconstyle-e.md#SaveIconStyle): Enumeration of icon styles for the save button. Specifies the icon style displayed.</li> <li>[SaveDescription](arkts-arkui-savedescription-e.md#SaveDescription): Enumeration of text descriptions for the save button. Specifies the text description displayed.</li> <li>[SaveButtonOnClickResult](arkts-arkui-savebuttononclickresult-e.md#SaveButtonOnClickResult): Enumeration of click results for the save button. Indicates whether authorization succeeds after a click.</li> ###### Key APIs <li>[SaveButtonOptions](arkts-arkui-savebuttonoptions-i.md#SaveButtonOptions): Configuration object for the save button. Defines properties including icon, text and button type.</li> <li>[SaveButtonCallback](arkts-arkui-savebuttoncallback-t.md#SaveButtonCallback): Callback for save button clicks. Returns click events, authorization results and error messages.</li> ###### Child Components <li>Not supported.</li></ul>

## SaveButton

```TypeScript
SaveButton()
```

Creates a **SaveButton** component with an icon, text, and background. When the user taps the save button for the first time, a dialog will pop up. Once the user grants permission, the app obtains temporary authorization to access media library APIs. No dialog box will appear for subsequent uses. <br>In API version 19 or earlier, authorization remains valid for 10 seconds. After authorization expires, existing file handles acquired during the valid period remain available for read and write operations. <br>In API version 20 or later, authorization remains valid for 1 minute. After authorization expires, existing file handles acquired during the valid period remain available for read and write operations. <br>**Description**&lt;/br&gt; &lt;ul&gt;&lt;li&gt;You may want to learn the [restrictions on security component styles](../../../security/AccessToken/security-component-overview.md#constraints) to avoid authorization failures caused by incompliant styles.&lt;/li&gt;&lt;/ul&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonInterface-(): SaveButtonAttribute--><!--Device-SaveButtonInterface-(): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SaveButton

```TypeScript
SaveButton(options: SaveButtonOptions)
```

Creates a save button with the specified icon, text and button type. When the user taps the save button for the first time, a dialog will pop up. Once the user grants permission, the app obtains temporary authorization to access media library APIs. No dialog box will appear for subsequent uses. <br>In API version 19 or earlier, authorization remains valid for 10 seconds. After authorization expires, existing file handles acquired during the valid period remain available for read and write operations. <br>In API version 20 or later, authorization remains valid for 1 minute. After authorization expires, existing file handles acquired during the valid period remain available for read and write operations. <br>**Description**&lt;/br&gt; &lt;ul&gt;&lt;li&gt;You may want to learn the [restrictions on security component styles](../../../security/AccessToken/security-component-overview.md#constraints) to avoid authorization failures caused by incompliant styles.&lt;/li&gt;&lt;/ul&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonInterface-(options: SaveButtonOptions): SaveButtonAttribute--><!--Device-SaveButtonInterface-(options: SaveButtonOptions): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SaveButtonOptions](arkts-arkui-savebuttonoptions-i.md) | Yes | Configuration options for the save button, used to set properties such as icon, text and button type. <br>You are advised to explicitly set at least one of **icon** and **text** to help users identify the button. If both are not specified, the component uses the default style. |

## Summary

- [SaveButtonOptions](arkts-arkui-savebuttonoptions-i.md)
- [SaveButtonCallback](arkts-arkui-savebuttoncallback-t.md)
- [SaveButtonOnClickResult](arkts-arkui-savebuttononclickresult-e.md)
- [SaveDescription](arkts-arkui-savedescription-e.md)
- [SaveIconStyle](arkts-arkui-saveiconstyle-e.md)
