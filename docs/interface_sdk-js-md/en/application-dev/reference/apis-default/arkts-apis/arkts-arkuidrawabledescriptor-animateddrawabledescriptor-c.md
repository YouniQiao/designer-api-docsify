# AnimatedDrawableDescriptor

Define the data structure for PixelMap animations.

@extends DrawableDescriptor

**Inheritance/Implementation:** AnimatedDrawableDescriptor extends [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-drawabledescriptor-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class AnimatedDrawableDescriptor--><!--Device-unnamed-export declare class AnimatedDrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)
```

Creates a new AnimatedDrawableDescriptor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatedDrawableDescriptor-constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)--><!--Device-AnimatedDrawableDescriptor-constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelMaps | Array&lt;image.PixelMap&gt; | Yes | PixelMap List. |
| options | [AnimationOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-animationoptions-i.md) | No | Animation control options. |

## constructor

```TypeScript
constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)
```

Creates a new AnimatedDrawableDescriptor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatedDrawableDescriptor-constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)--><!--Device-AnimatedDrawableDescriptor-constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | ResourceStr \| Array&lt;image.PixelMap&gt; | Yes | animated images or local resource. |
| options | [AnimationOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-animationoptions-i.md) | No | Animation control options. |

## getAnimationController

```TypeScript
getAnimationController(id?: string): AnimationController | undefined
```

Get the animation controller of the component based on the component id.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatedDrawableDescriptor-getAnimationController(id?: string): AnimationController | undefined--><!--Device-AnimatedDrawableDescriptor-getAnimationController(id?: string): AnimationController | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | No | component id. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimationController](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-animationcontroller-i.md) \| undefined | Return the component of animation controller. |

