# DrawableDescriptor

Represents the base class providing overridable methods for [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md#pixelmap) acquisition and image resource loading.

**Since:** 10

<!--Device-unnamed-export class DrawableDescriptor--><!--Device-unnamed-export class DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor } from 'DrawableDescriptor';
import { LayeredDrawableDescriptor } from 'LayeredDrawableDescriptor';
import { PixelMapDrawableDescriptor } from 'PixelMapDrawableDescriptor';
import { AnimationOptions } from 'AnimationOptions';
import { AnimatedDrawableDescriptor } from 'AnimatedDrawableDescriptor';
import { AnimationController } from 'AnimationController';
import { DrawableDescriptorLoadedResult } from 'DrawableDescriptorLoadedResult';
import { AnimationStopMode } from 'AnimationStopMode';
import { PictureDrawableDescriptor } from 'PictureDrawableDescriptor';
import { HdrCompositionConfig } from 'HdrCompositionConfig';
```

## getPixelMap

```TypeScript
getPixelMap(): image.PixelMap
```

Obtains this **PixelMap** instance.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DrawableDescriptor-getPixelMap(): image.PixelMap--><!--Device-DrawableDescriptor-getPixelMap(): image.PixelMap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | PixelMap** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) | The native memory referenced by the drawableDescriptor has been released.<br>**Applicable version:** 26.0.0 and later |

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

Redraws **DrawableDescriptor**. Currently, this API is supported for the [PictureDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-picturedrawabledescriptor-c.md#picturedrawabledescriptor) type, and does not take effect for other **DrawableDescriptor** subtypes. If no component is bound to **DrawableDescriptor**, no operation is performed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DrawableDescriptor-invalidate(): void--><!--Device-DrawableDescriptor-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReleased

```TypeScript
isReleased(): boolean
```

Checks whether **DrawableDescriptor** is released. If **true** is returned, the object has been released. In this case, calling APIs such as [getPixelMap](#getpixelmap), [getForeground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getforeground), [getBackground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getbackground), [getMask](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getmask), [loadSync](#loadsync), and [load](#load) will throw error code 1110 02. If **false** is returned, the object has not been released and can be used normally.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DrawableDescriptor-isReleased(): boolean--><!--Device-DrawableDescriptor-isReleased(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether **DrawableDescriptor** is released. The value **true** indicates that the object is released, and **false** indicates that the object is not released. |

## load

```TypeScript
load(): Promise<DrawableDescriptorLoadedResult>
```

Asynchronously loads the image resource and returns the loading result. This API uses a promise to return the result.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-DrawableDescriptor-load(): Promise<DrawableDescriptorLoadedResult>--><!--Device-DrawableDescriptor-load(): Promise<DrawableDescriptorLoadedResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DrawableDescriptorLoadedResult](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md)&gt; | Image resource loading result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [111001](../errorcode-drawable-descriptor.md#111001-failed-to-load-resources) | resource loading failed. |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) | The native memory referenced by the drawableDescriptor has been released.<br>**Applicable version:** 26.0.0 and later |

## loadSync

```TypeScript
loadSync(): DrawableDescriptorLoadedResult
```

Synchronously loads the image resource and returns the loading result.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-DrawableDescriptor-loadSync(): DrawableDescriptorLoadedResult--><!--Device-DrawableDescriptor-loadSync(): DrawableDescriptorLoadedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DrawableDescriptorLoadedResult](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md) | Image resource loading result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [111001](../errorcode-drawable-descriptor.md#111001-failed-to-load-resources) | resource loading failed. |
| [111002](../errorcode-drawable-descriptor.md#111002-resource-released) | The native memory referenced by the drawableDescriptor has been released.<br>**Applicable version:** 26.0.0 and later |

## release

```TypeScript
release(): void
```

Releases the resource held by **DrawableDescriptor**. After the **release** API is called, the object becomes unavailable. In this case, if you call APIs such as [getPixelMap](#getpixelmap), [getForeground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getforeground), [getBackground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getbackground), [getMask](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getmask), [loadSync](#loadsync), and [load](#load) again, error code 111002 will be thrown. No crash occurs when the **release** API is called repeatedly.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-DrawableDescriptor-release(): void--><!--Device-DrawableDescriptor-release(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

