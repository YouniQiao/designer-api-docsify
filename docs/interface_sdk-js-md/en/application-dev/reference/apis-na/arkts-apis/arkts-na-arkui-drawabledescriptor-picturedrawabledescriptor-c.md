# PictureDrawableDescriptor

Use the PictureDrawableDescriptor class to get the resource of picture or resource descriptor information.

**Inheritance/Implementation:** PictureDrawableDescriptor extends [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#DrawableDescriptor)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class PictureDrawableDescriptor--><!--Device-unnamed-export declare class PictureDrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(src: image.Picture)
```

Creates a new PictureDrawableDescriptor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PictureDrawableDescriptor-constructor(src: image.Picture)--><!--Device-PictureDrawableDescriptor-constructor(src: image.Picture)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.Picture | Yes | Indicates the resource to create PictureDrawableDescriptor. |

## setHdrComposition

```TypeScript
setHdrComposition(config: HdrCompositionConfig): void
```

Set HDR composition config.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PictureDrawableDescriptor-setHdrComposition(config: HdrCompositionConfig): void--><!--Device-PictureDrawableDescriptor-setHdrComposition(config: HdrCompositionConfig): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [HdrCompositionConfig](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-hdrcompositionconfig-i.md) | Yes | Indicates the HDR composition config. |

