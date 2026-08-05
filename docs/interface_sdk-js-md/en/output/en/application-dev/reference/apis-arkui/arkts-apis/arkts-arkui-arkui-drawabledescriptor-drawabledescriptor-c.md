# DrawableDescriptor

Use the DrawableDescriptor class to get drawable image.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class DrawableDescriptor--><!--Device-unnamed-export declare class DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getPixelMap

```TypeScript
getPixelMap(): image.PixelMap | undefined
```

Get pixelMap of drawable image.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-getPixelMap(): image.PixelMap | undefined--><!--Device-DrawableDescriptor-getPixelMap(): image.PixelMap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | - Return the PixelMap of the calling DrawableDescriptor object. |

## invalidate

```TypeScript
invalidate(): void
```

Redraw the DrawableDescriptor. Does nothing if the DrawableDescriptor is not bound to any component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-invalidate(): void--><!--Device-DrawableDescriptor-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReleased

```TypeScript
isReleased(): boolean
```

Releases the DrawableDescriptor object. After release, any method call that accesses the object's internal data wll fail.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-isReleased(): boolean--><!--Device-DrawableDescriptor-isReleased(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return true if the DrawableDescriptor object has been released, or false if not. |

## load

```TypeScript
load(): Promise<DrawableDescriptorLoadedResult>
```

Asynchronously loads image and returns loading result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-load(): Promise<DrawableDescriptorLoadedResult>--><!--Device-DrawableDescriptor-load(): Promise<DrawableDescriptorLoadedResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DrawableDescriptorLoadedResult&gt; | - The image loading result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [111001](../errorcode-drawable-descriptor.md#111001-failed-to-load-resources) | resource loading failed. |

## loadSync

```TypeScript
loadSync(): DrawableDescriptorLoadedResult
```

Synchronously loads the image and returns the loading result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-loadSync(): DrawableDescriptorLoadedResult--><!--Device-DrawableDescriptor-loadSync(): DrawableDescriptorLoadedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - loading outcome. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [111001](../errorcode-drawable-descriptor.md#111001-failed-to-load-resources) | resource loading failed. |

## release

```TypeScript
release(): void
```

Release the DrawableDescriptor object. After relase, any method call that accesses the object's internal data will fail.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-release(): void--><!--Device-DrawableDescriptor-release(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

