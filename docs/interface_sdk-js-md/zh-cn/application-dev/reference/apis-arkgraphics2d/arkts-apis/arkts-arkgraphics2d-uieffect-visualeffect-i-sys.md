# VisualEffect

VisualEffect效果类，用于将背景颜色混合、边框光照、颜色渐变等效果添加到组件上。 在调用VisualEffect的方法前，需要先通过[createEffect](arkts-arkgraphics2d-uieffect-createeffect-f.md)创建一个VisualEffect实例。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## backgroundColorBlender

```TypeScript
backgroundColorBlender(blender: BrightnessBlender): VisualEffect
```

用于改变组件背景颜色的blender，目前仅支持提亮混合器。

**起始版本：** 12

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blender | [BrightnessBlender](arkts-arkgraphics2d-uieffect-brightnessblender-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

## borderLight

```TypeScript
borderLight(lightPosition: common2D.Point3d, lightColor: common2D.Color, lightIntensity: number,
      borderWidth: number): VisualEffect
```

为圆角矩形组件边框添加3D光照效果。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lightPosition | common2D.Point3d | 是 |
| [lightColor](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | common2D.Color | 是 |
| [lightIntensity](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-sensor-colorresponse-i-sys.md) | number | 是 |
| borderWidth | number | 是 |

**返回值：**

| 类型 |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## colorGradient

```TypeScript
colorGradient(colors: Array<Color>, positions: Array<common2D.Point>, strengths: Array<number>,
      alphaMask?: Mask): VisualEffect
```

此方法为组件添加颜色渐变效果。

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
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## distortionCollapse

```TypeScript
distortionCollapse(distortionParam: DistortionParam): VisualEffect
```

为组件添加非线性形变效果。典型应用场景包括页面坍塌动画、窗口关闭特效、卡片翻转动画、场景过渡效果等。
1. 该视效支持控件范围外的绘制，但仍会受到父控件Clip的影响。
2. 因包含前景Filter，未与EffectComponent组合使用时不兼容组件自身及子组件的部分视效（如BrightnessBlender或systemMaterial）。
3. 支持对系统材质进行扭曲，但是与EffectComponent组合使用时，会导致系统材质的背景扭曲。
4. 调用distortionCollapse时，会创建与形变后区域等大的离屏画布，再将当前组件（含子组件）
的内容绘制到离屏画布上，再对画布上的已有内容进行形变绘制。
5. 使用该实现方式时，如果不与EffectComponent组合使用，将导致systemMaterial、
backgroundEffect、brightness、blur等需要截屏的接口无法截取到正确的画面。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distortionParam | [DistortionParam](../../apis-arkui/arkts-components/arkts-arkui-distortionparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

## liquidMaterial

```TypeScript
liquidMaterial(param : LiquidMaterialEffectParam, useEffectMask: Mask, distortMask?: Mask,
      brightnessParam?: BrightnessParam): VisualEffect
```

此方法为组件添加材质效果。材质效果通过模拟物理材质的光学特性（折射、反射）和动态扰动效果， 实现玻璃、金属等材质的视觉呈现。可用于模拟玻璃质感UI、流体材质动画、磨砂玻璃效果等场景。

**起始版本：** 22

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [LiquidMaterialEffectParam](arkts-arkgraphics2d-uieffect-liquidmaterialeffectparam-i-sys.md) | 是 |
| useEffectMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 是 |
| distortMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | 否 |
| brightnessParam | [BrightnessParam](arkts-arkgraphics2d-uieffect-brightnessparam-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
