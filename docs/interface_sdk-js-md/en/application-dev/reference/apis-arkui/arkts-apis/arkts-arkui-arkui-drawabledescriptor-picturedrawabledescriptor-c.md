# PictureDrawableDescriptor

Creates a **PictureDrawableDescriptor** object by passing a **Picture** object. This API inherits from [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md#DrawableDescriptorLoadedResult).

**Inheritance/Implementation:** PictureDrawableDescriptor extends [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#DrawableDescriptor)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class PictureDrawableDescriptor--><!--Device-unnamed-export class PictureDrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, AnimatedDrawableDescriptor, AnimationStopMode, AnimationOptions, AnimationController, DrawableDescriptorLoadedResult, LayeredDrawableDescriptor, PictureDrawableDescriptor, PixelMapDrawableDescriptor, HdrCompositionConfig } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(src: image.Picture)
```

A constructor used to create a **PictureDrawableDescriptor** object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PictureDrawableDescriptor-constructor(src: image.Picture)--><!--Device-PictureDrawableDescriptor-constructor(src: image.Picture)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.Picture | Yes | Picture** object for creating **PictureDrawableDescriptor**. |

## setHdrComposition

```TypeScript
setHdrComposition(config: HdrCompositionConfig): void
```

Sets HDR composition.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PictureDrawableDescriptor-setHdrComposition(config: HdrCompositionConfig): void--><!--Device-PictureDrawableDescriptor-setHdrComposition(config: HdrCompositionConfig): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [HdrCompositionConfig](arkts-arkui-arkui-drawabledescriptor-hdrcompositionconfig-i.md) | Yes | HDR composition configuration. |

