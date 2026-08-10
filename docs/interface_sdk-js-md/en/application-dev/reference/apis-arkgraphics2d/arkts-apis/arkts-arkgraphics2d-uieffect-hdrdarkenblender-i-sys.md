# HdrDarkenBlender (System API)

支持HDR的压暗混合器，用于将压暗效果添加到指定的组件上。在调用HdrDarkenBlender前，需要先通过createHdrDarkenBlender创建一个HdrDarkenBlender实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-uiEffect-interface HdrDarkenBlender--><!--Device-uiEffect-interface HdrDarkenBlender-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## grayscaleFactor

```TypeScript
grayscaleFactor?: [double, double, double]
```

将RGB颜色转换为灰度值。灰度转换公式的权重可随当前色域自动调整，不同色域下使用不同的权重计算方式；适用于sRGB等标准色域场景。当需要根据特定色域或视觉效果自定义灰度转换权重时传入此参数。三个分量均无边界限制。默认值为标准灰度权重[0.299, 0.587, 0.114]。

**Type:** [double, double, double]

**Default:** [0.299, 0.587, 0.114]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrDarkenBlender-grayscaleFactor?: [double, double, double]--><!--Device-HdrDarkenBlender-grayscaleFactor?: [double, double, double]-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## hdrBrightnessRatio

```TypeScript
hdrBrightnessRatio: double
```

HDR的提亮倍数。取值范围为[1.0, 设备当前支持最大提亮倍数]。设置小于1.0的值时，按值为1.0处理；当值等于1.0时，为组件原本亮度；设置大于设备当前支持最大提亮倍数的值时，按值为设备当前支持最大提亮倍数处理，支持最大提亮倍数 = 设备最大亮度 / 设备默认亮度。设备最大亮度通过hdc命令获取：hdc shell param get const.display.brightness.max设备默认亮度通过hdc命令获取：hdc shell param get const.display.brightness.default

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrDarkenBlender-hdrBrightnessRatio: double--><!--Device-HdrDarkenBlender-hdrBrightnessRatio: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

