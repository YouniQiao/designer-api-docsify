# DrawableDescriptor

父类对象提供可重写的方法，包含：获取[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)实例，图片资源加载能力。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class DrawableDescriptor--><!--Device-unnamed-export declare class DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, AnimatedDrawableDescriptor, AnimationStopMode, AnimationOptions, AnimationController, DrawableDescriptorLoadedResult, LayeredDrawableDescriptor, PictureDrawableDescriptor, PixelMapDrawableDescriptor, HdrCompositionConfig } from 'kits/@kit.ArkUI';
```

## getPixelMap

```TypeScript
getPixelMap(): image.PixelMap | undefined
```

获取PixelMap实例。

> **说明：**
> > DrawableDescriptor对象通过[release](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#release)释放后，本接口返回undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-getPixelMap(): image.PixelMap | undefined--><!--Device-DrawableDescriptor-getPixelMap(): image.PixelMap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | Return the PixelMap of the calling DrawableDescriptor object. |

## invalidate

```TypeScript
invalidate(): void
```

重新绘制DrawableDescriptor。当前仅支持  
[PictureDrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-picturedrawabledescriptor-c.md)类型，其他DrawableDescriptor子类型触发后无效果。若DrawableDescriptor未绑定任何组件，则不会执行任何操作。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-invalidate(): void--><!--Device-DrawableDescriptor-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReleased

```TypeScript
isReleased(): boolean
```

查询DrawableDescriptor是否已被释放。返回true表示已释放，此时调用  
[getPixelMap](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#getpixelmap)、  
[getForeground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getforeground)、  
[getBackground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getbackground)、  
[getMask](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getmask)、  
[loadSync](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#loadsync)、  
[load](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#load)等接口，返回undefined或默认异常值；返回false表示未释放，对象可正常使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-isReleased(): boolean--><!--Device-DrawableDescriptor-isReleased(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | DrawableDescriptor是否已被释放。true表示已释放，false表示未释放。 |

## load

```TypeScript
load(): Promise<DrawableDescriptorLoadedResult>
```

发起图片资源的异步加载，并返回加载结果。使用Promise异步回调。

> **说明：**
> > DrawableDescriptor对象通过[release](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#release)释放后，本接口返回imageWidth和imageHeight均为
> -1的Promise结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-load(): Promise<DrawableDescriptorLoadedResult>--><!--Device-DrawableDescriptor-load(): Promise<DrawableDescriptorLoadedResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DrawableDescriptorLoadedResult&gt; | 图片资源的加载结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 111001 | resource loading failed. |

## loadSync

```TypeScript
loadSync(): DrawableDescriptorLoadedResult
```

发起图片资源的同步加载，并返回加载结果。

> **说明：**
> > DrawableDescriptor对象通过[release](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#release)释放后，本接口返回imageWidth和imageHeight均为
> -1的结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-loadSync(): DrawableDescriptorLoadedResult--><!--Device-DrawableDescriptor-loadSync(): DrawableDescriptorLoadedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DrawableDescriptorLoadedResult](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md) | 图片资源的加载结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 111001 | resource loading failed. |

## release

```TypeScript
release(): void
```

释放DrawableDescriptor持有的资源。调用release后，该对象将不可用，再调用  
[getPixelMap](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#getpixelmap)、  
[getForeground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getforeground)、  
[getBackground](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getbackground)、  
[getMask](arkts-arkui-arkui-drawabledescriptor-layereddrawabledescriptor-c.md#getmask)、  
[loadSync](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#loadsync)、  
[load](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md#load)等接口，返回undefined或默认异常值。重复调用release不会崩溃。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-release(): void--><!--Device-DrawableDescriptor-release(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

