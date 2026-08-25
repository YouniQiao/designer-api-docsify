# Filter

Filter效果类，用于将模糊、边缘像素扩展、水波纹等效果添加到组件上。在调用Filter的方法前， 需要先通过[createFilter](arkts-arkgraphics2d-uieffect-createfilter-f.md)创建一个Filter实例。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## bezierWarp

```TypeScript
bezierWarp(controlPoints: Array<common2D.Point>): Filter
```

将贝塞尔曲线变形的效果添加至组件上。该效果通过在图层边界上创建封闭的贝塞尔曲线，实现对图像的精准扭曲和形状调整。 贝塞尔曲线共有四段，首尾顺次相连，每段包含一个顶点和两个切点。典型应用场景包括人脸形变特效、卡片透视变形等。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controlPoints | Array & lt;common2D.Point & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import {
  $r,
  Column,
  Component,
  Entry,
  Image,
  State
} from '@kit.ArkUI';

import uiEffect from '@ohos.graphics.uiEffect'
import {common2D} from '@kit.ArkGraphics2D'

@Entry
@Component
struct BezierWarpExample {
  @State valueBezier: Array<common2D.Point> = [
    {x: 0, y: 0} as common2D.Point, {x: 1/3, y: 0} as common2D.Point, {x: 2/3, y: 0} as common2D.Point,     // top edge
    {x: 0.5, y: 0} as common2D.Point, {x: 0.5, y: 1/3} as common2D.Point, {x: 1, y: 2/3} as common2D.Point, // right edge
    {x: 1, y: 1} as common2D.Point, {x: 2/3, y: 1} as common2D.Point, {x: 1/3, y: 1} as common2D.Point,     // bottom edge
    {x: 0, y: 1} as common2D.Point, {x: 0, y: 2/3} as common2D.Point, {x: 0, y: 1/3} as common2D.Point]     // left edge

  build() {
    Column() {
      Image('test.jpg')
        .foregroundFilter(uiEffect.createFilter().bezierWarp(this.valueBezier.map((v:common2D.Point)=>v)))
        .height('1000px')
    }
  }
}
```

## blurBubblesRise

```TypeScript
blurBubblesRise(param: BlurBubblesRiseEffectParam): Filter
```

应用模糊气泡上升效果到图像，模拟气泡在液体中上升的梦幻模糊扭曲效果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [BlurBubblesRiseEffectParam](arkts-arkgraphics2d-uieffect-blurbubblesriseeffectparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**示例**

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct BlurBubblesRiseExample {
  private context: Context | undefined = this.getUIContext().getHostContext();
  @State blurIntensity: number = 0.8;
  @State mixStrength: number = 0.6;
  @State progress: number = 0.5;
  @State maskImage: image.PixelMap | null = null;

  aboutToAppear() {
    if (this.context) {
      this.getImagePixelMap(this.context)
    }
  }

  getImagePixelMap(context: Context) {
    let resourceMgr = context.resourceManager;
    resourceMgr?.getMediaContent($r('app.media.drawBlurMask').id)
      .then((val: Uint8Array) => {
        let buffer: ArrayBuffer = val.buffer.slice(0, val.buffer.byteLength)
        let imageSource: image.ImageSource = image.createImageSource(buffer);
        imageSource.createPixelMap().then((pixelmap: image.PixelMap) => {
          this.maskImage = pixelmap as PixelMap;
        })
      })
  }

  build() {
    Stack() {
      Image($r('app.media.test'))
        .width('100%')
        .height('100%')
        .foregroundFilter(uiEffect.createFilter().blurBubblesRise({
          blurIntensity: this.blurIntensity,
          mixStrength: this.mixStrength,
          progress: this.progress,
          maskImage: this.maskImage
        }))
    }
    .width('100%')
    .height('100%')
  }
}
```

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

为组件内容添加颜色渐变效果。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colors | Array & lt;Color & gt; | 是 |
| positions | Array & lt;common2D.Point & gt; | 是 |
| strengths | ArkTS-Dyn: Array & lt;number & gt;<br>ArkTS-Sta：Array & lt;double & gt; | 是 |
| alphaMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Column, Stack, State, Row, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'
import type common2D from '@ohos.graphics.common2D'

@Entry
@Component
struct ColorGradient {
  @State colors: Array<uiEffect.Color> = [
    {red: 1.0, green: 0.8, blue: 0.5, alpha: 0.8} as uiEffect.Color,
    {red: 1.0, green: 1.5, blue: 0.5, alpha: 1.0} as uiEffect.Color
  ]
  @State positions: Array<common2D.Point> = [
    {x: 0.2, y: 0.2} as common2D.Point,
    {x: 0.8, y: 0.6} as common2D.Point]
  @State strengths: Array<double> = [0.3, 0.3]

