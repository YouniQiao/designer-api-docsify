# Filter

Filter效果类，用于将模糊、边缘像素扩展、水波纹等效果添加到组件上。在调用Filter的方法前， 需要先通过[createFilter](arkts-arkgraphics2d-uieffect-createfilter-f.md)创建一个Filter实例。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## bezierWarp

```TypeScript
bezierWarp(controlPoints: Array<common2D.Point>): Filter
```

将贝塞尔曲线变形的效果添加至组件上。该效果通过在图层边界上创建封闭的贝塞尔曲线，实现对图像的精准扭曲和形状调整。 贝塞尔曲线共有四段，首尾顺次相连，每段包含一个顶点和两个切点。典型应用场景包括人脸形变特效、卡片透视变形等。

**起始版本：** 20

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

## blurBubblesRise

```TypeScript
blurBubblesRise(param: BlurBubblesRiseEffectParam): Filter
```

应用模糊气泡上升效果到图像，模拟气泡在液体中上升的梦幻模糊扭曲效果。

**起始版本：** 26.0.0

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

## colorGradient

```TypeScript
colorGradient(colors: Array<Color>, positions: Array<common2D.Point>, strengths: Array<number>,
        alphaMask?: Mask): Filter
```

为组件内容添加颜色渐变效果。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colors | Array & lt;Color & gt; | 是 |
| positions | Array & lt;common2D.Point & gt; | 是 |
| strengths | Array & lt;number & gt; | 是 |
| alphaMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## contentLight

```TypeScript
contentLight(lightPosition: common2D.Point3d, lightColor: common2D.Color, lightIntensity: number,
      displacementMap?: Mask): Filter
```

为组件内容添加3D光照效果。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lightPosition | common2D.Point3d | 是 |
| [lightColor](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | common2D.Color | 是 |
| [lightIntensity](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-sensor-colorresponse-i-sys.md) | number | 是 |
| displacementMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## directionLight

```TypeScript
directionLight(direction: common2D.Point3d, color: Color, intensity: number, mask?: Mask, factor?: number): Filter
```

为组件内容提供基于Mask和平行光的光照效果。平行光从统一方向照射组件平面，所有光线方向一致， 不因距离衰减，光照强度在组件各处均匀分布，适合模拟太阳光等远距离光源场景。 与contentLight的点光源不同，平行光无需指定光源具体位置。通过Mask可控制光照细节， 通过factor可结合高度图增强浮雕效果。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | common2D.Point3d | 是 |
| color | [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) | 是 |
| intensity | number | 是 |
| mask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## displacementDistort

```TypeScript
displacementDistort(displacementMap: Mask, factor?: [number, number]): Filter
```

为组件内容添加扭曲效果。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displacementMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | [number, number] | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## distort

```TypeScript
distort(distortionK: number): Filter
```

将透镜畸变效果添加至组件上。

**起始版本：** 13

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distortionK | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## edgeLight

```TypeScript
edgeLight(alpha: number, color?: Color, mask?: Mask, bloom?: boolean): Filter
```

为组件内容检测边缘，并添加边缘高亮效果。该效果自动检测组件内容的边缘轮廓并叠加高亮描边。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alpha | number | 是 |
| color | [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) | 否 |
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

## flyInFlyOutEffect

```TypeScript
flyInFlyOutEffect(degree: number, flyMode: FlyMode): Filter
```

将飞入飞出形变效果添加至组件上。典型应用场景包括页面切换动画、窗口进出动画、对话框弹出动画、列表项进出动画等。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | number | 是 |
| flyMode | [FlyMode](arkts-arkgraphics2d-uieffect-flymode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## heatDistortion

```TypeScript
heatDistortion(param: HeatDistortionEffectParam): Filter
```

应用热浪扭曲效果到图像，模拟热空气流动产生的视觉扭曲效果。

**起始版本：** 26.0.0

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

## maskDispersion

```TypeScript
maskDispersion(dispersionMap: Mask, alpha: number, rFactor?: [number, number], gFactor?: [number, number],
      bFactor?: [number, number]): Filter
```

为组件内容添加由置换贴图控制的色散效果，模拟光线通过棱镜时的色散现象。典型应用场景包括炫彩特效、棱镜折射模拟等。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dispersionMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |
| alpha | number | 是 |
| rFactor | [number, number] | 否 |
| gFactor | [number, number] | 否 |
| bFactor | [number, number] | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## maskTransition

```TypeScript
maskTransition(alphaMask: Mask, factor?: number, inverse?: boolean): Filter
```

为组件内容提供基于Mask的转场效果，可用于页面切换动画、场景过渡效果等场景。不建议在屏幕尺寸发生改变的过程中使用此效果，如：旋转屏幕，折叠屏开合屏幕等。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alphaMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | number | 否 |
| inverse | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## pixelStretch

```TypeScript
pixelStretch(stretchSizes: Array<number>, tileMode: TileMode): Filter
```

将边缘像素扩展效果添加至组件上。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| stretchSizes | Array & lt;number & gt; | 是 |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## radiusGradientBlur

```TypeScript
radiusGradientBlur(radius: number, gradientParam: LinearGradientBlurOptions): Filter
```

为组件内容添加半径线性渐变模糊效果。

**起始版本：** 19

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |
| gradientParam | [LinearGradientBlurOptions](../../apis-arkui/arkts-components/arkts-arkui-lineargradientbluroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## variableRadiusBlur

```TypeScript
variableRadiusBlur(radius: number, radiusMap: Mask): Filter
```

为组件内容提供基于Mask的渐变模糊效果。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |
| radiusMap | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## waterRipple

```TypeScript
waterRipple(progress: number, waveCount: number, x: number, y: number, rippleMode: WaterRippleMode): Filter
```

将水波纹效果添加至组件上。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| progress | number | 是 |
| waveCount | number | 是 |
| x | number | 是 |
| y | number | 是 |
| rippleMode | [WaterRippleMode](arkts-arkgraphics2d-uieffect-waterripplemode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
