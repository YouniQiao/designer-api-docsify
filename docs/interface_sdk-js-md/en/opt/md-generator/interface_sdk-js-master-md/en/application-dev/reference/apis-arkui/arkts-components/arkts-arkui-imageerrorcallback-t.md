# ImageErrorCallback

```TypeScript
type ImageErrorCallback = (error: ImageError) => void
```

Triggered when an error occurs during image loading.

This event is not triggered if the parameter type of the component is  
[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void--><!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| error | [ImageError](arkts-arkui-imageerror-i.md) | Yes |
