# @ohos.arkui.ArcScrollBar

## Modules to Import

```TypeScript
import { ArcScrollBar, ArcScrollBarAttribute } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ArcScrollBarAttribute](arkts-arkui-arkui-arcscrollbar-arcscrollbarattribute-c.md) | Defines the arc scroll bar attribute functions. |

### Interfaces

| Name | Description |
| --- | --- |
| [ArcScrollBarInterface](arkts-arkui-arkui-arcscrollbar-arcscrollbarinterface-i.md) | The **ArcScrollBar** component is designed to be used together with scrollable components such as ArcList, List, Grid, Scroll, and WaterFlow. |
| [ArcScrollBarOptions](arkts-arkui-arkui-arcscrollbar-arcscrollbaroptions-i.md) | Represents the parameters used to construct an **ArcScrollBar** component. |

### Constants

| Name | Description |
| --- | --- |
| [ArcScrollBar](arkts-arkui-arkui-arcscrollbar-con.md) | The **ArcScrollBar** component is designed to be used together with scrollable components such as ArcList, List, Grid, Scroll, and WaterFlow. |
| [ArcScrollBarInstance](arkts-arkui-arkui-arcscrollbar-con.md#arcscrollbarinstance) | Defines ArcScrollBar Component instance. |

## Examples

This example demonstrates how to synchronize ArcScrollBar with the [Scroll](ts-container-scroll.md) component to implement an arc scrollbar.

```TypeScript
import { ArcScrollBar } from '@kit.ArkUI';

@Entry
@Component
struct ArcScrollBarExample {
  private scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Scroll(this.scroller) {
        Flex({ direction: FlexDirection.Column }) {
          ForEach(this.arr, (item: number) => {
            Row() {
              Text(item.toString())
                .width('80%')
                .height(60)
                .backgroundColor('#3366CC')
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 5 })
            }
          }, (item: number) => item.toString())
        }.margin({ right: 15 })
      }
      .width('90%')
      .scrollBar(BarState.Off)

      ArcScrollBar({ scroller: this.scroller, state: BarState.Auto })
    }
    .width('100%')
    .height('100%')
  }
}
```
