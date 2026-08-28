# ImageSpan

As a child of the Text and ContainerSpan components, the **ImageSpan** component is used to display inline images.

## Child Components

Not supported

## ImageSpan

```TypeScript
ImageSpan(value: ResourceStr | PixelMap)
```

Defines the constructor of ImageSpan.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Test API:** This is a test API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| PixelMap | Yes | Image source. Both local and network images are supported. When using an image referenced using a relative path, for example, **ImageSpan("common/test.jpg")**, the **ImageSpan** component cannot be called across bundles or modules. Therefore, you are advised to use **\$r** to reference image resources that need to be used globally. - The supported formats include PNG, JPG, BMP, SVG, GIF, and HEIF. - Base64 strings are supported. The value format is data:image/[png\|jpeg\|bmp\|webp\|heif];base64, [base64 data], where *[base64 data]* is a Base64 string. - Character string prefixed with file://data/ storage, which is used to read image resources in the file folder in the application installation directory. Ensure that the application has the read permission to the files in the specified path. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ImageLoadResult](arkts-arkui-imageloadresult-i.md) | Describes the object returned after the callback is triggered when an image is successfully loaded or decoded. |

### Types

| Name | Description |
| --- | --- |
| [ImageCompleteCallback](arkts-arkui-imagecompletecallback-t.md) | Defines the callback triggered when the image is successfully loaded or decoded. |

## Examples

This example demonstrates the alignment and scaling effects of the ImageSpan component using the [verticalAlign](#verticalalign) and [objectFit](#objectfit) attributes, available since API version 10.

```TypeScript
// xxx.ets
@Entry
@Component
struct SpanExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text() {
        Span('This is the Span and ImageSpan component').fontSize(25).textCase(TextCase.Normal)
          .decoration({ type: TextDecorationType.None, color: Color.Pink })
      }.width('100%').textAlign(TextAlign.Center)

      Text() {
        // Replace $r('app.media.app_icon') with the image resource file you use.
        ImageSpan($r('app.media.app_icon'))
          .width('200px')
          .height('200px')
          .objectFit(ImageFit.Fill)
          .verticalAlign(ImageSpanAlignment.CENTER)
        Span('I am LineThrough-span')
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .width('50px')
          .height('50px')
          .verticalAlign(ImageSpanAlignment.TOP)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .size({ width: '100px', height: '100px' })
          .verticalAlign(ImageSpanAlignment.BASELINE)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .width('70px')
          .height('70px')
          .verticalAlign(ImageSpanAlignment.BOTTOM)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(50)
      }
      .width('100%')
      .textIndent(50)
    }.width('100%').height('100%').padding({ left: 0, right: 0, top: 0 })
  }
}
```

This example demonstrates how to set the background style for text using the [textBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11) attribute, available since API version 11.

```TypeScript
// xxx.ets
@Component
@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Text() {
          // Replace $r('app.media.sky') with the image resource file you use.
          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
            .borderRadius(20)
            .textBackgroundStyle({ color: '#7F007DFF', radius: "5vp" })
        }
      }.width('100%')
    }.height('100%')
  }
}
```

This example demonstrates how to add load success and load error events to the ImageSpan component using [onComplete](#oncomplete12) and [onError](#onerror12), available since API version 12.

```TypeScript
// xxx.ets
@Entry
@Component
struct Index {
  // Replace $r('app.media.app_icon') with the image resource file you use.
  @State src: ResourceStr = $r('app.media.app_icon');

  build() {
    Column() {
      Text() {
        ImageSpan(this.src)
          .width(100).height(100)
          .onError((err) => {
            console.info("onError: " + err.message);
          })
          .onComplete((event) => {
            console.info("onComplete: " + event.loadingStatus);
          })
      }
    }.width('100%').height('100%')
  }
}
```

This example demonstrates the effect of setting a color filter for the ImageSpan component using the [colorFilter](#colorfilter14) attribute, available since API version 14.

```TypeScript
// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct SpanExample {
  private ColorFilterMatrix: number[] = [0.239, 0, 0, 0, 0, 0, 0.616, 0, 0, 0, 0, 0, 0.706, 0, 0, 0, 0, 0, 1, 0];
  @State DrawingColorFilterFirst: ColorFilter | undefined = new ColorFilter(this.ColorFilterMatrix);

  build() {
    Row() {
      Column({ space: 10 }) {
        // Use a ColorFilter object to apply a color filter to the image.
        Text() {
          // Replace $r('app.media.sky') with the image resource file you use.
          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .colorFilter(this.DrawingColorFilterFirst)
        }

        // Create a color filter using the drawing.ColorFilter API.
        Text() {
          // Replace $r('app.media.sky') with the image resource file you use.
          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter({
              alpha: 255,
              red: 112,
              green: 112,
              blue: 112
            }, drawing.BlendMode.SRC))
        }
      }.width('100%')
    }.height('100%')
  }
}
```

This example demonstrates how to use the [alt](#alt12) attribute to display a placeholder image in the ImageSpan component while loading a network image, available since API version 12.

```TypeScript
// xxx.ets
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SpanExample {
  @State imageAlt: PixelMap | undefined = undefined;

  httpRequest() {
    // Enter an image URL.
    http.createHttp().request("https://www.example.com/xxx.png", (error: BusinessError, data: http.HttpResponse) => {
      if (error) {
        console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`);
      } else {
        console.info(`http request success.`);
        let imageData: ArrayBuffer = data.result as ArrayBuffer;
        let imageSource: image.ImageSource = image.createImageSource(imageData);

        class tmp {
          height: number = 100;
          width: number = 100;
        }

        let option: Record<string, number | boolean | tmp> = {
          'alphaType': 0, // Alpha type.
          'editable': false, // Whether the image is editable.
          'pixelFormat': 3, // Pixel format.
          'scaleMode': 1, // Scale mode.
          'size': { height: 100, width: 100 }
        };
        // Image size.
        imageSource.createPixelMap(option).then((pixelMap: PixelMap) => {
          this.imageAlt = pixelMap;
        })
      }
    })
  }

  build() {
    Column() {
      Button("Get Network Image")
        .onClick(() => {
          this.httpRequest();
        })

      Text() {
        // Enter an image URL.
        ImageSpan('https://www.example.com/xxx.png')
          .alt(this.imageAlt)
          .width(300)
          .height(300)
      }

    }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })
  }
}
```

This example shows how to enable enhanced SVG usability capabilities through the [SVG tag parsing enhancement feature](ts-image-svg2-capabilities.md#improved-svg-usability) by configuring the [supportSvg2](#supportsvg222) attribute, available since API version 22.

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('Styled string with supportSvg2: false')
        // Replace $r("app.media.ice") with the image resource file you use.
        Text() {
          ImageSpan($r("app.media.ice"))
            .width(50)
            .height(50)
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
              drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
        }
        Text('Styled string with supportSvg2: true')
        // Replace $r("app.media.ice") with the image resource file you use.
        Text() {
          ImageSpan($r("app.media.ice"))
            .width(50)
            .height(50)
            .supportSvg2(true)
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
              drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
