# @ohos.arkui.components.ContainerReader

## Modules to Import

```TypeScript
import { ContainerReader, ContainerReaderAttribute, BreakpointOptions } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) | Defines the ContainerReader attribute functions. Provides methods for configuring container reading parameters and breakpoint analysis properties. |

### Interfaces

| Name | Description |
| --- | --- |
| [BreakpointOptions](arkts-arkui-arkui-components-containerreader-breakpointoptions-i.md) | Defines the breakpoint configuration options for container dimension analysis. Specifies threshold values that trigger different layout behaviors based on container size. |
| [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | Defines the configuration options for ContainerReader component. Used to specify the parameters for container dimension reading and breakpoint analysis. |
| [ContainerReaderInterface](arkts-arkui-arkui-components-containerreader-containerreaderinterface-i.md) | Defines the ContainerReader Component. Used for reading and analyzing container layout information based on size breakpoints in dynamic scenarios. Provides container dimension analysis and breakpoint detection capabilities. |

### Constants

| Name | Description |
| --- | --- |
| [ContainerReader](arkts-arkui-arkui-components-containerreader-con.md) | Defines ContainerReader Component. A component that analyzes container dimensions and provides breakpoint information for responsive layouts. |
| [ContainerReaderInstance](arkts-arkui-arkui-components-containerreader-con.md#containerreaderinstance) | Defines ContainerReader Component instance. Provides access to ContainerReader component methods for container dimension analysis and breakpoint detection. |

## Examples

This example demonstrates how the [ContainerReader](#containerreader-1) component obtains container size and breakpoint information through two-way binding, and switches the layout direction based on the width breakpoint.
The ContainerReader component is added since API version 26.0.0.

```TypeScript
// xxx.ets
import { ContainerReader, Size } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State containerSize: Size = { width: 0, height: 0 };
  @State widthBp: WidthBreakpoint = WidthBreakpoint.WIDTH_XS;
  @State heightBp: HeightBreakpoint = HeightBreakpoint.HEIGHT_SM;
  @State columnWidth: number = 180

  build() {
    Column({space: 10}) {
      Column({space: 10}) {
        ContainerReader({
          size: this.containerSize!!, // Bind to the this.containerSize variable. When the ContainerReader size changes, this.containerSize is automatically updated.
          widthBreakpoint: this.widthBp!!,
          heightBreakpoint: this.heightBp!!
        }) {
          // Switch layout direction based on the width breakpoint
          if (this.widthBp === WidthBreakpoint.WIDTH_XS) {
            Column({space: 20}) {
              Text('Vertical layout')
              Text(`Column`)
            }
            .width('100%')
            .height('100%')
            .backgroundColor('#D5D5D5')
            .justifyContent(FlexAlign.Center)
          } else {
            Row({space: 20}) {
              Text('Horizontal layout')
              Text(`Row`)
            }
            .width('100%')
            .height('100%')
            .backgroundColor('#2787D9')
            .justifyContent(FlexAlign.Center)
          }
        }
        .backgroundColor('#F0FAFF')
      }
      .height('20%')
      .width(this.columnWidth)
      Button('Change column width')
        .onClick(()=>{
          if (this.columnWidth == 180) {
            this.columnWidth = 320;
          } else {
            this.columnWidth = 180;
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

This example demonstrates how to customize breakpoint thresholds via [breakpointConfig](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md#breakpointconfig) to define various wide and narrow layout sizes, enabling more refined layout control.
The ContainerReader component and the breakpointConfig API are added since API version 26.0.0.

```TypeScript
// xxx.ets
import { ContainerReader, Size } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State containerSize: Size = { width: 0, height: 0 };
  @State widthBp: WidthBreakpoint = WidthBreakpoint.WIDTH_XS;
  @State heightBp: HeightBreakpoint = HeightBreakpoint.HEIGHT_SM;
  @State columnWidth: number = 180

  build() {
    Column({space: 10}) {
      Column({space: 10}) {
        ContainerReader({
          size: this.containerSize!!,
          widthBreakpoint: this.widthBp!!,
          heightBreakpoint: this.heightBp!!
        }) {
          if (this.widthBp === WidthBreakpoint.WIDTH_XS || this.widthBp === WidthBreakpoint.WIDTH_SM) {
            Column({space: 10}) {
              Text('Narrow screen layout')
                .fontSize(16)
              Text(`Width breakpoint: ${this.widthBp}`)
            }
            .width('100%')
            .height('100%')
            .backgroundColor('#D5D5D5')
            .justifyContent(FlexAlign.Center)
          } else {
            Row({space: 10}) {
              Text('Wide screen layout')
                .fontSize(16)
              Text(`Width breakpoint: ${this.widthBp}`)
            }
            .width('100%')
            .height('100%')
            .backgroundColor('#2787D9')
            .justifyContent(FlexAlign.Center)
          }
        }
        .height(100)
        .width('100%')
        .backgroundColor('#F0FAFF')
        .breakpointConfig({ width: [100, 200, 400, 500], height: [0.8, 1.2] })
      }
      .height('20%')
      .width(this.columnWidth)

      Button('Change column width')
        .onClick(()=>{
          if (this.columnWidth == 180) {
            this.columnWidth = 320;
          } else {
            this.columnWidth = 180;
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

This example demonstrates how to dynamically adjust the number of columns based on the width breakpoint obtained from ContainerReader, enabling adaptive layouts across multiple devices with varying column counts for different breakpoints.
The ContainerReader component is added since API version 26.0.0.

```TypeScript
// xxx.ets
import { ContainerReader, Size } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State containerSize: Size = { width: 0, height: 0 };
  @State widthBp: WidthBreakpoint = WidthBreakpoint.WIDTH_XS;
  @State columnWidth: number = 180

  build() {
    Column({space: 10}) {
      Column({space: 10}) {
        ContainerReader({
          size: this.containerSize!!,
          widthBreakpoint: this.widthBp!!
        }) {
          Row({ space: 2 }) {
            if (this.widthBp === WidthBreakpoint.WIDTH_XS || this.widthBp === WidthBreakpoint.WIDTH_SM) {
              Column() {
                Text(`Column 1`)
                  .fontColor(Color.White)
              }
              .width('100%')
              .height(60)
              .backgroundColor('#D5D5D5')
              .justifyContent(FlexAlign.Center)
              .borderRadius(8)
              .layoutWeight(1)
            } else {
              Column() {
                Text(`Column 1`)
                  .fontColor(Color.White)
              }
              .width('100%')
              .height(60)
              .backgroundColor('#D5D5D5')
              .justifyContent(FlexAlign.Center)
              .borderRadius(8)
              .layoutWeight(1)
              Column() {
                Text(`Column 2`)
                  .fontColor(Color.White)
              }
              .width('100%')
              .height(60)
              .backgroundColor('#707070')
              .justifyContent(FlexAlign.Center)
              .borderRadius(8)
              .layoutWeight(1)
            }
          }
          .width('100%')
          .height('100%')
        }
        .breakpointConfig({ width: [100, 200, 400, 500] })
        .backgroundColor('#F0FAFF')
      }
      .height('20%')
      .width(this.columnWidth)

      Button('Change column width')
        .onClick(()=>{
          if (this.columnWidth == 180) {
            this.columnWidth = 320;
          } else {
            this.columnWidth = 180;
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
