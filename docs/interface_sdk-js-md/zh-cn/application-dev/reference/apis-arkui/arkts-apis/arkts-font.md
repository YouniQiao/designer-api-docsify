# @ohos.font(Custom Font Registration)

本模块提供注册自定义字体。

> **说明：**&gt;
> - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)说明。&gt;
> - 推荐使用字体引擎的[loadFontSync](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync)接口注册自定义字体。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { font } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getFontByName(Custom Font Registration)](arkts-arkui-font-getfontbyname-f.md) |
| [getSystemFontList(Custom Font Registration)](arkts-arkui-font-getsystemfontlist-f.md) |
| [getUIFontConfig(Custom Font Registration)](arkts-arkui-font-getuifontconfig-f.md) |
| [registerFont(Custom Font Registration)](arkts-arkui-font-registerfont-f.md) |

### 接口

| 名称 |
| --- |
| [FontInfo(Custom Font Registration)](arkts-arkui-font-fontinfo-i.md) |
| [FontOptions(Custom Font Registration)](arkts-arkui-font-fontoptions-i.md) |
| [UIFontAdjustInfo(Custom Font Registration)](arkts-arkui-font-uifontadjustinfo-i.md) |
| [UIFontAliasInfo(Custom Font Registration)](arkts-arkui-font-uifontaliasinfo-i.md) |
| [UIFontConfig(Custom Font Registration)](arkts-arkui-font-uifontconfig-i.md) |
| [UIFontFallbackGroupInfo(Custom Font Registration)](arkts-arkui-font-uifontfallbackgroupinfo-i.md) |
| [UIFontFallbackInfo(Custom Font Registration)](arkts-arkui-font-uifontfallbackinfo-i.md) |
| [UIFontGenericInfo(Custom Font Registration)](arkts-arkui-font-uifontgenericinfo-i.md) |
