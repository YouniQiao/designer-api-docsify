# FloatingBallParams

启动和更新闪控球的配置参数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-floatingBall-interface FloatingBallParams--><!--Device-floatingBall-interface FloatingBallParams-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## backgroundColor

```TypeScript
backgroundColor?: string
```

闪控球背景颜色，为不带透明度的十六进制颜色格式（例如'#008EF5'或'#FF008EF5'），不传入时闪控球跟随系统深浅色模式的默认背景色。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallParams-backgroundColor?: string--><!--Device-FloatingBallParams-backgroundColor?: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## content

```TypeScript
content?: string
```

闪控球内容，大小不超过64字节。不传入时默认为空字符串，不显示闪控球内容。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallParams-content?: string--><!--Device-FloatingBallParams-content?: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## contentColor

```TypeScript
contentColor?: string
```

闪控球内容颜色，为不带透明度的十六进制颜色格式（例如'#008EF5'或'#FF008EF5'）。如果背景颜色没有指定，不允许指定内容颜色。

**Type:** string

**Default:** Set different default values according to the 'backgroundColor'. - If 'backgroundColor' is provided, when 'backgroundColor' is light color, default value is '#99FFFFFF', otherwise is '#99000000' - If 'backgroundColor' is not provided, default value is $r('sys.color.font_secondary')

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallParams-contentColor?: string--><!--Device-FloatingBallParams-contentColor?: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## icon

```TypeScript
icon?: image.PixelMap
```

闪控球图标，图标像素的总字节数不超过192KB（图标像素的总字节数通过  
[getPixelBytesNumber](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md#getpixelbytesnumber)获取）。建议图标像素宽高为128px*128px。实际显示效果依赖于设备能力和闪控球UI样式。

**Type:** image.PixelMap

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallParams-icon?: image.PixelMap--><!--Device-FloatingBallParams-icon?: image.PixelMap-End-->

**System capability:** SystemCapability.Window.SessionManager

## template

```TypeScript
template: FloatingBallTemplate
```

闪控球模板。

**Type:** [FloatingBallTemplate](arkts-arkui-floatingball-floatingballtemplate-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallParams-template: FloatingBallTemplate--><!--Device-FloatingBallParams-template: FloatingBallTemplate-End-->

**System capability:** SystemCapability.Window.SessionManager

## textUpdateAnimationType

```TypeScript
textUpdateAnimationType?: FloatingBallTextUpdateAnimationType
```

闪控球文本更新时的动画类型。默认为FloatingBallTextUpdateAnimationType.ANIMATION_NONE。

**Type:** [FloatingBallTextUpdateAnimationType](arkts-arkui-floatingball-floatingballtextupdateanimationtype-e.md)

**Default:** FloatingBallTextUpdateAnimationType.ANIMATION_NONE

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallParams-textUpdateAnimationType?: FloatingBallTextUpdateAnimationType--><!--Device-FloatingBallParams-textUpdateAnimationType?: FloatingBallTextUpdateAnimationType-End-->

**System capability:** SystemCapability.Window.SessionManager

## title

```TypeScript
title: string
```

闪控球标题，不可为空字符串，大小不超过64字节。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallParams-title: string--><!--Device-FloatingBallParams-title: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## titleColor

```TypeScript
titleColor?: string
```

闪控球标题颜色，为不带透明度的十六进制颜色格式（例如'#008EF5'或'#FF008EF5'）。如果背景颜色没有指定，不允许指定标题颜色。

**Type:** string

**Default:** Set different default values according to the 'backgroundColor'. - If 'backgroundColor' is provided, when 'backgroundColor' is light color, default value is '#E5FFFFFF', otherwise is '#E5000000'. - If 'backgroundColor' is not provided, default value is $r('sys.color.font_primary').

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallParams-titleColor?: string--><!--Device-FloatingBallParams-titleColor?: string-End-->

**System capability:** SystemCapability.Window.SessionManager

