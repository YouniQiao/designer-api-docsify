# createFromBuilder

## Modules to Import

```TypeScript
import { componentSnapshot } from '@kit.ArkUI';
```

## createFromBuilder

```TypeScript
function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,
    delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void
```

Renders a custom component in the application background and outputs its snapshot. This API uses an asynchronous callback to return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the callback. > **NOTE：**> > - Since API version 12, you can use the [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getComponentSnapshot) > API in [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext) to obtain the [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md#ComponentSnapshot) > object associated with the current UI context. > > - To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots > has a delay of less than 500 ms. > > - Components in the builder do not support the setting of animation-related attributes, such as > transition. > > - If a component is on a time-consuming task, for example, an Image or Web component > that is loading online images, its loading may be still in progress when this API is called. In this case, the > output snapshot does not represent the component in the way it looks when the loading is successfully completed.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** createFromBuilder

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-componentSnapshot-function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,    delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void--><!--Device-componentSnapshot-function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>,    delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |
| delay | number | No |
| checkImageStatus | boolean | No |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [160001](../errorcode-snapshot.md#160001-image-loading-error) |

## Examples

```TypeScript
import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct OffscreenSnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  @Builder
  RandomBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Test menu item 1')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Test menu item 2')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
    }
    .width(100)
    .id("builder")
  }

  build() {
    Column() {
      Button("click to generate offscreen UI snapshot")
        .onClick(() => {
          // You are advised to use this.getUIContext().getComponentSnapshot().createFromBuilder().
          componentSnapshot.createFromBuilder(() => {
            this.RandomBuilder()
          },
            (error: Error, pixmap: image.PixelMap) => {
              if (error) {
                console.error(`error:${JSON.stringify(error)}`)
                return;
              }
              this.pixmap = pixmap
              // Save the pixmap to a file.
              // ....
              // Obtain the component size and position.
              let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
              console.info(info.size.width + ' ' + info.size.height + ' ' + info.localOffset.x + ' ' +
              info.localOffset.y + ' ' + info.windowOffset.x + ' ' + info.windowOffset.y)
            }, 320, true, { scale: 2, waitUntilRenderFinished: true })
        })
      Image(this.pixmap)
        .margin(10)
        .height(200)
        .width(200)
        .border({ color: Color.Black, width: 2 })
    }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
  }
}
```


## createFromBuilder

```TypeScript
function createFromBuilder(builder: CustomBuilder, delay?: number,
    checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>
```

Renders a custom component in the application background and outputs its snapshot. This API uses a promise to return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the callback. > **NOTE：**> > - Since API version 12, you can use the [getComponentSnapshot](arkts-arkui-arkui-uicontext-uicontext-c.md#getComponentSnapshot) > API in [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext) to obtain the [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md#ComponentSnapshot) > object associated with the current UI context. > > - To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots > has a delay of less than 500 ms. > > - Components in the builder do not support the setting of animation-related attributes, such as > transition. > > - If a component is on a time-consuming task, for example, an Image or Web component > that is loading online images, its loading may be still in progress when this API is called. In this case, the > output snapshot does not represent the component in the way it looks when the loading is successfully completed.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** createFromBuilder

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-componentSnapshot-function createFromBuilder(builder: CustomBuilder, delay?: number,    checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>--><!--Device-componentSnapshot-function createFromBuilder(builder: CustomBuilder, delay?: number,    checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes |
| delay | number | No |
| checkImageStatus | boolean | No |
| options | [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [160001](../errorcode-snapshot.md#160001-image-loading-error) |

## Examples

```TypeScript
import { componentSnapshot } from '@kit.ArkUI'
import { image } from '@kit.ImageKit'

@Entry
@Component
struct OffscreenSnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  @Builder
  RandomBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Test menu item 1')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Test menu item 2')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
    }
    .width(100)
    .id("builder")
  }

  build() {
    Column() {
      Button("click to generate offscreen UI snapshot")
        .onClick(() => {
          // You are advised to use this.getUIContext().getComponentSnapshot().createFromBuilder().
          componentSnapshot.createFromBuilder(() => {
            this.RandomBuilder()
          }, 320, true, { scale: 2, waitUntilRenderFinished: true })
            .then((pixmap: image.PixelMap) => {
              this.pixmap = pixmap
              // Save the pixmap to a file.
              // ....
              // Obtain the component size and position.
              let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
              console.info(`${info.size.width} ${info.size.height} ${info.localOffset.x} ${
              info.localOffset.y} ${info.windowOffset.x} ${info.windowOffset.y}`)
            }).catch((err: Error) => {
            console.error(`error:${err}`)
          })
        })
      Image(this.pixmap)
        .margin(10)
        .height(200)
        .width(200)
        .border({ color: Color.Black, width: 2 })
    }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
  }
}
```
