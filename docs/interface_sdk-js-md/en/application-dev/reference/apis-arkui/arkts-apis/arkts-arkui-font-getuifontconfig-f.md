# getUIFontConfig

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## getUIFontConfig

```TypeScript
function getUIFontConfig(): UIFontConfig
```

获取系统字体配置文件的UI字体配置信息。

该接口仅支持获取配置文件内的信息以及当UI上下文不明确时可能返回undefined，如果想要获取全量的字体配置信息，推荐使用字体引擎的  
[getSystemFontFullNamesByType](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#textgetsystemfontfullnamesbytype14)接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-font-function getUIFontConfig(): UIFontConfig--><!--Device-font-function getUIFontConfig(): UIFontConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIFontConfig](arkts-arkui-font-uifontconfig-i.md) | Returns the ui font config |

