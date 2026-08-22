# DrawableDescriptor

Represents the base class providing overridable methods for [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) acquisition and image resource loading.

**Since:** 10

<!--Device-unnamed-export class DrawableDescriptor--><!--Device-unnamed-export class DrawableDescriptor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor, AnimationOptions, AnimatedDrawableDescriptor, AnimationController, DrawableDescriptorLoadedResult, AnimationStopMode, PictureDrawableDescriptor, HdrCompositionConfig } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor()
```

Creates a new DrawableDescriptor.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-DrawableDescriptor-constructor()--><!--Device-DrawableDescriptor-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

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

