# @ohos.font

注册自定义字体


**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace font--><!--Device-unnamed-declare namespace font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getUIFontConfig](arkts-arkui-font-getuifontconfig-f.md#getuifontconfig) | 获取系统字体配置文件的UI字体配置信息。  该接口仅支持获取配置文件内的信息以及当UI上下文不明确时可能返回undefined，如果想要获取全量的字体配置信息，推荐使用字体引擎的  [getSystemFontFullNamesByType](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#textgetsystemfontfullnamesbytype14)接口。 |

### Interfaces

| Name | Description |
| --- | --- |
| [FontInfo](arkts-arkui-font-fontinfo-i.md) |  |
| [FontOptions](arkts-arkui-font-fontoptions-i.md) |  |
| [UIFontAdjustInfo](arkts-arkui-font-uifontadjustinfo-i.md) |  |
| [UIFontAliasInfo](arkts-arkui-font-uifontaliasinfo-i.md) |  |
| [UIFontConfig](arkts-arkui-font-uifontconfig-i.md) |  |
| [UIFontFallbackGroupInfo](arkts-arkui-font-uifontfallbackgroupinfo-i.md) |  |
| [UIFontFallbackInfo](arkts-arkui-font-uifontfallbackinfo-i.md) |  |
| [UIFontGenericInfo](arkts-arkui-font-uifontgenericinfo-i.md) |  |

