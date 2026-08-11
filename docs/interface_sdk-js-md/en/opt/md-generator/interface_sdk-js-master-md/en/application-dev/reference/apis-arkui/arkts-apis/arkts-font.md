# @ohos.font(Custom Font Registration)

The **font** module provides APIs for registering custom fonts.

> **NOTE：**
> 
> - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
> where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
> [UIContext](arkts-arkui-uicontext.md).
> 
> - You are advised to use the [loadFontSync](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontcollection-c.md/arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync) API of the
> font engine to register custom fonts.

**Since:** 9

<!--Device-unnamed-declare namespace font--><!--Device-unnamed-declare namespace font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getFontByName](arkts-arkui-font-getfontbyname-f.md#getfontbyname) |
| [getSystemFontList](arkts-arkui-font-getsystemfontlist-f.md#getsystemfontlist) |
| [getUIFontConfig](arkts-arkui-font-getuifontconfig-f.md#getuifontconfig) |
| [registerFont](arkts-arkui-font-registerfont-f.md#registerfont) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FontInfo](arkts-arkui-font-fontinfo-i.md) |
| [FontOptions](arkts-arkui-font-fontoptions-i.md) |
| [UIFontAdjustInfo](arkts-arkui-font-uifontadjustinfo-i.md) |
| [UIFontAliasInfo](arkts-arkui-font-uifontaliasinfo-i.md) |
| [UIFontConfig](arkts-arkui-font-uifontconfig-i.md) |
| [UIFontFallbackGroupInfo](arkts-arkui-font-uifontfallbackgroupinfo-i.md) |
| [UIFontFallbackInfo](arkts-arkui-font-uifontfallbackinfo-i.md) |
| [UIFontGenericInfo](arkts-arkui-font-uifontgenericinfo-i.md) |
