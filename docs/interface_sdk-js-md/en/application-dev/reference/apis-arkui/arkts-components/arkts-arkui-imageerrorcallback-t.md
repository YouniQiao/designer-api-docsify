# ImageErrorCallback

```TypeScript
type ImageErrorCallback = (error: ImageError) => void
```

Triggered when an error occurs during image loading.

This event is not triggered if the parameter type of the component is  
[AnimatedDrawableDescriptor]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void--><!--Device-unnamed-type ImageErrorCallback = (error: ImageError) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Object returned by the callback triggered when an exception occurs during image loading. |

