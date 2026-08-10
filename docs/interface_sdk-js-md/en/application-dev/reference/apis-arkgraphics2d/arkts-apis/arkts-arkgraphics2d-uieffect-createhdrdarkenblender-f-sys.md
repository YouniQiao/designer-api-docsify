# createHdrDarkenBlender (System API)

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createHdrDarkenBlender

```TypeScript
function createHdrDarkenBlender(hdrBrightnessRatio: double,
    grayscaleFactor?: [double, double, double]): HdrDarkenBlender
```

创建HdrDarkenBlender实例用于HDR图层的压暗混合效果。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiEffect-function createHdrDarkenBlender(hdrBrightnessRatio: double,    grayscaleFactor?: [double, double, double]): HdrDarkenBlender--><!--Device-uiEffect-function createHdrDarkenBlender(hdrBrightnessRatio: double,    grayscaleFactor?: [double, double, double]): HdrDarkenBlender-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hdrBrightnessRatio | double | Yes | HDR的提亮倍数。取值范围为[1.0, 设备当前支持最大提亮倍数]。 设置小于1.0的值时，按值为1.0处理；当值等于1.0时，为组件原本亮度； 设置大于设备当前支持最大提亮倍数的值时，按值为设备当前支持最大提亮倍数处理， 支持最大提亮倍数 = 设备最大亮度 / 设备默认亮度。 设备最大亮度通过hdc命令获取：hdc shell param get const.display.brightness.max 设备默认亮度通过hdc命令获取：hdc shell param get const.display.brightness.default |
| grayscaleFactor | [double, double, double] | No | 将RGB颜色转换为灰度值。灰度转换公式的权重 可随当前色域自动调整，不同色域下使用不同的权重计算方式； 适用于sRGB等标准色域场景。当需要根据特定色域或视觉效果自定义灰度转换权重时传入此参数。 三个分量均无边界限制。默认值为标准灰度权重[0.299, 0.587, 0.114]。 |

**Return value:**

| Type | Description |
| --- | --- |
| [HdrDarkenBlender](arkts-arkgraphics2d-uieffect-hdrdarkenblender-i-sys.md) | 返回HDR压暗混合器，用于将压暗效果添加到指定的组件上。 |

## Examples

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D'

// Create an HDR darken blender instance.
let blender : uiEffect.HdrDarkenBlender = 
  uiEffect.createHdrDarkenBlender(1.3, [0.299, 0.587, 0.114])

@Entry
@Component
struct Example {
  build() { 
    RelativeContainer() { 
      Stack(){ 
          Text("TextWord") 
          Image($r("app.media.screenshot")) 
            .width("100%") 
            .height("100%") 
            .advancedBlendMode(blender) 
      } 
    } 
  } 
}
```

