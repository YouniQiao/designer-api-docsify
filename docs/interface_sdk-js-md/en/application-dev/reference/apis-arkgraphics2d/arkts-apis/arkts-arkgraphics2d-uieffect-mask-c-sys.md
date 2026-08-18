# Mask (System API)

Mask effect class, used as input for Filter and VisualEffect. Different types of Mask provide different grayscale distribution patterns, such as wave ring masks, radial gradients, pixel map masks, etc.

**Since:** 23

<!--Device-uiEffect-class Mask--><!--Device-uiEffect-class Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,
      fillColor?: Color): Mask
```

Creates a Mask instance with scaling effect by inputting a pixelMap, the area of the pixelMap to be drawn, the drawing area of the mounted node, and the color to fill outside the drawing area.

**Since:** 23

<!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      fillColor?: Color): Mask--><!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      fillColor?: Color): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelMap | image.PixelMap | Yes | The PixelMap instance created by the image module. It can be obtained through image decoding or direct creation. |
| srcRect | common2D.Rect | Yes | The area of the pixelMap to be drawn. The leftmost and topmost positions correspond to 0, and the rightmost and bottommost positions correspond to 1. right must be greater than left, and bottom must be greater than top; otherwise the effect will not take effect. |
| dstRect | common2D.Rect | Yes | The drawing area of the pixelMap on the node where the mask is mounted. The leftmost and topmost positions of the node correspond to 0, and the rightmost and bottommost positions correspond to 1. right must be greater than left, and bottom must be greater than top; otherwise the effect will not take effect. |
| fillColor | Color | No | The color to fill the area outside the pixelMap drawing area on the node. Each component range is [0, 1], default is transparent color. Values less than 0 are treated as 0, and values greater than 1 are treated as 1. |

**Return value:**

| Type | Description |
| --- | --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Returns a Mask instance created based on the pixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { image } from "@kit.ImageKit";
import { uiEffect, common2D } from "@kit.ArkGraphics2D";
import { BusinessError } from '@kit.BasicServicesKit'

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  let srcRect : common2D.Rect = {
    left: 0,
    top: 0,
    right: 1,
    bottom: 1
  }
  let dstRect : common2D.Rect = {
    left: 0,
    top: 0,
    right: 1,
    bottom: 1
  }
  let fillColor : uiEffect.Color = {
    red: 0,
    green: 0,
    blue: 0,
    alpha: 1
  }
  let mask = uiEffect.Mask.createPixelMapMask(pixelMap, srcRect, dstRect, fillColor);
}).catch((error: BusinessError)=>{
  console.error('Failed to create pixelmap. code is ${error.code}, message is ${error.message}');
})
```

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap): Mask
```

Creates a Mask instance by inputting a pixelMap. This interface does not perform scaling on the input pixelMap.

**Since:** 23

<!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap): Mask--><!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelMap | image.PixelMap | Yes | The PixelMap instance created by the image module. It can be obtained through image decoding or direct creation. |

**Return value:**

| Type | Description |
| --- | --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Returns a Mask with the pixelMap. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State distortProgress: number = 0.;
  @State rippleProgress: number = 0.;
  @State distortFactor: number = 0.;
  @State materialFactor: number = 1.;
  @State refractionFactor: number = 1.;
  @State reflectionFactor: number = 1.;
  @State tintColorR: number = 1.;
  @State tintColorG: number = 1.;
  @State tintColorB: number = 1.;
  @State tintColorA: number = 1.;
  @State pixelMapDistort: image.PixelMap | undefined = this.getPixelMap();

  private getPixelMap(): image.PixelMap | undefined {
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // this path should be created in local
      const path: string = context.resourceDir + "/perlin_worley_noise_3d_64.bmp";
      const imageSource: image.ImageSource = image.createImageSource(path);
      if (!imageSource) {
        return undefined;
      }
      const pixelMap: image.PixelMap = imageSource.createPixelMapSync();
      imageSource.release();
      return pixelMap;
    } catch (err) {
      return undefined;
    }
  }

  private GetMaterialVisualEffect(): uiEffect.VisualEffect {
    let effect: uiEffect.VisualEffect = uiEffect.createEffect();
    effect.liquidMaterial({
      enable: true,
      distortProgress : this.distortProgress,
      rippleProgress: this.rippleProgress,
      distortFactor: this.distortFactor,
      materialFactor : this.materialFactor,
      refractionFactor : this.refractionFactor,
      reflectionFactor: this.reflectionFactor,
      tintColor : [this.tintColorR, this.tintColorG, this.tintColorB, this.tintColorA],
      ripplePosition: undefined,
    },
      uiEffect.Mask.createUseEffectMask(true),
      uiEffect.Mask.createPixelMapMask (this.pixelMapDistort), // Example of using createImageMask.
      );
    return effect;
  }

  build() {
    Stack() {
      EffectComponent() {
        Column()
          .position({ x: 200 + 'px', y: 200 + 'px' })
          .height(553 + 'px')
          .width(553 + 'px')
          .borderRadius(12)
          .visualEffect(this.GetMaterialVisualEffect())
      }
      .backgroundEffect({
        radius: 15,
      }, { disableSystemAdaptation: true })
      .width("100%").height("100%").align(Alignment.Center)
    }
    .backgroundImage($r('app.media.bg6'), ImageRepeat.NoRepeat) // the image should be created in local
    .width("100%").height("100%").align(Alignment.Center)
  }
}
```

