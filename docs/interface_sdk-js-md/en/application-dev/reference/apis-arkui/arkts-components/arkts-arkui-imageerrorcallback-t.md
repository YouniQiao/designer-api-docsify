# ImageErrorCallback

```TypeScript
type ImageErrorCallback = (error: ImageError) => void
```

Triggered when an error occurs during image loading. This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../../apis-na/arkts-apis/arkts-na-arkui-drawabledescriptor-animateddrawabledescriptor-c.md#AnimatedDrawableDescriptor).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void--><!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | [ImageError](arkts-arkui-imageerror-i.md) | Yes | Object returned by the callback triggered when an exception occurs during image loading. |

