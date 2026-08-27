# DynamicRangeModeOptions

Defines the dynamic range mode used for the snapshot.

**Since:** 23

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { componentSnapshot } from '@kit.ArkUI';
```

## dynamicRangeMode

```TypeScript
dynamicRangeMode?: DynamicRangeMode
```

Dynamic range mode used for the snapshot.

By default, the system snapshots in STANDARD mode. If the dynamic range mode used by the target component is known, you can specify the dynamic range mode using the **dynamicRangeMode** field and set **isAuto** to **false** to achieve the expected snapshot effect.

There are three dynamic range modes available. HDR is applied for **HIGH** and **CONSTRAINT** modes, and SDR is applied for **STANDARD** mode.

After a valid dynamic range mode is specified, the dynamic range to be used for the snapshot is determined by both the target component and the specified mode. The details are as follows:

1. If SDR is used for the component, SDR is applied for the snapshot even if the dynamic range mode is set to **HIGH**.
2. If HDR is used for the component, the specified dynamic range mode is applied for the screenshot.
3. If the [color space](arkts-arkui-componentsnapshot-colormodeoptions-i.md) is set to **SRGB** or **DISPLAY_P3**, SDR is applied for the snapshot.
4. If both SDR and HDR are used for the child components, HDR is applied for the snapshot.
5. If both conditions 3 and 4 are met, SDR is applied for the snapshot.

For details about the enum values, see DynamicRangeMode.

Default value: **STANDARD**

If the value is **undefined**, **null**, or not set, the default value is used. If an abnormal value is used, snapshot capture fails and the error code 160003 is returned.

**Type:** DynamicRangeMode

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isAuto

```TypeScript
isAuto?: boolean
```

Whether the system automatically determines the dynamic range mode to be used.

The value **true** means to allow the system to automatically determine the dynamic range mode to be used, and **false** means to manually set the dynamic range mode through **dynamicRangeMode**. If an invalid value is used, the default value **false** is used.

Default value: **false**

For offscreen snapshots, this parameter can only be set to **false**. Otherwise, the error code 160004 will be returned.

If `isAuto` is set to **true**, you are advised to set `waitUntilRenderFinished` in [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) to **true** to ensure that the system can properly detect the used dynamic range mode.

If the dynamic range mode used by the component is uncertain, you are advised to set **isAuto** to **true** so that the system can automatically determine the dynamic range mode to be used.

When **isAuto** is set to true, the value of **dynamicRangeMode** is ignored.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotDynamicRangeExample {
  @State pixmap: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // Replace $r('app.media.img') with the image resource file you use.
        Image($r('app.media.img'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id('root')
      }

      Button('click to generate UI snapshot')
        .onClick(() => {
          this.getUIContext().getComponentSnapshot().get('root', (error: Error, pixmap: image.PixelMap) => {
            if (error) {
              console.error(`error:${JSON.stringify(error)}`);
              return;
            }
            this.pixmap = pixmap;
          }, {
            scale: 2,
            waitUntilRenderFinished: true,
            // Set isAuto to true for the dynamic range mode.
            dynamicRangeMode: { dynamicRangeMode: DynamicRangeMode.STANDARD, isAuto: true }
          })
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}
```
