# setTextHighContrast

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## setTextHighContrast

```TypeScript
function setTextHighContrast(action : TextHighContrast): void
```

用于设置文字渲染高对比度模式。

该接口设置后整个进程都会生效，进程内所有页面共用相同模式。

可调用此接口设置，也可通过系统设置界面中**高对比度文字配置开关**进行开启/关闭。使用此接口设置开启/关闭文字渲染高对比度配置的优先级高于系统开关设置。

该接口针对应用通过Canvas等接口自行绘制文字的场景不生效，仅对使用系统文本组件渲染的场景生效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-text-function setTextHighContrast(action : TextHighContrast): void--><!--Device-text-function setTextHighContrast(action : TextHighContrast): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | [TextHighContrast](arkts-arkgraphics2d-text-texthighcontrast-e.md) | Yes | 文字渲染高对比度模式。 |

## Examples

```TypeScript
text.setTextHighContrast(text.TextHighContrast.TEXT_APP_DISABLE_HIGH_CONTRAST)
```

