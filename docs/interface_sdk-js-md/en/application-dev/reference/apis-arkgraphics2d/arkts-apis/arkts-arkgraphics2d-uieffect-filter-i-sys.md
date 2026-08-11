# Filter

Filter effect class, used to apply corresponding effects to specified components.Before calling Filter methods, you need to first create a Filter instance through createFilter.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-uiEffect-interface Filter--><!--Device-uiEffect-interface Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## bezierWarp

```TypeScript
bezierWarp(controlPoints: Array<common2D.Point>): Filter
```

Adds a Bezier curve deformation effect to the component. This effect achieves precise distortion and shape adjustment of the image by creating closed Bezier curves at the layer boundary.There are four Bezier curve segments, connected head to tail in sequence, with each segment containing one vertex and two tangent points. Typical application scenarios include face deformation effects,card perspective distortion, etc.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-bezierWarp(controlPoints: Array<common2D.Point>): Filter--><!--Device-Filter-bezierWarp(controlPoints: Array<common2D.Point>): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controlPoints | Array&lt;common2D.Point&gt; | Yes | 12 Bezier deformation control points. The array length must be 12. Changing the positions of the control points changes the shape of the curves forming the edges, thereby distorting the image. The control point coordinates use a normalized coordinate system (default range [0, 1]), and coordinate values can be greater than 1 or less than 0. If the array length is not 12, the effect will not take effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the Bezier curve deformation effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { common2D, uiEffect } from '@kit.ArkGraphics2D'

@Entry
@Component
struct BezierWarpExample {
  @State valueBezier: Array<common2D.Point> = [
    { x: 0, y: 0 }, { x: 1 / 3, y: 0 }, { x: 2 / 3, y: 0 }, // top edge
    { x: 0.5, y: 0 }, { x: 0.5, y: 1 / 3 }, { x: 1, y: 2 / 3 }, // right edge
    { x: 1, y: 1 }, { x: 2 / 3, y: 1 }, { x: 1 / 3, y: 1 }, // bottom edge
    { x: 0, y: 1 }, { x: 0, y: 2 / 3 }, { x: 0, y: 1 / 3 }] // left edge

  build() {
    Column() {
      Image($rawfile('test.jpg'))
        .foregroundFilter(uiEffect.createFilter().bezierWarp(this.valueBezier))
    }
  }
}
```

## blurBubblesRise

```TypeScript
blurBubblesRise(param: BlurBubblesRiseEffectParam): Filter
```

Applies a blur bubbles rise effect to the image, simulating a dreamy, bubbly distortion similar to rising bubbles in liquid.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-blurBubblesRise(param: BlurBubblesRiseEffectParam): Filter--><!--Device-Filter-blurBubblesRise(param: BlurBubblesRiseEffectParam): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [BlurBubblesRiseEffectParam](arkts-arkgraphics2d-uieffect-blurbubblesriseeffectparam-i-sys.md) | Yes | The blur bubbles rise effect parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the blur bubbles rise effect attached. |

## colorGradient

ArkTS-Dyn:
```TypeScript
colorGradient(colors: Array<Color>, positions: Array<common2D.Point>, strengths: Array<number>,
        alphaMask?: Mask): Filter
```

ArkTS-Sta:
```TypeScript
colorGradient(colors: Array<Color>, positions: Array<common2D.Point>, strengths: Array<double>,
        alphaMask?: Mask): Filter