## createRadialGradientMask

```TypeScript
static createRadialGradientMask(center: common2D.Point, radiusX: double, radiusY: double,
      gradients: Array<[double, double]>): Mask
```

Creates an elliptical mask Mask instance by inputting the center position of the ellipse, the semi-major and semi-minor axes, and shape parameters.

**Since:** 23

<!--Device-Mask-static createRadialGradientMask(center: common2D.Point, radiusX: double, radiusY: double,      gradients: Array<[double, double]>): Mask--><!--Device-Mask-static createRadialGradientMask(center: common2D.Point, radiusX: double, radiusY: double,      gradients: Array<[double, double]>): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| center | common2D.Point | Yes | Sets the center point of the ellipse. [0, 0] is the top-left corner of the component, [1, 1] is the bottom-right corner of the component. The value range is [-10, 10], floating-point values are supported, and values outside the range will be clamped during implementation. |
| radiusX | double | Yes | Sets the semi-major axis of the ellipse. When the radius is 1, it equals the component height. The value range is [0, 10], floating-point values are supported, and values outside the range will be clamped during implementation. |
| radiusY | double | Yes | Sets the semi-minor axis of the ellipse. When the radius is 1, it equals the component height. The value range is [0, 10], floating-point values are supported, and values outside the range will be clamped during implementation. |
| gradients | Array&lt;[double, double]&gt; | Yes | The binary arrays in the array represent gradients: [RGBA color, position]. The RGBA color uses the same value for all four channels, which can be regarded as a grayscale value; position represents the distribution position of the RGBA color along the radial direction outward. Both RGBA color and position have a value range of [0, 1], floating-point values are supported, values less than 0 are treated as 0, and values greater than 1 are treated as 1. The position parameter values must be strictly increasing, the number of binary arrays in the Array must be greater than or equal to 2, and the elements in the binary arrays must not be empty; otherwise the elliptical distribution effect will not take effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Returns a grayscale Mask with the elliptical radial distribution effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## createRippleMask

```TypeScript
static createRippleMask(center: common2D.Point, radius: double, width: double, offset?: double): Mask
```

Creates a wave ring mask Mask instance by inputting the center position, radius, and width of the wave ring.

**Since:** 23

<!--Device-Mask-static createRippleMask(center: common2D.Point, radius: double, width: double, offset?: double): Mask--><!--Device-Mask-static createRippleMask(center: common2D.Point, radius: double, width: double, offset?: double): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| center | common2D.Point | Yes | Sets the position of the wave ring center on the component. [0, 0] is the top-left corner of the component, [1, 1] is the bottom-right corner of the component. The value range is [-10, 10], and values outside the range will be clamped during implementation. |
| radius | double | Yes | Sets the radius of the wave ring, using normalized values. When the radius is 1, the wave ring radius equals the component height. The value range is [0, 10], and values outside the range will be clamped during implementation. |
| width | double | Yes | Sets the width of the wave ring, using normalized values. When the width is 1, the wave ring width equals the component height. The value range is [0, 10], and values outside the range will be clamped during implementation. |
| offset | double | No | Sets the offset of the wave peak position. The default value is 0, meaning the wave peak is at the exact center of the wave ring; -1.0 means the wave peak is at the innermost edge of the wave ring; 1.0 means the wave peak is at the outermost edge of the wave ring. The value range is [-1, 1], and values outside the range will be clamped during implementation. |

**Return value:**

