# Mask (System API)

Mask effect class, used as input for Filter and VisualEffect. Different types of Mask provide different grayscale distribution patterns, such as wave ring masks, radial gradients, pixel map masks, etc.

**Since:** 20

<!--Device-uiEffect-class Mask--><!--Device-uiEffect-class Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,
      fillColor?: Color): Mask
```

Creates a Mask instance with scaling effect by inputting a pixelMap, the area of the pixelMap to be drawn,the drawing area of the mounted node, and the color to fill outside the drawing area.

**Since:** 20

<!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      fillColor?: Color): Mask--><!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      fillColor?: Color): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelMap | image.PixelMap | Yes |
| srcRect | common2D.Rect | Yes |
| dstRect | common2D.Rect | Yes |
| fillColor | [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { uiEffect, common2D } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit'

const colorBuffer = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
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
  console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
})
```

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap): Mask
```

Creates a Mask instance by inputting a pixelMap. This interface does not perform scaling on the input pixelMap.

**Since:** 22

<!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap): Mask--><!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelMap | image.PixelMap | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
  @State pixelMapDistort: image.PixelMap | undefined = undefined;

  aboutToAppear(): void {
    this.pixelMapDistort = this.getPixelMap();
  }

  private getPixelMap(): image.PixelMap | undefined {
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // this path should be created in local
      const path: string = context.resourceDir + "/perlin_worley_noise_3d_64.bmp";
      const imageSource: image.ImageSource = image.createImageSource(path);
      if (!imageSource) {
        return undefined;
      }
      const pixelMap: image.PixelMap | null = imageSource.createPixelMapSync();
      if (!pixelMap) {
        imageSource.release();
        return undefined;
      }
      imageSource.release();
      return pixelMap;
    } catch (err) {
      return undefined;
    }
  }

  private getMaterialVisualEffect(): uiEffect.VisualEffect {
    let effect: uiEffect.VisualEffect = uiEffect.createEffect();
    let distortMask: uiEffect.Mask | undefined = undefined;
    if (this.pixelMapDistort) {
      distortMask = uiEffect.Mask.createPixelMapMask(this.pixelMapDistort);
    }
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
      distortMask
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
          .visualEffect(this.getMaterialVisualEffect())
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
static createRadialGradientMask(center: common2D.Point, radiusX: number, radiusY: number,
      gradients: Array<[number, number]>): Mask
```

Creates an elliptical mask Mask instance by inputting the center position of the ellipse,the semi-major and semi-minor axes, and shape parameters.

**Since:** 20

<!--Device-Mask-static createRadialGradientMask(center: common2D.Point, radiusX: double, radiusY: double,      gradients: Array<[double, double]>): Mask--><!--Device-Mask-static createRadialGradientMask(center: common2D.Point, radiusX: double, radiusY: double,      gradients: Array<[double, double]>): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| center | common2D.Point | Yes |
| radiusX | number | Yes |
| radiusY | number | Yes |
| gradients | Array & lt;[number, number] & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createRippleMask

```TypeScript
static createRippleMask(center: common2D.Point, radius: number, width: number, offset?: number): Mask
```

Creates a wave ring mask Mask instance by inputting the center position, radius, and width of the wave ring.

**Since:** 20

<!--Device-Mask-static createRippleMask(center: common2D.Point, radius: double, width: double, offset?: double): Mask--><!--Device-Mask-static createRippleMask(center: common2D.Point, radius: double, width: double, offset?: double): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| center | common2D.Point | Yes |
| radius | number | Yes |
| width | number | Yes |
| offset | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let mask = uiEffect.Mask.createRippleMask({x: 0.5, y: 1.0}, 0.5, 0.3, 0.0);
```

## createUseEffectMask

```TypeScript
static createUseEffectMask(useEffect: boolean): Mask
```

Creates and sets a Mask instance indicating whether to use blur caching. This Mask instance is specifically designed for the useEffectMask parameter of the liquidMaterial method, used to declare whether the material effect uses blur caching to improve performance. When this Mask instance is used with other Filter or VisualEffect methods, the useEffect property may not take effect.

**Since:** 22

<!--Device-Mask-static createUseEffectMask(useEffect: boolean): Mask--><!--Device-Mask-static createUseEffectMask(useEffect: boolean): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| useEffect | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

  private getMaterialVisualEffect(): uiEffect.VisualEffect {
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
          .visualEffect(this.getMaterialVisualEffect())
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
static createWaveGradientMask(center: common2D.Point, width: number, propagationRadius: number,
      blurRadius: number, turbulenceStrength?: number): Mask
```

Creates a single-wave mask Mask instance by inputting the wave source center position and single-wave parameters.

**Since:** 20

<!--Device-Mask-static createWaveGradientMask(center: common2D.Point, width: double, propagationRadius: double,      blurRadius: double, turbulenceStrength?: double): Mask--><!--Device-Mask-static createWaveGradientMask(center: common2D.Point, width: double, propagationRadius: double,      blurRadius: double, turbulenceStrength?: double): Mask-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| center | common2D.Point | Yes |
| width | number | Yes |
| propagationRadius | number | Yes |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| turbulenceStrength | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