```

Adds a color gradient effect to the component content.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-colorGradient(colors: Array<Color>, positions: Array<common2D.Point>, strengths: Array<double>,        alphaMask?: Mask): Filter--><!--Device-Filter-colorGradient(colors: Array<Color>, positions: Array<common2D.Point>, strengths: Array<double>,        alphaMask?: Mask): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colors | Array&lt;Color&gt; | Yes | The color array for multi-color gradient. The array length range is [0, 12], and each color value must be greater than or equal to 0. If the array length is 0 or greater than 12, or if the array lengths of colors, positions, and strengths are not equal, the effect will not take effect. |
| positions | Array&lt;common2D.Point&gt; | Yes | The position array, corresponding to the distribution positions of colors. The array length range is [0, 12]. If the array length is 0 or greater than 12, or if the array lengths of colors, positions, and strengths are not equal, the effect will not take effect. |
| strengths | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Yes | The strength array, corresponding to the diffusion strength of colors. The array length range is [0, 12], and each strength value must be greater than or equal to 0. If the array length is 0 or greater than 12, or if the array lengths of colors, positions, and strengths are not equal, the effect will not take effect. |
| alphaMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | No | The mask that controls the transparency distribution of the gradient effect. A Mask instance can be created through Mask creation methods (such as createRippleMask, createRadialGradientMask, etc.). Pass this parameter when you need to control the transparency distribution of the color gradient effect (such as local transparency or dynamic transparency effects). If not set, the transparency of the color gradient effect is entirely determined by the colors parameter. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the color gradient effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { common2D, uiEffect } from "@kit.ArkGraphics2D"

@Entry
@Component
struct ColorGradientExample {
  @State colorsExample: Array<uiEffect.Color> = [
    {red: 1.0, green: 0.8, blue: 0.5, alpha: 0.8},
    {red: 1.0, green: 1.5, blue: 0.5, alpha: 1.0}
  ]

  @State positionsExample: Array<common2D.Point> = [
    {x: 0.2, y: 0.2},
    {x: 0.8, y: 0.6}]

  @State strengthsExample: Array<number> = [0.3, 0.3]

  build() {
    Column() {
      Row()
        .width("100%")
        .height("100%")
        .backgroundFilter(uiEffect.createFilter().colorGradient(this.colorsExample, this.positionsExample, this.strengthsExample))
    }
  }
}
```

## contentLight

ArkTS-Dyn:
```TypeScript
contentLight(lightPosition: common2D.Point3d, lightColor: common2D.Color, lightIntensity: number,
      displacementMap?: Mask): Filter
```

ArkTS-Sta:
```TypeScript
contentLight(lightPosition: common2D.Point3d, lightColor: common2D.Color, lightIntensity: double,
      displacementMap?: Mask): Filter
```

