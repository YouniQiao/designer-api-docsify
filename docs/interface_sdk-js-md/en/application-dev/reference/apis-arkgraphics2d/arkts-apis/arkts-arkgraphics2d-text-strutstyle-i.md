# StrutStyle

支柱样式，用于控制绘制文本的行间距、基线对齐方式以及其他与行高相关的属性，默认不开启。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-interface StrutStyle--><!--Device-text-interface StrutStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## enabled

```TypeScript
enabled?: boolean
```

是否启用支柱样式，true表示使用，false表示不使用，默认为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-enabled?: boolean--><!--Device-StrutStyle-enabled?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontFamilies

```TypeScript
fontFamilies?: Array<string>
```

字体家族名称列表，默认为空，匹配系统字体。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-fontFamilies?: Array<string>--><!--Device-StrutStyle-fontFamilies?: Array<string>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontSize

```TypeScript
fontSize?: double
```

字体大小，浮点数，默认为14.0，单位为物理像素px。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-fontSize?: double--><!--Device-StrutStyle-fontSize?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontStyle

```TypeScript
fontStyle?: FontStyle
```

字体样式，默认为常规样式。

**Type:** [FontStyle](arkts-arkgraphics2d-text-fontstyle-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-fontStyle?: FontStyle--><!--Device-StrutStyle-fontStyle?: FontStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontWeight

```TypeScript
fontWeight?: FontWeight
```

字重，默认为W400。在&lt;!--RP1--&gt;OpenHarmony 6.1&lt;!--RP1End--&gt;之前，仅系统字体中的可变字体支持字重调节；从&lt;!--RP1--&gt;OpenHarmony 6.1&lt;!--RP1End--&gt;开始，系统字体与三方注册字体中的可变字体均支持字重调节。非可变字体设置字重值小于W600时字体粗细无变化，设置字重值大于等于W600时可能会触发伪加粗效果。

**Type:** [FontWeight](../../apis-arkui/arkts-apis/arkts-arkui-fontweight-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-fontWeight?: FontWeight--><!--Device-StrutStyle-fontWeight?: FontWeight-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontWidth

```TypeScript
fontWidth?: FontWidth
```

字体宽度，默认为NORMAL。

**Type:** [FontWidth](arkts-arkgraphics2d-text-fontwidth-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-fontWidth?: FontWidth--><!--Device-StrutStyle-fontWidth?: FontWidth-End-->

**System capability:** SystemCapability.Graphics.Drawing

## forceHeight

```TypeScript
forceHeight?: boolean
```

是否所有行都将使用支柱的高度，true表示使用，false表示不使用，默认为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-forceHeight?: boolean--><!--Device-StrutStyle-forceHeight?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## halfLeading

```TypeScript
halfLeading?: boolean
```

true表示将行间距平分至行的顶部与底部，false则不平分，默认为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-halfLeading?: boolean--><!--Device-StrutStyle-halfLeading?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## height

```TypeScript
height?: double
```

行高缩放倍数，浮点数，默认为1.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-height?: double--><!--Device-StrutStyle-height?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## heightOverride

```TypeScript
heightOverride?: boolean
```

是否覆盖高度，true表示覆盖，false表示不覆盖，默认为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-heightOverride?: boolean--><!--Device-StrutStyle-heightOverride?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## leading

```TypeScript
leading?: double
```

自定义应用于支柱的行距，浮点数，单位为物理像素px，默认为-1.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-StrutStyle-leading?: double--><!--Device-StrutStyle-leading?: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

