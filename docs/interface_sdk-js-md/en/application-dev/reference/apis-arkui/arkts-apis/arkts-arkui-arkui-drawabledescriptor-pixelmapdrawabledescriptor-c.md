# PixelMapDrawableDescriptor

Implements a **PixelMapDrawableDescriptor** object, which can be created by passing in a **PixelMap** object. Inherits from [DrawableDescriptor](../../apis-default/arkts-apis/arkts-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md).

**Inheritance/Implementation:** PixelMapDrawableDescriptor extends [DrawableDescriptor](../../apis-default/arkts-apis/arkts-arkui-drawabledescriptor-drawabledescriptor-c.md)

**Since:** 12

<!--Device-unnamed-export class PixelMapDrawableDescriptor--><!--Device-unnamed-export class PixelMapDrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor, AnimationOptions, AnimatedDrawableDescriptor, AnimationController, DrawableDescriptorLoadedResult, AnimationStopMode, PictureDrawableDescriptor, HdrCompositionConfig } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(src?: image.PixelMap)
```

A constructor used to create a **PixelMapDrawableDescriptor** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PixelMapDrawableDescriptor-constructor(src?: image.PixelMap)--><!--Device-PixelMapDrawableDescriptor-constructor(src?: image.PixelMap)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap | No | PixelMap** image data. |

**Examples**

```TypeScript
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // Sandbox paths (file://xx) and application resources are supported.
  @State animated1: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);
  @State animated2: AnimatedDrawableDescriptor | undefined = undefined;

  aboutToAppear() {
    let files = this.getUIContext().getHostContext()?.filesDir
    let originPath = files + "/flower.gif"
    let resultPath = fileUri.getUriFromPath(originPath)
    this.animated2 = new AnimatedDrawableDescriptor(resultPath, { iterations: -1 })
  }

  build() {
    Column() {
      Row() {
        Image(this.animated1).width(100).height(100)
        Image(this.animated2).width(100).height(100)
      }
    }
  }
}
```

## constructor

```TypeScript
constructor(src?: image.PixelMap | ResourceStr)
```

A constructor used to create a **PixelMapDrawableDescriptor** object through the PixelMap type or **ResourceStr**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PixelMapDrawableDescriptor-constructor(src?: image.PixelMap | ResourceStr)--><!--Device-PixelMapDrawableDescriptor-constructor(src?: image.PixelMap | ResourceStr)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap \| ResourceStr | No | PixelMap** image data. You can use application resources, system resources, sandbox paths (file://&lt;bundleName&gt;/&lt;sandboxPath&gt;), and Base64 strings to create **PixelMapDrawableDescriptor** objects. |

**Examples**

See [constructor](#constructor)