Adds a 3D lighting effect to the component content.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-contentLight(lightPosition: common2D.Point3d, lightColor: common2D.Color, lightIntensity: double,      displacementMap?: Mask): Filter--><!--Device-Filter-contentLight(lightPosition: common2D.Point3d, lightColor: common2D.Color, lightIntensity: double,      displacementMap?: Mask): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lightPosition | common2D.Point3d | Yes | The position of the light source in the component space. [-1, -1, 0] is the top-left corner of the component, [1, 1, 0] is the bottom-right corner of the component. The larger the z-axis component, the farther the light source is from the component plane, and the larger the illuminated area. The x component range is [-10, 10], the y component range is [-10, 10], and the z component range is [0, 10]. Values outside the range will be automatically clamped. |
| lightColor | common2D.Color | Yes | The color of the light source. The RGBA components range from [0, 1]. Values outside the range will be automatically clamped. |
| lightIntensity | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The intensity of the light source. The value range is [0, 1]. A larger value indicates a brighter light source. Values outside the range will be automatically clamped. |
| displacementMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | No | The displacement map parameter. This parameter is not currently effective and is not recommended to be passed in. Not setting it has no effect on the functionality. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the content lighting effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { common2D, uiEffect } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  @State point2: common2D.Point3d = {
    x: 0, y: 0, z: 2
  }
  @State color2: common2D.Color = {
    red: 1,
    green: 1,
    blue: 1,
    alpha: 1
  }
  @State lightIntensity2: number = 1

  build() {
    Column() {
      Stack() {
        Image($r('app.media.man'))
          .width('646px')
          .height('900px')
          .borderRadius(10)
          .foregroundFilter(uiEffect.createFilter().contentLight(this.point2, this.color2, this.lightIntensity2))
      }
      .width('100%')
      .height('55%')
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#555')
  }
}
```

## directionLight

ArkTS-Dyn:
```TypeScript
directionLight(direction: common2D.Point3d, color: Color, intensity: number, mask?: Mask, factor?: number): Filter
```

ArkTS-Sta:
```TypeScript
directionLight(direction: common2D.Point3d, color: Color, intensity: double, mask?: Mask, factor?: double): Filter
```

Provides a Mask-based and directional light lighting effect for the component content.Directional light illuminates the component plane from a uniform direction, with all light rays in the same direction, not attenuating with distance, and the light intensity is evenly distributed across the component,suitable for simulating distant light sources such as sunlight. Unlike the point light source of contentLight,directional light does not need to specify the specific position of the light source.Through the Mask, you can control lighting details, and through the factor, you can combine height maps to enhance the relief effect.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-directionLight(direction: common2D.Point3d, color: Color, intensity: double, mask?: Mask, factor?: double): Filter--><!--Device-Filter-directionLight(direction: common2D.Point3d, color: Color, intensity: double, mask?: Mask, factor?: double): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | common2D.Point3d | Yes | The direction of the incident light, represented by three-dimensional coordinates indicating the direction of the light rays. |
| color | [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | Yes | The light color. |
| intensity | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The light intensity. The value range is [0, +∞). A larger value indicates a brighter light source. |
| mask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | No | The displacement map, used to describe the three-dimensional details of the two-dimensional image surface. A Mask instance can be created through Mask creation methods (such as createRippleMask, createRadialGradientMask, etc.). Pass this parameter when you need to enhance local details and lighting reflection effects (such as relief, bump textures). Implemented through normal maps or height maps; if a height map is input, it needs to be used with the factor parameter. If not set, the default is empty, resulting in a global flat lighting effect without details. |
| factor | ArkTS-Dyn: number  <br>ArkTS-Sta：double | No | The sampling scale coefficient. Pass this parameter when using a height map as the mask and needing to control the height scaling. If not set, the mask is sampled directly as a normal map; if a value is set, the mask is sampled as a height map, and the actual height value is the product of the mask sampling value and the factor. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the lighting effect controlled by the displacement map attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { uiEffect, common2D } from "@kit.ArkGraphics2D";

@Entry
@Component
struct Index {
  @State rippleMaskCenter: common2D.Point = {x:0.5, y:0.5}
  @State rippleMaskRadius: number = 0.0
  @State rippleMaskWidth: number = 0.0
  @State color: Color = Color.Transparent

  build() {
    Column() {
      RelativeContainer() {
        Image($r("app.media.back")).width("100%").height("100%")
        Stack()
          .width("100%")
          .height("100%")
          .backgroundColor(this.color)
          .backgroundFilter(uiEffect.createFilter()
            .directionLight(
              {x:0, y:0, z:-1}, {red:2.0, green:2.0, blue:2.0, alpha:1.0}, 0.5,
              uiEffect.Mask.createRippleMask(this.rippleMaskCenter, this.rippleMaskRadius, this.rippleMaskWidth, 0.0)
              ))
          .onClick(() => {
            this.getUIContext().animateTo({duration: 1000}, () => {
              this.rippleMaskWidth = 1.0;
            })
          })
      }
    }.alignItems(HorizontalAlign.Center).borderWidth(2)
  }
}
```

## displacementDistort

ArkTS-Dyn:
```TypeScript
displacementDistort(displacementMap: Mask, factor?: [number, number]): Filter
```

ArkTS-Sta:
```TypeScript
displacementDistort(displacementMap: Mask, factor?: [double, double]): Filter
```

Adds a distortion effect to the component content.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-displacementDistort(displacementMap: Mask, factor?: [double, double]): Filter--><!--Device-Filter-displacementDistort(displacementMap: Mask, factor?: [double, double]): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displacementMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Yes | The displacement map, used to control the direction and intensity of distortion. A Mask instance can be created through Mask creation methods (such as createRippleMask, createPixelMapMask, etc.). It works together with the factor to determine the degree of distortion. |
| factor | ArkTS-Dyn: [number, number]  <br>ArkTS-Sta：[double, double] | No | Specifies the horizontal and vertical distortion intensity coefficients. Pass this parameter when you need to control the direction and intensity of distortion (such as one-way distortion or differential distortion). The larger the absolute value of the coefficient, the more obvious the distortion. The recommended value range is [-10.0, 10.0]. If not set, the default value is [1.0, 1.0], indicating that both horizontal and vertical directions apply the default distortion intensity. Setting it to [0.0, 0.0] results in no distortion effect. The grayscale value of the Mask controls the direction and intensity of distortion, and the factor multiplied by the Mask grayscale value jointly determines the final distortion degree, i.e., actual distortion value = Mask grayscale value × factor value. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the distortion effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { uiEffect } from "@kit.ArkGraphics2D"

