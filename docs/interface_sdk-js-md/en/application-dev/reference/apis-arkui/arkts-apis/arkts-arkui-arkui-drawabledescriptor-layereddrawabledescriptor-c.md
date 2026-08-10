# LayeredDrawableDescriptor

当传入资源id或name为包含前景和背景资源的json文件时，生成LayeredDrawableDescriptor对象。继承自  
[DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md)。

drawable.json位于项目工程entry/src/main/resources/base/media目录下。定义请参考：

**Inheritance/Implementation:** LayeredDrawableDescriptor extends [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class LayeredDrawableDescriptor extends DrawableDescriptor--><!--Device-unnamed-export declare class LayeredDrawableDescriptor extends DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, AnimatedDrawableDescriptor, AnimationStopMode, AnimationOptions, AnimationController, DrawableDescriptorLoadedResult, LayeredDrawableDescriptor, PictureDrawableDescriptor, PixelMapDrawableDescriptor, HdrCompositionConfig } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(
    foreground?: DrawableDescriptor,
    background?: DrawableDescriptor,
    mask?: DrawableDescriptor
  )
```

LayeredDrawableDescriptor的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-constructor(    foreground?: DrawableDescriptor,    background?: DrawableDescriptor,    mask?: DrawableDescriptor  )--><!--Device-LayeredDrawableDescriptor-constructor(    foreground?: DrawableDescriptor,    background?: DrawableDescriptor,    mask?: DrawableDescriptor  )-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| foreground | [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | No | 分层图标的前景图片选项。 |
| background | [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | No | 分层图标的背景图片选项。 |
| mask | [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | No | 分层图标的遮罩选项。 |

## constructor

```TypeScript
constructor(
```

Creates a new LayeredDrawableDescriptor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-LayeredDrawableDescriptor-constructor(--><!--Device-LayeredDrawableDescriptor-constructor(-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getBackground

```TypeScript
getBackground(): DrawableDescriptor | undefined
```

获取背景的DrawableDescriptor对象。

> **说明：**
> > DrawableDescriptor对象通过[release](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#release)释放后，本接口返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-getBackground(): DrawableDescriptor | undefined--><!--Device-LayeredDrawableDescriptor-getBackground(): DrawableDescriptor | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | Return the DrawableDescriptor object of background. |

## getForeground

```TypeScript
getForeground(): DrawableDescriptor | undefined
```

获取前景的DrawableDescriptor对象。

> **说明：**
> > DrawableDescriptor对象通过[release](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#release)释放后，本接口返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-getForeground(): DrawableDescriptor | undefined--><!--Device-LayeredDrawableDescriptor-getForeground(): DrawableDescriptor | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | Return the DrawableDescriptor object of foreground. |

## getMask

```TypeScript
getMask(): DrawableDescriptor | undefined
```

获取蒙版的DrawableDescriptor对象。

> **说明：**
> > DrawableDescriptor对象通过[release](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#release)释放后，本接口返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-getMask(): DrawableDescriptor | undefined--><!--Device-LayeredDrawableDescriptor-getMask(): DrawableDescriptor | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) | Return the DrawableDescriptor object of mask. |

## getMaskClipPath

```TypeScript
static getMaskClipPath(): string
```

LayeredDrawableDescriptor的静态方法，获取系统内置的裁切路径参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-static getMaskClipPath(): string--><!--Device-LayeredDrawableDescriptor-static getMaskClipPath(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回裁切路径的命令字符串。 |

## setBlendMode

```TypeScript
setBlendMode(mode: drawing.BlendMode | undefined): void
```

设置LayeredDrawableDescriptor的混合模式。对同一LayeredDrawableDescriptor对象多次调用setBlendMode接口时，仅在绘制完成前的最后一次调用生效。该接口不支持动态切换。LayeredDrawableDescriptor的默认绘制顺序为背景、蒙版、前景。设置了混合模式后，绘制顺序变为背景、前景、蒙版。若设置的值无效，会按照未设置混合模式进行绘制。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayeredDrawableDescriptor-setBlendMode(mode: drawing.BlendMode | undefined): void--><!--Device-LayeredDrawableDescriptor-setBlendMode(mode: drawing.BlendMode | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | drawing.BlendMode \| undefined | Yes | 混合模式。设置undefined，会按照未设置混合模式进行绘制。 |

