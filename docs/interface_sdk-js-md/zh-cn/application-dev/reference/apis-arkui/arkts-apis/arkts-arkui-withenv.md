# @ohos.arkui.WithEnv(定义WithEnv组件，允许为子组件设置环境属性。)

## 导入模块

```TypeScript
import { WithEnv, WithEnvAttribute} from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [WithEnvAttribute](arkts-arkui-arkui-withenv-withenvattribute-c.md) | 定义WithEnv组件的属性功能。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [WithEnvInterface](arkts-arkui-withenvinterface-t.md) | 定义WithEnv组件的类型。 |

### 常量

| 名称 | 说明 |
| --- | --- |
| [WithEnv](arkts-arkui-arkui-withenv-con.md) | WithEnv组件用于为子组件树设置局部环境变量作用域。开发者可以通过该组件为后代组件提供自定义环境变量，或设置系统环境变量。 |
| [WithEnvInstance](arkts-arkui-arkui-withenv-con.md#withenvinstance) | 定义WithEnv逻辑组件实例。 |

## 示例

该示例通过为作用域内组件设置局部字体缩放比例。
从API版本26.0.0开始，新增env属性和键值WritableEnvKey.FONT_SCALE。

```TypeScript
// xxx.ets
import { WithEnv } from '@kit.ArkUI';
@Entry
@Component
struct WithEnvExample1 {
  @State fontScale: number = 1.0;

  build() {
    Column({ space: 12 }) {
      Row({ space: 8 }) {
        Button('缩小 0.5x')
          .onClick(() => {
            this.fontScale = 0.5;
          })
        Button('正常 1.0x')
          .onClick(() => {
            this.fontScale = 1.0;
          })
        Button('放大 1.5x')
          .onClick(() => {
            this.fontScale = 1.5;
          })
      }

      WithEnv() {
        Column({ space: 8 }) {
          Text('当前字体缩放作用域内的文本')
            .fontSize(16)
          Text('该文本同样受 WithEnv 字体缩放影响')
            .fontSize(14)
            .fontColor('#99182431')
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
      }
      .env(WritableEnvKey.FONT_SCALE, this.fontScale) // 设置局部字体缩放比例
    }
    .padding(12)
    .width('100%')
  }
}
```

该示例通过为作用域内组件设置局部布局方向。
从API版本26.0.0开始，新增env属性和键值WritableEnvKey.DIRECTION。

```TypeScript
// xxx.ets
import { WithEnv } from '@kit.ArkUI';

@Entry
@Component
struct WithEnvExample2 {
  @State directionValue: Direction = Direction.Ltr;

  build() {
    Column({ space: 12 }) {
      Row({ space: 10 }) {
        Column().backgroundColor('#F0FAFF').width(60).height('100%')
        Column().backgroundColor('#2787D9').width(60).height('100%')
        Column().backgroundColor('#004AAF').width(60).height('100%')

      }.backgroundColor('#D5D5D5').width(200).height(50)

      WithEnv() {
        Row({ space: 10 }) {
          Column().backgroundColor('#F0FAFF').width(60).height('100%')
          Column().backgroundColor('#2787D9').width(60).height('100%')
          Column().backgroundColor('#004AAF').width(60).height('100%')

        }.backgroundColor('#D5D5D5').width(200).height(50)
      }
      .env(WritableEnvKey.DIRECTION, this.directionValue) // 设置局部布局方向

      Button('change direction').onClick(() => {
        if (this.directionValue === Direction.Ltr) {
          this.directionValue = Direction.Rtl;
        } else {
          this.directionValue = Direction.Ltr;
        }
      })
    }
    .width('80%')
    .height('30%')
  }
}
```
