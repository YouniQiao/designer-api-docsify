# DrawableDescriptor

Represents the base class providing overridable methods for [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) acquisition and image resource loading.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor, AnimationOptions, AnimatedDrawableDescriptor, AnimationController, DrawableDescriptorLoadedResult, AnimationStopMode, PictureDrawableDescriptor, HdrCompositionConfig } from '@kit.ArkUI';
```

## getPixelMap

```TypeScript
getPixelMap(): image.PixelMap
```

Obtains this **PixelMap** instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) |

**Examples**

```TypeScript
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI'
import { image } from '@kit.ImageKit'

let resManager = this.getUIContext().getHostContext()?.resourceManager;
// Replace $r('app.media.app_icon') with the image resource file you use.
let pixmap: DrawableDescriptor = (resManager?.getDrawableDescriptor($r('app.media.icon')
  .id)) as DrawableDescriptor; // When the passed resource ID or name is a regular image, a DrawableDescriptor object is generated.
let pixmapNew: image.PixelMap | undefined = pixmap?.getPixelMap();
```

## invalidate

```TypeScript
invalidate(): void
```

Redraws **DrawableDescriptor**. Currently, this API is supported for the [PictureDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-picturedrawabledescriptor-c.md) type, and does not take effect for other **DrawableDescriptor** subtypes. If no component is bound to **DrawableDescriptor**, no operation is performed.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReleased

```TypeScript
isReleased(): boolean
```

Checks whether **DrawableDescriptor** is released. If **true** is returned, the object has been released. In this case, calling APIs such as [getPixelMap](#getpixelmap), [getForeground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getforeground), [getBackground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getbackground), [getMask](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getmask), [loadSync](#loadsync), and [load](#load) will throw error code 1110
02. If **false** is returned, the object has not been released and can be used normally.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## load

```TypeScript
load(): Promise<DrawableDescriptorLoadedResult>
```

Asynchronously loads the image resource and returns the loading result. This API uses a promise to return the result.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DrawableDescriptorLoadedResult](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [111001](../errorcode-drawable-descriptor.md#111001-failed-to-load-resources) |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) |

## loadSync

```TypeScript
loadSync(): DrawableDescriptorLoadedResult
```

Synchronously loads the image resource and returns the loading result.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DrawableDescriptorLoadedResult](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [111001](../errorcode-drawable-descriptor.md#111001-failed-to-load-resources) |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) |

## release

```TypeScript
release(): void
```

Releases the resource held by **DrawableDescriptor**. After the **release** API is called, the object becomes unavailable. In this case, if you call APIs such as [getPixelMap](#getpixelmap), [getForeground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getforeground), [getBackground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getbackground), [getMask](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getmask), [loadSync](#loadsync), and [load](#load) again, error code 111002 will be thrown. No crash occurs when the **release** API is called repeatedly.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