@Entry
@Component
struct DisplacementDistortExample {
  @State maskExample: uiEffect.Mask = uiEffect.Mask.createRippleMask({x: 0.5, y: 0.5}, 0.2, 0.3, 0.0)
  
  build() {
    Stack() {
      Image($rawfile('test.png'))
      Row()  
        .width("100%")
        .height("100%")
        .backgroundFilter(uiEffect.createFilter().displacementDistort(this.maskExample, [5.0, 5.0]))
    }
  }
}
```

## distort

ArkTS-Dyn:
```TypeScript
distort(distortionK: number): Filter
```

ArkTS-Sta:
```TypeScript
distort(distortionK: double): Filter
```

Adds a lens distortion effect to the component.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-Filter-distort(distortionK: double): Filter--><!--Device-Filter-distort(distortionK: double): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distortionK | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The distortion coefficient, indicating the degree of lens distortion. The value range is [-1, 1]. Values less than -1 are treated as -1; values greater than 1 are treated as 1. When the distortion coefficient is less than 0, the effect is barrel distortion; when greater than 0, the effect is pincushion distortion. The closer the value is to 0, the smaller the distortion; when the value is 0, there is no distortion effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the lens distortion effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
filter.distort(-0.5)
```

## edgeLight

ArkTS-Dyn:
```TypeScript
edgeLight(alpha: number, color?: Color, mask?: Mask, bloom?: boolean): Filter
```

ArkTS-Sta:
```TypeScript
edgeLight(alpha: double, color?: Color, mask?: Mask, bloom?: boolean): Filter
```

