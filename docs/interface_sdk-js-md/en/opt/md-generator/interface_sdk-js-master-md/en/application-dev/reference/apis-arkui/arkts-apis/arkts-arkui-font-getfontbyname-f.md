# getFontByName

## Modules to Import

```TypeScript
```

## getFontByName

```TypeScript
function getFontByName(fontName: string): FontInfo
```

Obtains information about a system font based on the font name. > **NOTE：**> > - Since API version 10, you can use the > [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont) API in > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) to obtain the [Font](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) object associated with > the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** getFontByName

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-font-function getFontByName(fontName: string): FontInfo--><!--Device-font-function getFontByName(fontName: string): FontInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontInfo](arkts-arkui-font-fontinfo-i.md) |
