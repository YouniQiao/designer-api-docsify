# getFontByName

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## getFontByName

```TypeScript
function getFontByName(fontName: string): FontInfo
```

根据传入的系统字体名称获取系统字体的相关信息。

> **说明：**
> 
> -getFontByName需要先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont)方法获取
> [Font](arkts-arkui-uicontext.md)对象，然后通过该对象进行调用。且直接使用getFontByName可能导致
> [UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的问题。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的
> [Font](arkts-arkui-uicontext.md)对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.Font#getFontByName

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-font-function getFontByName(fontName: string): FontInfo--><!--Device-font-function getFontByName(fontName: string): FontInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontName | string | Yes | 系统的字体名。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FontInfo](arkts-arkui-font-fontinfo-i.md) | 字体的详细信息。 |