  build() {
    Column() {
      Row().width("100%").height("100%")
        .backgroundFilter(uiEffect.createFilter().colorGradient(this.colors.map((v: uiEffect.Color) => v),
          this.positions.map((v: common2D.Point) => v), this.strengths.map((v: double) => v)))
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { common2D, uiEffect } from "@kit.ArkGraphics2D"

@Entry
@Component
struct ColorGradientExample {
  build() {
    Stack() {
      Stack() {}
      .visualEffect(uiEffect.createEffect()
        .colorGradient(
          [
            {red: 1.0, green: 0.0, blue: 0.0, alpha: 1.0},
            {red: 0.0, green: 1.0, blue: 0.0, alpha: 1.0},
            {red: 0.0, green: 0.0, blue: 1.0, alpha: 1.0},
            {red: 1.0, green: 1.0, blue: 1.0, alpha: 1.0},
          ],
          [
            {x: 0.1, y: 0.1},
            {x: 0.1, y: 0.9},
            {x: 0.9, y: 0.1},
            {x: 0.9, y: 0.9},
          ],
          [12.4, 7.8, 7.8, 10.0],
          uiEffect.Mask.createRippleMask({x: 0.5, y: 0.5}, 0.2, 0.1)
        )
      )
      .width("1024px")
      .height("1024px")
    }
    .width("100%")
    .height("100%")
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Column, Stack, State, Row, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'
import type common2D from '@ohos.graphics.common2D'

@Entry
@Component
struct ColorGradient {
  @State colors: Array<uiEffect.Color> = [
    {red: 1.0, green: 0.8, blue: 0.5, alpha: 0.8} as uiEffect.Color,
    {red: 1.0, green: 1.0, blue: 0.5, alpha: 1.0} as uiEffect.Color
  ]
  @State positions: Array<common2D.Point> = [
    {x: 0.2, y: 0.2} as common2D.Point,
    {x: 0.8, y: 0.6} as common2D.Point]
  @State strengths: Array<double> = [0.3, 0.3]

  build() {
    Column() {
      Row().width("100%").height("100%")
        .backgroundFilter(uiEffect.createFilter().colorGradient(this.colors.map((v: uiEffect.Color) => v),
          this.positions.map((v: common2D.Point) => v), this.strengths.map((v: double) => v)))
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

为组件内容添加3D光照效果。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lightPosition | common2D.Point3d | 是 |
| [lightColor](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | common2D.Color | 是 |
| [lightIntensity](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-sensor-colorresponse-i-sys.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| displacementMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import {
  Entry,
  Component,
  State,
  Column,
  Stack,
  Image,
  $r,
  FlexAlign
} from '@kit.ArkUI';

import uiEffect from '@ohos.graphics.uiEffect'
import {common2D} from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  @State lightIntensity2:double = 1

  build() {
    Column() {
      Stack() {
        Image($r('app.media.man'))
          .width('646px')
          .height('900px')
          .borderRadius(10)
          .foregroundFilter(uiEffect.createFilter().contentLight(
            { x:0.0, y:0.0, z:2.0 } as common2D.Point3d,
            { red:255, blue:255, green:255, alpha:255 } as common2D.Color,
            this.lightIntensity2))
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

为组件内容提供基于Mask和平行光的光照效果。平行光从统一方向照射组件平面，所有光线方向一致， 不因距离衰减，光照强度在组件各处均匀分布，适合模拟太阳光等远距离光源场景。 与contentLight的点光源不同，平行光无需指定光源具体位置。通过Mask可控制光照细节， 通过factor可结合高度图增强浮雕效果。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | common2D.Point3d | 是 |
| color | [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | 是 |
| intensity | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| mask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

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

为组件内容添加扭曲效果。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displacementMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | ArkTS-Dyn: [number, number]<br>ArkTS-Sta：[double, double] | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Stack, State, Image, Row, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'

@Entry
@Component
struct DisplacementDistort {
  @State dfx: double = 20.0
  @State dfy: double = 20.0

  build() {
    Stack() {
      Image($r('app.media.man'))
      Row().width("100%").height("100%")
        .backgroundFilter(uiEffect.createFilter().displacementDistort(
          uiEffect.Mask.createRippleMask({ x: 0.5, y: 0.5 }, 0.2, 0.3, 0.0),
          [this.dfx, this.dfy] as [double, double]))
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

将透镜畸变效果添加至组件上。

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distortionK | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
filter.distort(-0.5)
```

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Column, Stack, Image, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'

@Entry
@Component
struct Distort {
  build() {
    Stack() {
      Image($r('app.media.man'))
        .foregroundFilter(uiEffect.createFilter().distort(-0.5))
    }
  }
}
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

为组件内容检测边缘，并添加边缘高亮效果。该效果自动检测组件内容的边缘轮廓并叠加高亮描边。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alpha | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| color | [Color](../../apis-arkui/arkts-apis/arkts-arkui-enums-color-e.md) | 否 |
| mask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |
| bloom | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Stack, State, Image, RelativeContainer, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'
import type common2D from '@ohos.graphics.common2D'

@Entry
@Component
struct EdgeLight {
  @State gradient: Array<[double, double]> = [[1,0] as [double, double], [1, 1] as [double, double]]

  build() {
    RelativeContainer() {
      Image($r('app.media.man'))
      Stack().width("100%").height("100%")
        .backgroundFilter(uiEffect.createFilter().edgeLight(1.0, { red: 1, blue: 1, green: 1, alpha: 1},
          uiEffect.Mask.createRadialGradientMask({ x: 0.5, y: 0.5 } as common2D.Point,
          0.5, 0.5, this.gradient.map<[double, double]>((v) => [v[0], v[1]] as [double, double])),
          false))
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

将飞入飞出形变效果添加至组件上。典型应用场景包括页面切换动画、窗口进出动画、对话框弹出动画、列表项进出动画等。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| flyMode | [FlyMode](arkts-arkgraphics2d-uieffect-flymode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
filter.flyInFlyOutEffect(0.5, uiEffect.FlyMode.TOP)
```

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Column, Stack, Image, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'

@Entry
@Component
struct FlyInFlyOutEffect {
  build() {
    Stack() {
      Image($r('app.media.man'))
        .foregroundFilter(uiEffect.createFilter().flyInFlyOutEffect(0.5, uiEffect.FlyMode.TOP))
    }
  }
}
```

## heatDistortion

```TypeScript
heatDistortion(param: HeatDistortionEffectParam): Filter
```

应用热浪扭曲效果到图像，模拟热空气流动产生的视觉扭曲效果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [HeatDistortionEffectParam](arkts-arkgraphics2d-uieffect-heatdistortioneffectparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**示例**

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';

@Entry
@Component
struct HeatDistortionExample {
  @State intensity: number = 0.8;
  @State noiseScale: number = 2.0;
  @State riseWeight: number = 0.5;
  @State progress: number = 0.3;

  build() {
    Stack() {
      Image($r('app.media.test'))
        .width('100%')
        .height('100%')
        .foregroundFilter(uiEffect.createFilter().heatDistortion({
          intensity: this.intensity,
          noiseScale: this.noiseScale,
          riseWeight: this.riseWeight,
          progress: this.progress
        }))
    }
    .width('100%')
    .height('100%')
  }
}
```

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

为组件内容添加由置换贴图控制的色散效果，模拟光线通过棱镜时的色散现象。典型应用场景包括炫彩特效、棱镜折射模拟等。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dispersionMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |
| alpha | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| rFactor | ArkTS-Dyn: [number, number]<br>ArkTS-Sta：[double, double] | 否 |
| gFactor | ArkTS-Dyn: [number, number]<br>ArkTS-Sta：[double, double] | 否 |
| bFactor | ArkTS-Dyn: [number, number]<br>ArkTS-Sta：[double, double] | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import {image} from '@kit.ImageKit'
import {common2D, uiEffect} from '@kit.ArkGraphics2D'
import {common} from '@kit.AbilityKit'

@Entry
@Component
struct MaskDispersion {
  @State pixelMap_: PixelMap | null = null
  @State src: common2D.Rect = { left: 0, top: 0, right: 1.0, bottom: 1.0 }
  @State dst: common2D.Rect = { left: 0, top: 0, right: 1.0, bottom: 1.0 }
  @State fillColor: uiEffect.Color = { red: 0, green: 0, blue: 0, alpha: 0 }

  onPageShow(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext
    context.resourceManager.getMediaByName("mask_alpha").then(val => {
      let buffer = val.buffer.slice(0, val.buffer.byteLength)
      let imageSource = image.createImageSource(buffer);
      imageSource.createPixelMap().then(pixelMap => {
        this.pixelMap_ = pixelMap
      })
    })
  }

  build() {
    Stack() {
      Image($rawfile('test.png'))
      Row()
        .width("100%")
        .height("100%")
        .backgroundFilter(uiEffect.createFilter().maskDispersion(
          uiEffect.Mask.createPixelMapMask(this.pixelMap_, this.src, this.dst, this.fillColor),
          1.0,
          [0.5, -0.5],
          [0.0, 0.0],
          [-0.5, 0.5]))
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Stack, State, Image, RelativeContainer, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'

@Entry
@Component
struct MaskDispersion {
  @State centerX: double = 0.5
  @State centerY: double = 0.5
  @State radius: double = 0.5
  @State rf: [double, double] = [0.3, -0.3] as [double, double]
  @State gf: [double, double] = [0, 0] as [double, double]
  @State bf: [double, double] = [-0.3, 0.3] as [double, double]

  build() {
    RelativeContainer() {
      Image($r('app.media.man'))
      Stack().width("100%").height("100%")
        .backgroundFilter(uiEffect.createFilter().maskDispersion(
          uiEffect.Mask.createRippleMask({ x: this.centerX, y: this.centerY }, this.radius, 0.3, 0.0),
          1.0, this.rf, this.gf, this.bf))
    }
  }
}
```

## maskTransition

ArkTS-Dyn:
```TypeScript
maskTransition(alphaMask: Mask, factor?: number, inverse?: boolean): Filter
```

ArkTS-Sta:
```TypeScript
maskTransition(alphaMask: Mask, factor?: double, inverse?: boolean): Filter
```

为组件内容提供基于Mask的转场效果，可用于页面切换动画、场景过渡效果等场景。不建议在屏幕尺寸发生改变的过程中使用此效果，如：旋转屏幕，折叠屏开合屏幕等。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alphaMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | ArkTS-Dyn: number<br>ArkTS-Sta：double | 否 |
| inverse | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

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
      // 转场前页面
      Image($r("app.media.before")).width("100%").height("100%")
        if (this.enterNewPage){
          // 转场后页面
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

将边缘像素扩展效果添加至组件上。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| stretchSizes | ArkTS-Dyn: Array & lt;number & gt;<br>ArkTS-Sta：Array & lt;double & gt; | 是 |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
filter.pixelStretch([0.2, 0.2, 0.2, 0.2], uiEffect.TileMode.CLAMP)
```

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Column, Stack, Image, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'

@Entry
@Component
struct PixelStretch {
  build() {
    Stack() {
      Image($r('app.media.startIcon')).width(300).height(300)
      Column().width(300).height(300)
        .compositingFilter(uiEffect.createFilter().pixelStretch([-0.2, -0.2, -0.2, -0.2], uiEffect.TileMode.MIRROR))
    }
  }
}
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

为组件内容添加半径线性渐变模糊效果。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| gradientParam | [LinearGradientBlurOptions](../../apis-arkui/arkts-apis/arkts-arkui-common-lineargradientbluroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { uiEffect } from "@kit.ArkGraphics2D"

@Entry
@Component
struct RadiusGradientBlurExample {
  @State blurRadiusExample: number = 64
  @State linearGradientBlurOptionsExample: LinearGradientBlurOptions =
    {fractionStops: [[0.0, 0.0], [1.0, 1.0]], direction: GradientDirection.Bottom}

  build() {
    Column() {
      Image($rawfile('test.png'))
        .compositingFilter(uiEffect.createFilter().radiusGradientBlur(this.blurRadiusExample,
          this.linearGradientBlurOptionsExample))
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Column, Image, Stack, State, Row, $r, LinearGradientBlurOptions, GradientDirection, FractionStop } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'
import type common2D from '@ohos.graphics.common2D'

@Entry
@Component
struct RadiusGradientBlur {
  @State filter: uiEffect.Filter = uiEffect.createFilter()

  build() {
    Column() {
      Image($r('app.media.man'))
        .compositingFilter(this.filter)
        .onAppear(() => {
          let blurOptions: LinearGradientBlurOptions = {
            fractionStops: [[0.0, 0.0] as FractionStop, [1.0, 1.0] as FractionStop] as Array<FractionStop>,
            direction: GradientDirection.Bottom
          } as LinearGradientBlurOptions
          this.filter = uiEffect.createFilter().radiusGradientBlur(64, blurOptions)
        })
    }
  }
}
```

## variableRadiusBlur

ArkTS-Dyn:
```TypeScript
variableRadiusBlur(radius: number, radiusMap: Mask): Filter
```

ArkTS-Sta:
```TypeScript
variableRadiusBlur(radius: double, radiusMap: Mask): Filter
```

为组件内容提供基于Mask的渐变模糊效果。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| radiusMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

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

将水波纹效果添加至组件上。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| progress | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| waveCount | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| rippleMode | [WaterRippleMode](arkts-arkgraphics2d-uieffect-waterripplemode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
filter.waterRipple(0.5, 2, 0.5, 0.5, uiEffect.WaterRippleMode.SMALL2SMALL)
```

ArkTS-Sta示例：

```TypeScript
import { Entry, Component, Column, Stack, Image, Row, $r } from '@kit.ArkUI'
import uiEffect from '@ohos.graphics.uiEffect'

@Entry
@Component
struct WaterRipple {
  build() {
    Stack() {
      Row() {}
        .width("100%").height("100%")
        .backgroundFilter(uiEffect.createFilter().
          waterRipple(0.6, 2, 0.5, 0.5, uiEffect.WaterRippleMode.SMALL2MEDIUM_RECV))
        .opacity(1)
    }
    .width("100%").height("100%")
    .backgroundImage($r('app.media.1'))
  }
}
```
