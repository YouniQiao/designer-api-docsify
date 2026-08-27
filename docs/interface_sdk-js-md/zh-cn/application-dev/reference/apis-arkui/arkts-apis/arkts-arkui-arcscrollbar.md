# @ohos.arkui.ArcScrollBar

## 导入模块

```TypeScript
import { ArcScrollBar, ArcScrollBarAttribute } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ArcScrollBarAttribute](arkts-arkui-arkui-arcscrollbar-arcscrollbarattribute-c.md) |  |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ArcScrollBarInterface](arkts-arkui-arkui-arcscrollbar-arcscrollbarinterface-i.md) | 弧形滚动条组件ArcScrollBar，适用于圆形屏幕等需要弧形滚动条的场景，用于配合可滚动组件使用，如ArcList、List、Grid、Scroll、WaterFlow。 |
| [ArcScrollBarOptions](arkts-arkui-arkui-arcscrollbar-arcscrollbaroptions-i.md) | ArcScrollBar的构造函数参数。 |

### 常量

| 名称 | 说明 |
| --- | --- |
| [ArcScrollBar](arkts-arkui-arkui-arcscrollbar-con.md) | 弧形滚动条组件ArcScrollBar，适用于圆形屏幕等需要弧形滚动条的场景，用于配合可滚动组件使用，如ArcList、List、Grid、Scroll、WaterFlow。 |
| [ArcScrollBarInstance](arkts-arkui-arkui-arcscrollbar-con.md#arcscrollbarinstance) | 定义ArcScrollBar组件实例。 |

## 示例

该示例通过ArcScrollBar与[Scroll](ts-container-scroll.md)组件联动，设置了弧形外置滚动条。

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
