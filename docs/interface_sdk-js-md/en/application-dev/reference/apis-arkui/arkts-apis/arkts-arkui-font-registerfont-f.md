# registerFont

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## registerFont

```TypeScript
function registerFont(options: FontOptions): void
```

在字体管理中注册自定义字体。

该接口为异步接口，不支持并发调用。

> **说明：**
> 
> -registerFont需要先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont)方法获取
> [Font](arkts-arkui-uicontext.md)对象，然后通过该对象进行调用。且直接使用registerFont可能导致
> [UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的问题。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的
> [Font](arkts-arkui-uicontext.md)对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.Font#registerFont

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-font-function registerFont(options: FontOptions): void--><!--Device-font-function registerFont(options: FontOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FontOptions](arkts-arkui-font-fontoptions-i.md) | Yes | 注册的自定义字体信息。 |

