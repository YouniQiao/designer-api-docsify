# registerFont

## Modules to Import

```TypeScript
import { font } from '@kit.ArkUI';
```

## registerFont

```TypeScript
function registerFont(options: FontOptions): void
```

Registers a custom font with the font manager.

This API is asynchronous and does not support concurrent calls.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [Font](@ohos.arkui.UIContext) object associated with
> the current UI context.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [registerFont](ohos.arkui.UIContext.Font#registerFont)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-font-function registerFont(options: FontOptions): void--><!--Device-font-function registerFont(options: FontOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FontOptions](arkts-arkui-font-fontoptions-i.md) | Yes | Information about the custom font to register. |

