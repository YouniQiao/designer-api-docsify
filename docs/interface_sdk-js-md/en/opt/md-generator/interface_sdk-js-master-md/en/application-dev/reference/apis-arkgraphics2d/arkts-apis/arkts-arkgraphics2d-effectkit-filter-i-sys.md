# Filter

An image effect class used to add a specified effect to the effect chain through chained calls. It is suitable for scenarios such as image filter processing, visual effect enhancement, and image beautification. Before calling the methods of Filter, you need to create a Filter instance via createEffect. After adding effects, you need to call getEffectPixelMap to obtain the processed image.

**Since:** 23

**Deprecated since:** -1

<!--Device-effectKit-interface Filter--><!--Device-effectKit-interface Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { effectKit } from '@kit.ArkGraphics2D';
```

## ellipticalGradientBlur

```TypeScript
ellipticalGradientBlur(blurRadius: number, center: EllipticalMaskCenter,
      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter
```

Adds the elliptical gradient blur effect to the filter linked list, and returns the head node of the linked list.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-ellipticalGradientBlur(blurRadius: double, center: EllipticalMaskCenter,      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter--><!--Device-Filter-ellipticalGradientBlur(blurRadius: double, center: EllipticalMaskCenter,      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| center | [EllipticalMaskCenter](arkts-arkgraphics2d-effectkit-ellipticalmaskcenter-t-sys.md) | Yes |
| maskRadius | [EllipticalMaskRadius](arkts-arkgraphics2d-effectkit-ellipticalmaskradius-t-sys.md) | Yes |
| fractionStops | [FractionStop](../../apis-arkui/arkts-components/arkts-arkui-fractionstop-t.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass in the read image data
function ImageEllipticalGradientBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    let blurRadius:number = 25;
    let fractionStops:FractionStop[] = [[0, 0.2], [0.5, 0.7]];
    let maskRadius:effectKit.EllipticalMaskRadius = [1, 1];
    let center:effectKit.EllipticalMaskCenter = [0.5, 0.5];
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an effect identifier to the image
        headFilter.ellipticalGradientBlur(blurRadius, center, maskRadius, fractionStops);
        // Process the image according to the added effect identifier and return the processed image data
        headFilter.getEffectPixelMap(false).then(imageData => {
          resolve(imageData);
        });
      }
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file from the rawfile folder. You can also change the reading method as needed, as long as the final image data is in ArrayBuffer format.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // Image processing is an asynchronous operation. You can add await for synchronization as needed, depending on whether you need to obtain the processed image data before proceeding to the next step.
    this.imagePixelMap = await ImageEllipticalGradientBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```