| Type | Description |
| --- | --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Returns a Mask with the wave ring mask effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
let mask = uiEffect.Mask.createRippleMask({x:0.5, y:1.0}, 0.5, 0.3, 0.0);
```

## createUseEffectMask

```TypeScript
static createUseEffectMask(useEffect: boolean): Mask
```

Creates and sets a Mask instance indicating whether to use blur caching. This Mask instance is specifically designed for the useEffectMask parameter of the liquidMaterial method, used to declare whether the material effect uses blur caching to improve performance. When this Mask instance is used with other Filter or VisualEffect methods, the useEffect property may not take effect.

**Since:** 23

<!--Device-Mask-static createUseEffectMask(useEffect: boolean): Mask--><!--Device-Mask-static createUseEffectMask(useEffect: boolean): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| useEffect | boolean | Yes | Flag indicating whether to use blur caching. A value of true means use, and the blur effect will be displayed normally; a value of false means not use, and the blur effect will not be displayed. |

**Return value:**

| Type | Description |
| --- | --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Returns a Mask instance that indicates whether to use blur caching. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
  @State distortProgress: number = 0.;
  @State rippleProgress: number = 0.;
  @State distortFactor: number = 0.;
  @State materialFactor: number = 1.;
  @State refractionFactor: number = 1.;
  @State reflectionFactor: number = 1.;
  @State tintColorR: number = 1.;
  @State tintColorG: number = 1.;
  @State tintColorB: number = 1.;
  @State tintColorA: number = 1.;

  private GetMaterialVisualEffect(): uiEffect.VisualEffect {
    let effect: uiEffect.VisualEffect = uiEffect.createEffect();
    effect.liquidMaterial({
        enable: true,
        distortProgress : this.distortProgress,
        rippleProgress: this.rippleProgress,
        distortFactor: this.distortFactor,
        materialFactor : this.materialFactor,
        refractionFactor : this.refractionFactor,
        reflectionFactor: this.reflectionFactor,
        tintColor : [this.tintColorR, this.tintColorG, this.tintColorB, this.tintColorA],
        ripplePosition: undefined,
      },
      uiEffect.Mask.createUseEffectMask(true), // Example of using useEffectMask.
    );
    return effect;
  }

  build() {
    Stack() {
      EffectComponent() {
        Column()
          .position({ x: 200 + 'px', y: 200 + 'px' })
          .height(553 + 'px')
          .width(553 + 'px')
          .borderRadius(12)
          .visualEffect(this.GetMaterialVisualEffect())
      }
      .backgroundEffect({
        radius: 15,
      }, { disableSystemAdaptation: true })
      .width("100%").height("100%").align(Alignment.Center)
    }
    .backgroundImage($r('app.media.bg6'), ImageRepeat.NoRepeat)
    .width("100%").height("100%").align(Alignment.Center)
  }
}
```

## createWaveGradientMask

```TypeScript
static createWaveGradientMask(center: common2D.Point, width: double, propagationRadius: double,
      blurRadius: double, turbulenceStrength?: double): Mask
```

Creates a single-wave mask Mask instance by inputting the wave source center position and single-wave parameters.

**Since:** 23

<!--Device-Mask-static createWaveGradientMask(center: common2D.Point, width: double, propagationRadius: double,      blurRadius: double, turbulenceStrength?: double): Mask--><!--Device-Mask-static createWaveGradientMask(center: common2D.Point, width: double, propagationRadius: double,      blurRadius: double, turbulenceStrength?: double): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| center | common2D.Point | Yes | Sets the center point of the single-wave source. [0, 0] is the top-left corner of the component, [1, 1] is the bottom-right corner of the component. The value range is [-10, 10], floating-point values are supported, and values outside the range will be clamped during implementation. |
| width | double | Yes | Sets the width of the single-wave ring. The value range is [0, 5], floating-point values are supported, and values outside the range will be clamped during implementation. |
| propagationRadius | double | Yes | Sets the outer diffusion radius of the single-wave ring. The value range is [0, 10], floating-point values are supported, and values outside the range will be clamped during implementation. |
| blurRadius | double | Yes | Sets the blur outer radius of the single-wave ring. A blur radius of 0 results in a solid-edge ring; otherwise, it is a soft-edge ring. The value range is [0, 5], floating-point values are supported, and values outside the range will be clamped during implementation. |
| turbulenceStrength | double | No | Sets the turbulence intensity of the single-wave ring. The default value is 0; an intensity of 0 results in a regular ring, otherwise the ring edges will be turbulently distorted. The value range is [-1, 1], floating-point values are supported, and values outside the range will be clamped during implementation. |

**Return value:**

| Type | Description |
| --- | --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Returns a grayscale Mask with a single wave shape. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { uiEffect } from "@kit.ArkGraphics2D";
// center: [0.5, 0.5]; width: 0.01; propagationRadius: 0.5; blurRadius: 0.1; turbulenceStrength: 0.1
let mask = uiEffect.Mask.createWaveGradientMask({x: 0.5, y: 0.5}, 0.01, 0.5, 0.1, 0.1);
@Entry
@Component
struct WaveGradientMaskExample {
  build() {
    Stack() {
      Image($rawfile('test.jpg'))
      Column()
        .width('100%')
        .height('100%')
        // Use the mask as the filter parameter to implement the ripple effect that spreads from the center of the screen.
        .backgroundFilter(uiEffect.createFilter().edgeLight(1.0, null, mask))
    }
  }
}
```

