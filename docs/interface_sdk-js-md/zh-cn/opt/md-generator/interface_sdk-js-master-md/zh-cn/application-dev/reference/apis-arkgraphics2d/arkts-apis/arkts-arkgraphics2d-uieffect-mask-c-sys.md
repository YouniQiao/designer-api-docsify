# Mask（系统接口）

Mask效果类，作为Filter以及VisualEffect的输入使用。不同类型的Mask提供不同的灰度分布模式，如波环遮罩、径向渐变、像素图遮罩等。

**起始版本：** 23

**废弃版本：** -1

<!--Device-uiEffect-class Mask--><!--Device-uiEffect-class Mask-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,
      fillColor?: Color): Mask
```

通过输入的pixelMap，以及pixelMap的待绘制区域、挂载节点的绘制区域和绘制区域外填充的颜色创建具有缩放效果的Mask实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      fillColor?: Color): Mask--><!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,      fillColor?: Color): Mask-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap | 是 |
| srcRect | common2D.Rect | 是 |
| dstRect | common2D.Rect | 是 |
| fillColor | [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { image } from '@kit.ImageKit';
import { uiEffect, common2D } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

const colorBuffer = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  let srcRect: common2D.Rect = {
    left: 0,
    top: 0,
    right: 1,
    bottom: 1
  };
  let dstRect: common2D.Rect = {
    left: 0,
    top: 0,
    right: 1,
    bottom: 1
  };
  let fillColor: uiEffect.Color = {
    red: 0,
    green: 0,
    blue: 0,
    alpha: 1
  };
  let mask = uiEffect.Mask.createPixelMapMask(pixelMap, srcRect, dstRect, fillColor);
}).catch((error: BusinessError)=>{
  console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
});
```

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap): Mask
```

通过输入的pixelMap创建Mask实例。该接口不会对传入的pixelMap进行缩放处理。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap): Mask--><!--Device-Mask-static createPixelMapMask(pixelMap: image.PixelMap): Mask-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
      const path: string = context.resourceDir + '/perlin_worley_noise_3d_64.bmp';
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
      distortProgress: this.distortProgress,
      rippleProgress: this.rippleProgress,
      distortFactor: this.distortFactor,
      materialFactor: this.materialFactor,
      refractionFactor: this.refractionFactor,
      reflectionFactor: this.reflectionFactor,
      tintColor: [this.tintColorR, this.tintColorG, this.tintColorB, this.tintColorA],
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
      .width('100%').height('100%').align(Alignment.Center)
    }
    .backgroundImage($r('app.media.bg6'), ImageRepeat.NoRepeat) // the image should be created in local
    .width('100%').height('100%').align(Alignment.Center)
  }
}
```

## createRadialGradientMask

```TypeScript
static createRadialGradientMask(center: common2D.Point, radiusX: number, radiusY: number,
      gradients: Array<[number, number]>): Mask
```

通过输入椭圆中心点的位置、长短轴和形状参数创建椭圆遮罩效果Mask实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Mask-static createRadialGradientMask(center: common2D.Point, radiusX: double, radiusY: double,      gradients: Array<[double, double]>): Mask--><!--Device-Mask-static createRadialGradientMask(center: common2D.Point, radiusX: double, radiusY: double,      gradients: Array<[double, double]>): Mask-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| center | common2D.Point | 是 |
| radiusX | number | 是 |
| radiusY | number | 是 |
| gradients | Array & lt;[number, number] & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## createRippleMask

```TypeScript
static createRippleMask(center: common2D.Point, radius: number, width: number, offset?: number): Mask
```

通过输入波环圆心的位置、半径和宽度创建波环遮罩效果Mask实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Mask-static createRippleMask(center: common2D.Point, radius: double, width: double, offset?: double): Mask--><!--Device-Mask-static createRippleMask(center: common2D.Point, radius: double, width: double, offset?: double): Mask-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| center | common2D.Point | 是 |
| radius | number | 是 |
| width | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let mask = uiEffect.Mask.createRippleMask({x: 0.5, y: 1.0}, 0.5, 0.3, 0.0);
```

## createUseEffectMask

```TypeScript
static createUseEffectMask(useEffect: boolean): Mask
```

创建并设置Mask实例是否使用模糊缓存。此Mask实例专为liquidMaterial方法的useEffectMask参数设计， 用于声明材质效果是否使用模糊缓存以提升性能。将此Mask实例用于其他Filter或VisualEffect方法时， useEffect属性可能不生效。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Mask-static createUseEffectMask(useEffect: boolean): Mask--><!--Device-Mask-static createUseEffectMask(useEffect: boolean): Mask-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| useEffect | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
        distortProgress: this.distortProgress,
        rippleProgress: this.rippleProgress,
        distortFactor: this.distortFactor,
        materialFactor: this.materialFactor,
        refractionFactor: this.refractionFactor,
        reflectionFactor: this.reflectionFactor,
        tintColor: [this.tintColorR, this.tintColorG, this.tintColorB, this.tintColorA],
        ripplePosition: undefined,
      },
      uiEffect.Mask.createUseEffectMask(true), // useEffectMask使用示例
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
      .width('100%').height('100%').align(Alignment.Center)
    }
    .backgroundImage($r('app.media.bg6'), ImageRepeat.NoRepeat)
    .width('100%').height('100%').align(Alignment.Center)
  }
}
```

## createWaveGradientMask

```TypeScript
static createWaveGradientMask(center: common2D.Point, width: number, propagationRadius: number,
      blurRadius: number, turbulenceStrength?: number): Mask
```

输入波源中心位置、单波参数创建单波遮罩效果Mask实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Mask-static createWaveGradientMask(center: common2D.Point, width: double, propagationRadius: double,      blurRadius: double, turbulenceStrength?: double): Mask--><!--Device-Mask-static createWaveGradientMask(center: common2D.Point, width: double, propagationRadius: double,      blurRadius: double, turbulenceStrength?: double): Mask-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| center | common2D.Point | 是 |
| width | number | 是 |
| propagationRadius | number | 是 |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | 是 |
| turbulenceStrength | number | 否 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
// center: [0.5, 0.5]；width: 0.01; propagationRadius: 0.5; blurRadius: 0.1; turbulenceStrength: 0.1
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
        // 将Mask作为Filter的参数，实现屏幕中心向四周扩散的水波形状效果。
        .backgroundFilter(uiEffect.createFilter().edgeLight(1.0, null, mask))
    }
  }
}
```
