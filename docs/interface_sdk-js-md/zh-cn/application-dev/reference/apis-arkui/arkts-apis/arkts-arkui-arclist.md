# @ohos.arkui.ArcList

## 导入模块

```TypeScript
import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) | 除支持通用属性外，还支持以下属性（不支持[滚动组件通用属性](../arkts-components/arkts-arkui-scrollablecommonmethod-c.md)）： |
| [ArcListItemAttribute](arkts-arkui-arkui-arclist-arclistitemattribute-c.md) | 除支持通用属性外，还支持以下属性： |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ArcListInterface](arkts-arkui-arkui-arclist-arclistinterface-i.md) | 弧形列表由沿弧形排列的一系列列表项组成，适用于圆形屏幕设备。适合连续、多行呈现同类数据，例如图片和文本。 |
| [ArcListItemInterface](arkts-arkui-arkui-arclist-arclistiteminterface-i.md) | 用于展示弧形列表的子组件，必须配合ArcList使用。 |
| [ArkListOptions](arkts-arkui-arkui-arclist-arklistoptions-i.md) | 包含创建ArcList组件的基础参数。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ArcScrollIndexHandler](arkts-arkui-arcscrollindexhandler-t.md) | 有子组件划入或划出ArcList显示区域时触发的回调。 |

### 常量

| 名称 | 说明 |
| --- | --- |
| [ArcList](arkts-arkui-arkui-arclist-con.md) | 弧形列表由沿弧形排列的一系列列表项组成，适用于圆形屏幕设备。适合连续、多行呈现同类数据，例如图片和文本。 |
| [ArcListInstance](arkts-arkui-arkui-arclist-con.md#arclistinstance) | 定义ArcList组件实例。 |
| [ArcListItem](arkts-arkui-arkui-arclist-con.md#arclistitem) | 用于展示弧形列表的子组件，必须配合ArcList使用。 |
| [ArcListItemInstance](arkts-arkui-arkui-arclist-con.md#arclistiteminstance) | 定义ArcListItem组件实例。 |

## 示例

该示例展示了子项关闭自动缩放和开启自动缩放后的对比效果。

```TypeScript
// xxx.ets
import { LengthMetrics, CircleShape } from '@kit.ArkUI';
// 从API version 22开始，无需手动导入ArcListAttribute和ArcListItemAttribute。具体请参考ArcList、ArcListItem的导入模块说明。
import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';

@Entry
@Component
struct ArcListItemExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  private watchSize: string = '466px'; // 手表默认宽高：466*466
  private itemSize: string = '414px'; // item宽度

  @Builder
  buildList() {
    Stack() {
      Column() {
      }
      .width(this.watchSize)
      .height(this.watchSize)
      .clipShape(new CircleShape({ width: '100%', height: '100%' }))
      .backgroundColor(0x707070)

      ArcList({ initialIndex: 3}) {
        ForEach(this.arr, (item: number) => {
          ArcListItem() {
            Button('' + item, { type: ButtonType.Capsule })
              .width(this.itemSize)
              .height('70px')
              .fontSize('40px')
              .backgroundColor(0x17A98D)
          }
          .autoScale(item % 3 == 0 || item % 5 == 0)
        }, (item: number) => item.toString())
      }
      .space(LengthMetrics.px(10))
      .borderRadius(this.watchSize)
    }
    .width(this.watchSize)
    .height(this.watchSize)
  }

  build() {
    Column() {
      this.buildList();
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

该示例增加了ArcList支持标题栏设置的效果，子项自动缩放显示。

```TypeScript
// xxx.ets
import { ComponentContent, LengthMetrics, UIContext, CircleShape } from '@kit.ArkUI';
// 从API version 22开始，无需手动导入ArcListAttribute和ArcListItemAttribute。具体请参考ArcList、ArcListItem的导入模块说明。
import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';

@Builder
function buildText() {
  Column() {
    Text('header')
      .fontSize('60px')
      .fontWeight(FontWeight.Bold)
      .fontColor(Color.Black)
  }.margin(0)
}

@Entry
@Component
struct Index {
  @State private numItems: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  private watchSize: string = '466px'; // Wearable默认宽高：466*466
  private listSize: string = '414px'; // item宽度

  context: UIContext = this.getUIContext();
  headerContent: ComponentContent<Object> = new ComponentContent(this.context, wrapBuilder(buildText));

  @Builder
  buildList() {
    Stack() {
      Column() {
      }
      .justifyContent(FlexAlign.Center)
      .width(this.watchSize)
      .height(this.watchSize)
      .clipShape(new CircleShape({ width: '100%', height: '100%' }))
      .backgroundColor(Color.White)

      ArcList({ initialIndex: 0, header: this.headerContent }) {
        ForEach(this.numItems, (item: number, index: number) => {
          ArcListItem() {
            Button('' + item, { type: ButtonType.Capsule })
              .width(this.listSize)
              .height('100px')
              .fontSize('40px')
              .focusable(true)
              .focusOnTouch(true)
              .backgroundColor(0x17A98D)
          }.align(Alignment.Center)
        }, (item: number, index: number) => (item + index).toString())
      }
      .space(LengthMetrics.px(10))
      .borderRadius(this.watchSize)
      .focusable(true)
      .focusOnTouch(true)
      .defaultFocus(true)
    }
    .align(Alignment.Center)
    .width(this.watchSize)
    .height(this.watchSize)
    .border({color: Color.Black, width: 1})
    .borderRadius(this.watchSize)
  }

  build() {
    Column() {
      this.buildList()
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```
