# VisualEffect

VisualEffect class, used to apply background color blending, border lighting, color gradient, and other effects to a component. Before calling VisualEffect methods, you need to first create a VisualEffect instance through createEffect.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## backgroundColorBlender

```TypeScript
backgroundColorBlender(blender: BrightnessBlender): VisualEffect
```

A blender for changing the background color of the component. Currently, only the brightness blender is supported.

**Since:** 12

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blender | [BrightnessBlender](arkts-arkgraphics2d-uieffect-brightnessblender-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

## borderLight

```TypeScript
borderLight(lightPosition: common2D.Point3d, lightColor: common2D.Color, lightIntensity: number,
      borderWidth: number): VisualEffect
```

Adds a 3D lighting effect to the border of a rounded rectangle component.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lightPosition | common2D.Point3d | Yes |
| [lightColor](../../apis-notification-kit/arkts-apis/arkts-notification-notificationslot-notificationslot-i.md) | common2D.Color | Yes |
| [lightIntensity](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-sensor-colorresponse-i-sys.md) | number | Yes |
| borderWidth | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## colorGradient

```TypeScript
colorGradient(colors: Array<Color>, positions: Array<common2D.Point>, strengths: Array<number>,
      alphaMask?: Mask): VisualEffect
```

Adds a color gradient effect to the component.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colors | Array & lt;Color & gt; | Yes |
| positions | Array & lt;common2D.Point & gt; | Yes |
| strengths | Array & lt;number & gt; | Yes |
| alphaMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## distortionCollapse

```TypeScript
distortionCollapse(distortionParam: DistortionParam): VisualEffect
```

Adds a nonlinear deformation effect to the component. Typical application scenarios include page collapse animations, window close effects, card flip animations, scene transition effects, etc.NOTE
1. This visual effect supports drawing outside the bounds of the control,
but it is still subject to the clipping (Clip) of the parent control.
2. Because it contains a foreground Filter, some visual effects of the component itself and its child components
(e.g., BrightnessBlender or systemMaterial) are incompatible when not used in combination with the EffectComponent.
3. It supports distorting the system material, but when used in combination with the EffectComponent,
it will cause the background of the system material to be distorted.
4. When calling distortionCollapse, an offscreen canvas equal in size to the deformed area will be created.
The content of the current component (including child components) is then drawn onto this offscreen canvas, and the existing content on the canvas is drawn with deformation.
5. When using this implementation without combining with the EffectComponent, interfaces that require screen
capture, such as systemMaterial, backgroundEffect, brightness, and blur, will not be able to capture the correct screen.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| distortionParam | [DistortionParam](../../apis-arkui/arkts-components/arkts-arkui-distortionparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

## liquidMaterial

```TypeScript
liquidMaterial(param : LiquidMaterialEffectParam, useEffectMask: Mask, distortMask?: Mask,
      brightnessParam?: BrightnessParam): VisualEffect
```

Adds a material effect to the component. The material effect simulates the optical properties (refraction, reflection) and dynamic perturbation effects of physical materials to achieve visual representations of glass, metal, and other materials. It can be used for scenarios such as glass-textured UI, fluid material animation, frosted glass effects, etc.

**Since:** 22

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [LiquidMaterialEffectParam](arkts-arkgraphics2d-uieffect-liquidmaterialeffectparam-i-sys.md) | Yes |
| useEffectMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | Yes |
| distortMask | [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) | No |
| brightnessParam | [BrightnessParam](arkts-arkgraphics2d-uieffect-brightnessparam-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
