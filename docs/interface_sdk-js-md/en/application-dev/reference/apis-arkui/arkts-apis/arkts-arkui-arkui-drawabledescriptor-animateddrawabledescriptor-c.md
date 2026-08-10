# AnimatedDrawableDescriptor

使用[Image](../../apis-arkui/arkts-components/arkts-arkui-image.static-i)组件播放PixelMap数组或动图资源时传入AnimatedDrawableDescriptor对象，该对象继承自[DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md)。

**Inheritance/Implementation:** AnimatedDrawableDescriptor extends [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class AnimatedDrawableDescriptor extends DrawableDescriptor--><!--Device-unnamed-export declare class AnimatedDrawableDescriptor extends DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, AnimatedDrawableDescriptor, AnimationStopMode, AnimationOptions, AnimationController, DrawableDescriptorLoadedResult, LayeredDrawableDescriptor, PictureDrawableDescriptor, PixelMapDrawableDescriptor, HdrCompositionConfig } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)
```

AnimatedDrawableDescriptor的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatedDrawableDescriptor-constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)--><!--Device-AnimatedDrawableDescriptor-constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelMaps | Array&lt;image.PixelMap&gt; | Yes | PixelMap 数组类型参数，存储 PixelMap 图片数据。 |
| options | [AnimationOptions](arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | No | 动画控制选项。 |

## constructor

```TypeScript
constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)
```

AnimatedDrawableDescriptor的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatedDrawableDescriptor-constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)--><!--Device-AnimatedDrawableDescriptor-constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [ResourceStr](arkts-arkui-resourcestr-t.md) \| Array&lt;image.PixelMap&gt; | Yes | 动图资源地址或者 [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)对象构成的数组。&lt;br/&gt; ResourceStr当前支持的范围： 应用资源Resource，沙箱路径（file://&lt;bundleName&gt;/&lt;sandboxPath&gt;），BASE64字符串。 |
| options | [AnimationOptions](arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | No | 动画控制参数。 |

## getAnimationController

```TypeScript
getAnimationController(id?: string): AnimationController | undefined
```

获取动画控制器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatedDrawableDescriptor-getAnimationController(id?: string): AnimationController | undefined--><!--Device-AnimatedDrawableDescriptor-getAnimationController(id?: string): AnimationController | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | No | 组件的id。&lt;br/&gt;当[Image](../../apis-arkui/arkts-components/arkts-arkui-image.static-i)组件与 AnimatedDrawableDescriptor确保1比1持有（仅传入一个[Image](../../apis-arkui/arkts-components/arkts-arkui-image.static-i)组件）时， id非必填；&lt;br/&gt;若同一AnimatedDrawableDescriptor需绑定多个 [Image](../../apis-arkui/arkts-components/arkts-arkui-image.static-i)组件，则必须设置唯一id以准确获取对应组件的动画控制器 （唯一性由开发者保证）。&lt;br/&gt;此规则基于动画系统设计原则：动画数据可多组件共享，但各组件动画独立运行， AnimationController与组件严格1比1持有关系（一个组件一个AnimationController对象）。&lt;br/&gt;另外， [AnimatedDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)支持不可见时自动暂停播放功能，详见 [onVisibleAreaChange](arkts-arkui-common-commonmethod-i.md#onvisibleareachange)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimationController](arkts-arkui-arkui-drawabledescriptor-animationcontroller-i.md) | Return the component of animation controller. |

