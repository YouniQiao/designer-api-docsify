# PictureDrawableDescriptor

Creates a **PictureDrawableDescriptor** object by passing a **Picture** object. This API inherits from [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptorloadedresult-i.md).

**Inheritance/Implementation:** PictureDrawableDescriptor extends [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md)

**Since:** 26.0.0

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor, AnimationOptions, AnimatedDrawableDescriptor, AnimationController, DrawableDescriptorLoadedResult, AnimationStopMode, PictureDrawableDescriptor, HdrCompositionConfig } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(src: image.Picture)
```

A constructor used to create a **PictureDrawableDescriptor** object.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [image.Picture](../../apis-image-kit/arkts-apis/arkts-image-image-picture-i.md) | Yes | Picture** object for creating **PictureDrawableDescriptor**. |

**Examples**

The following is the sample code for creating a PixelMapDrawableDescriptor object using ResourceStr:

```TypeScript
// xxx.ets
import { DrawableDescriptor, PixelMapDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct PixelMapDrawableDescriptorExample {
  // Create a PixelMapDrawableDescriptor object using Resource.
  // Replace $r('app.media.icon') with the image resource file you use.
  @State drawable: DrawableDescriptor = new PixelMapDrawableDescriptor($r('app.media.icon'))

  build() {
    Column() {
      Image(this.drawable)
        .width(100)
        .height(100)
        .margin({ bottom: 20 })
    }
  }
}
```

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

## setHdrComposition

```TypeScript
setHdrComposition(config: HdrCompositionConfig): void
```

Sets HDR composition.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [HdrCompositionConfig](arkts-arkui-arkui-drawabledescriptor-hdrcompositionconfig-i.md) | Yes | HDR composition configuration. |

**Examples**

```TypeScript
import { PictureDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';


@Entry
@Component
struct PictureDrawableDescriptorInvalidateTest {
  @State drawable: PictureDrawableDescriptor | undefined = undefined;

  async createPictureDrawableDescriptor() {
    let resMgr = this.getUIContext().getHostContext()?.resourceManager
    if (resMgr) {
      try {
        // Replace $r('app.media.heic') with the image resource file you use.
        let uint8buffer = resMgr.getMediaContentSync($r('app.media.heic').id)
        let imageSource = image.createImageSource(uint8buffer.buffer)
        // Configure decoding options and request to decode the GAINMAP and LHDR_GAINMAP auxiliary images for HDR composition.
        let options: image.DecodingOptionsForPicture = {
          desiredAuxiliaryPictures: [image.AuxiliaryPictureType.GAINMAP, image.AuxiliaryPictureType.LHDR_GAINMAP],
          desiredPixelFormat: image.PixelMapFormat.NV12
        }
        let picture = await imageSource.createPicture(options)
        let drawable = new PictureDrawableDescriptor(picture)
        imageSource.release()
        this.drawable = drawable
      } catch (error) {
        console.error(`get media content failed`)
      }
    }
  }

  build() {
    Column() {
      Image(this.drawable)
        .width(300)
        .height(225)
        .borderColor(Color.Red)
        .borderWidth(1)

      Button("Create PictureDrawableDescriptor").onClick((event: ClickEvent) => {
        this.createPictureDrawableDescriptor()
      })

      Button("Trigger Rebuild").onClick((event: ClickEvent) => {
        // Set the HDR composition and specify the position and size of the rectangle area for composition.
        this.drawable?.setHdrComposition({
          rect: {
            x: 200,
            y: 200,
            width: 300,
            height: 300
          }
        })
        this.drawable?.invalidate()
      })
    }
    .height('100%')
    .width('100%')
  }
}
```