Detects edges of the component content and adds an edge highlight effect.This effect automatically detects the edge contours of the component content and overlays a highlight stroke.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-edgeLight(alpha: double, color?: Color, mask?: Mask, bloom?: boolean): Filter--><!--Device-Filter-edgeLight(alpha: double, color?: Color, mask?: Mask, bloom?: boolean): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Specifies the stroke highlight transparency. A larger value makes the stroke more obvious. The value range is [0, 1]. Setting it to 0 results in no stroke; values less than 0 are treated as 0; values greater than 1 are treated as 1. |
| color | [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | No | Specifies the stroke highlight color. The RGB components range from [0, +∞). Pass this parameter when you need to customize the stroke highlight color (such as emphasizing a specific color effect). If not set, the original color of the component content is used by default. When the color parameter is set, the alpha in Color does not take effect; only RGB is used. |
| mask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | No | Specifies the stroke highlight intensity mask. A Mask instance can be created through Mask creation methods (such as createRippleMask, createRadialGradientMask, etc.). Pass this parameter when you need to control the area of the stroke highlight effect (such as local highlight instead of global highlight). If not set, the entire component content has the stroke highlight effect by default. |
| bloom | boolean | No | Specifies whether the stroke has a bloom effect. Set to true when you need to enhance the visual effect; set to false when you need a simple stroke effect. The default value is true (with bloom effect). For images smaller than 16x16, there is only a stroke effect by default, no bloom effect, and this parameter has no effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the edge highlight effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { uiEffect } from "@kit.ArkGraphics2D"

@Entry
@Component
struct EdgeLightExample {
  @State colorExample: uiEffect.Color = {red: 0.0, green: 1.0, blue: 0.0, alpha: 1.0}
  
  @State maskExample: uiEffect.Mask = uiEffect.Mask.createRippleMask({x: 0.5, y: 0.5}, 0.2, 0.5, 0.5)
  
  build() {
    Stack() {
      Image($rawfile('test.png'))
      Row()  
        .width("100%")
        .height("100%")
        .backgroundFilter(uiEffect.createFilter().edgeLight(1.0, this.colorExample, this.maskExample, false))
    }
  }
}
```

## flyInFlyOutEffect

ArkTS-Dyn:
```TypeScript
flyInFlyOutEffect(degree: number, flyMode: FlyMode): Filter
```

ArkTS-Sta:
```TypeScript
flyInFlyOutEffect(degree: double, flyMode: FlyMode): Filter
```

Adds a fly-in or fly-out deformation effect to the component.Typical application scenarios include page transition animations, window entry/exit animations,dialog pop-up animations, list item entry/exit animations, etc.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Filter-flyInFlyOutEffect(degree: double, flyMode: FlyMode): Filter--><!--Device-Filter-flyInFlyOutEffect(degree: double, flyMode: FlyMode): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| degree | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Indicates the degree of fly-in or fly-out deformation. The value range is [0, 1]. The closer the value is to 1, the more obvious the deformation. Values outside the range will not produce a deformation effect. |
| flyMode | [FlyMode](arkts-arkgraphics2d-uieffect-flymode-e-sys.md) | Yes | The scene mode of the fly-in or fly-out effect. BOTTOM indicates the fly-in or fly-out deformation scene from the bottom of the device. TOP indicates the fly-in or fly-out deformation scene from the top of the device. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the fly-in or fly-out deformation effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
filter.flyInFlyOutEffect(0.5, uiEffect.FlyMode.TOP)
```

## heatDistortion

```TypeScript
heatDistortion(param: HeatDistortionEffectParam): Filter
```

Applies a heat distortion effect to the image, simulating the visual distortion caused by hot air flow.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-heatDistortion(param: HeatDistortionEffectParam): Filter--><!--Device-Filter-heatDistortion(param: HeatDistortionEffectParam): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [HeatDistortionEffectParam](arkts-arkgraphics2d-uieffect-heatdistortioneffectparam-i-sys.md) | Yes | The heat distortion effect parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the heat distortion effect attached. |

## maskDispersion

ArkTS-Dyn:
```TypeScript
maskDispersion(dispersionMap: Mask, alpha: number, rFactor?: [number, number], gFactor?: [number, number],
      bFactor?: [number, number]): Filter
```

ArkTS-Sta:
```TypeScript
maskDispersion(dispersionMap: Mask, alpha: double, rFactor?: [double, double], gFactor?: [double, double],
      bFactor?: [double, double]): Filter
```

Adds a dispersion effect controlled by a displacement map to the component content, simulating the dispersion phenomenon when light passes through a prism. Typical application scenarios include colorful effects, prism refraction simulation, etc.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-maskDispersion(dispersionMap: Mask, alpha: double, rFactor?: [double, double], gFactor?: [double, double],      bFactor?: [double, double]): Filter--><!--Device-Filter-maskDispersion(dispersionMap: Mask, alpha: double, rFactor?: [double, double], gFactor?: [double, double],      bFactor?: [double, double]): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dispersionMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Yes | The displacement map, used to control the intensity, direction, and transparency of dispersion. It is recommended to use a PixelMapMask-type displacement map, which allows fine-grained control over the dispersion area and intensity through custom image textures. A Mask instance can be created through the createPixelMapMask method. |
| alpha | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The overall transparency of the dispersion effect. A smaller transparency value results in a more transparent effect. The value range is [0, 1.0]. Setting it to 0 results in no dispersion effect; values less than 0 are treated as 0; values greater than 1.0 are treated as 1.0. |
| rFactor | ArkTS-Dyn: [number, number]  <br>ArkTS-Sta：[double, double] | No | The basic offset of the R channel in the X/Y direction. Pass this parameter when you need to customize the dispersion intensity and direction of the red channel. A larger offset results in a more obvious red dispersion effect. If not passed, the default value is [0.0, 0.0], meaning no R channel dispersion offset. The value range for each direction is [-1.0, 1.0], and values outside the range will be automatically clamped. |
| gFactor | ArkTS-Dyn: [number, number]  <br>ArkTS-Sta：[double, double] | No | The basic offset of the G channel in the X/Y direction. Pass this parameter when you need to customize the dispersion intensity and direction of the green channel. If not passed, the default value is [0.0, 0.0], meaning no G channel dispersion offset. The value range is the same as rFactor, [-1.0, 1.0], and values outside the range will be automatically clamped. |
| bFactor | ArkTS-Dyn: [number, number]  <br>ArkTS-Sta：[double, double] | No | The basic offset of the B channel in the X/Y direction. Pass this parameter when you need to customize the dispersion intensity and direction of the blue channel. If not passed, the default value is [0.0, 0.0], meaning no B channel dispersion offset. The value range is the same as rFactor, [-1.0, 1.0], and values outside the range will be automatically clamped. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the dispersion effect controlled by the displacement map attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## maskTransition

ArkTS-Dyn:
```TypeScript
maskTransition(alphaMask: Mask, factor?: number, inverse?: boolean): Filter
```

ArkTS-Sta:
```TypeScript
maskTransition(alphaMask: Mask, factor?: double, inverse?: boolean): Filter
```

Provides a Mask-based transition effect for the component content, which can be used for page transition animations, scene transition effects, etc.

It is not recommended to use this effect during screen size changes, such as screen rotation,foldable screen opening/closing, etc.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-maskTransition(alphaMask: Mask, factor?: double, inverse?: boolean): Filter--><!--Device-Filter-maskTransition(alphaMask: Mask, factor?: double, inverse?: boolean): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alphaMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Yes | Specifies the area of the transition effect through a mask. A Mask instance can be created through Mask creation methods (such as createRippleMask, createRadialGradientMask, etc.). The grayscale value of the Mask determines the degree of the transition effect; a larger grayscale value results in a more obvious transition effect in that area. |
| factor | ArkTS-Dyn: number  <br>ArkTS-Sta：double | No | The transition coefficient. Pass this parameter when you need to control the transition progress (such as during animation or dynamic adjustment). A larger value makes the image closer to the post-transition page. If not set, the default value is 1.0 (transition completed state). The value range is [0.0, 1.0], and values outside the range will be automatically clamped to [0.0, 1.0]. |
| inverse | boolean | No | Whether to enable reverse transition. Set to true when you need a reverse transition effect (such as transitioning from the back page to the front page); set to false when you need a forward transition effect (such as transitioning from the front page to the back page). The default value is false (forward transition). |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the transition effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { uiEffect, common2D } from "@kit.ArkGraphics2D";

@Entry
@Component
struct Index {
  context = this.getUIContext()
  @State alpha: number = 0
  @State enterNewPage:boolean = false
  @State rippleMaskCenter: common2D.Point = {x:0.5, y:0.5}
  @State rippleMaskRadius: number = 0.1
  build() {
    Stack() {
      // Page before transition
      Image($r("app.media.before")).width("100%").height("100%")
        if (this.enterNewPage){
          // Page after transition
          Column().width("100%").height("100%").backgroundImage($r("app.media.after"))
            .backgroundFilter(uiEffect.createFilter()
              .maskTransition(
                uiEffect.Mask.createRadialGradientMask(this.rippleMaskCenter, this.rippleMaskRadius,this.rippleMaskRadius, [[1, 0], [1, 1]]),
                this.alpha))
            .onAppear(() => {
              this.context.animateTo({ duration: 1000 }, () => {
                this.rippleMaskRadius = 1.3
              })
              this.context.animateTo({ duration: 800 }, () => {
                this.alpha = 1
              })
            })
        }
    }.borderWidth(2)
    .onClick(()=>{
      this.enterNewPage=!this.enterNewPage;
      if (this.enterNewPage) {
        this.alpha=0;
        this.rippleMaskRadius=0.1;
      }
    })
  }
}
```

## pixelStretch

ArkTS-Dyn:
```TypeScript
pixelStretch(stretchSizes: Array<number>, tileMode: TileMode): Filter
```

ArkTS-Sta:
```TypeScript
pixelStretch(stretchSizes: Array<double>, tileMode: TileMode): Filter
```

Adds a pixel stretch effect to the component.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Filter-pixelStretch(stretchSizes: Array<double>, tileMode: TileMode): Filter--><!--Device-Filter-pixelStretch(stretchSizes: Array<double>, tileMode: TileMode): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stretchSizes | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Yes | The percentage ratios of edge pixel stretching in the top, bottom, left, and right directions. The value range is [-1, 1]. A positive value indicates outward stretching, and the edge pixels of the specified original image ratio are used to fill in the top, bottom, left, and right directions. A negative value indicates inward shrinking, but the final image size remains unchanged. Note that the parameters for all four directions must be uniformly non-positive or non-negative, otherwise the effect will not take effect. |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | Yes | The pixel fill mode for edge pixel stretching. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the pixel stretch effect attached. |

## Examples

```TypeScript
filter.pixelStretch([0.2, 0.2, 0.2, 0.2], uiEffect.TileMode.CLAMP)
```

## radiusGradientBlur

ArkTS-Dyn:
```TypeScript
radiusGradientBlur(radius: number, gradientParam: LinearGradientBlurOptions): Filter
```

ArkTS-Sta:
```TypeScript
radiusGradientBlur(radius: double, gradientParam: LinearGradientBlurOptions): Filter
```

Adds a radius linear gradient blur effect to the component content.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-Filter-radiusGradientBlur(radius: double, gradientParam: LinearGradientBlurOptions): Filter--><!--Device-Filter-radiusGradientBlur(radius: double, gradientParam: LinearGradientBlurOptions): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Blur radius, in px. A larger blur radius results in a stronger blur effect. The value range is [0, 128]. When the blur radius is 0, there is no blur effect; values less than 0 are treated as 0; values greater than 128 are treated as 128. |
| gradientParam | [LinearGradientBlurOptions](../../apis-arkui/arkts-components/arkts-arkui-lineargradientbluroptions-i.md) | Yes | The linear gradient parameters, including fractionStops and direction. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the radius linear gradient blur effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## variableRadiusBlur

ArkTS-Dyn:
```TypeScript
variableRadiusBlur(radius: number, radiusMap: Mask): Filter
```

ArkTS-Sta:
```TypeScript
variableRadiusBlur(radius: double, radiusMap: Mask): Filter
```

Provides a Mask-based gradient blur effect for the component content.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Filter-variableRadiusBlur(radius: double, radiusMap: Mask): Filter--><!--Device-Filter-variableRadiusBlur(radius: double, radiusMap: Mask): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Maximum blur radius, in px. A larger value results in a stronger blur effect. The value range is [0, 128]. When the blur radius is 0, there is no blur effect; values less than 0 are treated as 0; values greater than 128 are treated as 128. |
| radiusMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Yes | The Mask object representing the degree of blurring. The grayscale value of the Mask represents the degree of blurring at the corresponding position; a larger grayscale value indicates more blurring. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the current effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { uiEffect } from "@kit.ArkGraphics2D";

@Entry
@Component
struct VariableRadiusBlurExample {
  @State maskExample: uiEffect.Mask = uiEffect.Mask.createRippleMask({x: 0.5, y: 0.5}, 0.2, 0.1)

  build() {
    Stack() {
      Image($rawfile('test.png'))
      Row()
        .width("100%")
        .height("100%")
        .backgroundFilter(uiEffect.createFilter().variableRadiusBlur(64, this.maskExample))
    }
  }
}
```

## waterRipple

ArkTS-Dyn:
```TypeScript
waterRipple(progress: number, waveCount: number, x: number, y: number, rippleMode: WaterRippleMode): Filter
```

ArkTS-Sta:
```TypeScript
waterRipple(progress: double, waveCount: int, x: double, y: double, rippleMode: WaterRippleMode): Filter
```

Adds a water ripple effect to the component.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Filter-waterRipple(progress: double, waveCount: int, x: double, y: double, rippleMode: WaterRippleMode): Filter--><!--Device-Filter-waterRipple(progress: double, waveCount: int, x: double, y: double, rippleMode: WaterRippleMode): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Indicates the ripple progress. The value range is [0, 1]. The closer the progress is to 1, the more fully the ripples are displayed. Values outside the range will not produce a ripple effect. |
| waveCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The number of waves when the water ripples. The value range is [1, 3]. The wave count must be an integer. If a floating-point number or a value outside the range is provided, the ripple effect will not appear. |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The X-axis position of the center point where the water ripple first appears on the screen. The screen is normalized, with the top-left corner at (0, 0) and the top-right corner at (1, 0). A negative value indicates a position to the left of the screen. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | The Y-axis position of the center point where the water ripple first appears on the screen. The screen is normalized, with the top-left corner at (0, 0) and the bottom-left corner at (0, 1). A negative value indicates a position above the screen. |
| rippleMode | [WaterRippleMode](arkts-arkgraphics2d-uieffect-waterripplemode-e-sys.md) | Yes | The scene mode of the water ripple. |

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i-sys.md) | Returns the Filter with the water ripple effect attached. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
filter.waterRipple(0.5, 2, 0.5, 0.5, uiEffect.WaterRippleMode.SMALL2SMALL)
```

