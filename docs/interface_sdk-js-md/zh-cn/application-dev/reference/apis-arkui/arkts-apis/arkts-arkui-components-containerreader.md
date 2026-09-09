# @ohos.arkui.components.ContainerReader

## 导入模块

```TypeScript
import { ContainerReader, ContainerReaderAttribute, BreakpointOptions } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ContainerReaderAttribute](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md) | 除支持[通用属性](../arkts-components/arkts-arkui-commonmethod-c.md)外，还支持以下属性： |

### 接口

| 名称 | 说明 |
| --- | --- |
| [BreakpointOptions](arkts-arkui-arkui-components-containerreader-breakpointoptions-i.md) | 定义断点配置选项，用于指定容器尺寸分析的阈值参数。 |
| [ContainerReaderInfo](arkts-arkui-arkui-components-containerreader-containerreaderinfo-i.md) | 定义ContainerReader组件的配置选项，用于指定容器尺寸读取和断点值获取的参数，不能通过此参数改变组件尺寸和断点值。 |
| [ContainerReaderInterface](arkts-arkui-arkui-components-containerreader-containerreaderinterface-i.md) | 定义ContainerReader组件。用于在动态场景下基于尺寸断点读取和分析容器布局信息。提供容器尺寸分析和断点检测能力。 |

### 常量

| 名称 | 说明 |
| --- | --- |
| [ContainerReader](arkts-arkui-arkui-components-containerreader-con.md) | ContainerReader是容器断点组件，用于在动态场景下根据容器尺寸获取断点信息并进行响应式布局。该组件通过[双向绑定](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)实时返回容器的尺寸和断点，使开发者能够基于容器大小进行差异化的组件创建和布局。 |
| [ContainerReaderInstance](arkts-arkui-arkui-components-containerreader-con.md#containerreaderinstance) | 定义ContainerReader组件实例。提供对ContainerReader组件方法的访问，用于容器尺寸分析和断点检测。 |

## 示例

该示例展示了[ContainerReader](#containerreader-1)组件，如何通过双向绑定获取容器尺寸和断点信息，并根据宽度断点切换布局方向。
从API版本26.0.0开始，新增ContainerReader。

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
          size: this.containerSize!!, // 和this.containerSize变量绑定，ContainerReader尺寸变化时this.containerSize自动更新。
          widthBreakpoint: this.widthBp!!,
          heightBreakpoint: this.heightBp!!
        }) {
          // 根据宽度断点切换布局方向
          if (this.widthBp === WidthBreakpoint.WIDTH_XS) {
            Column({space: 20}) {
              Text('竖向布局')
              Text(`Column`)
            }
            .width('100%')
            .height('100%')
            .backgroundColor('#D5D5D5')
            .justifyContent(FlexAlign.Center)
          } else {
            Row({space: 20}) {
              Text('横向布局')
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
      Button('改变Column宽度')
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

该示例展示了如何通过[breakpointConfig](arkts-arkui-arkui-components-containerreader-containerreaderattribute-c.md#breakpointconfig)自定义断点阈值，定义不同的宽窄布局尺寸要求，实现更精细化的布局控制。
从API版本26.0.0开始，新增ContainerReader与breakpointConfig。

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
              Text('窄屏布局')
                .fontSize(16)
              Text(`宽度断点: ${this.widthBp}`)
            }
            .width('100%')
            .height('100%')
            .backgroundColor('#D5D5D5')
            .justifyContent(FlexAlign.Center)
          } else {
            Row({space: 10}) {
              Text('宽屏布局')
                .fontSize(16)
              Text(`宽度断点: ${this.widthBp}`)
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

      Button('改变Column宽度')
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

该示例展示了如何根据ContainerReader得到的宽度断点动态调整列数，实现多设备自适应布局。根据宽度断点不同设置不同的列数。
从API版本26.0.0开始，新增ContainerReader。

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
                Text(`第 1 个 Column`)
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
                Text(`第 1 个 Column`)
                  .fontColor(Color.White)
              }
              .width('100%')
              .height(60)
              .backgroundColor('#D5D5D5')
              .justifyContent(FlexAlign.Center)
              .borderRadius(8)
              .layoutWeight(1)
              Column() {
                Text(`第 2 个 Column`)
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

      Button('改变Column宽度')
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
