# @ohos.arkui.advanced.ArcButton(Defines the arc button component)

## 导入模块

```TypeScript
import { ArcButton, ArcButtonOptions, ArcButtonProgressConfig, ArcButtonPosition, ArcButtonStyleMode, ArcButtonStatus } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ArcButtonOptions](arkts-arkui-arkui-advanced-arcbutton-arcbuttonoptions-c.md) | 定义ArcButton的默认样式或自定义样式参数。 |
| [ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md) | ArcButton内进度条的参数配置。 |

### 结构体

| 名称 | 说明 |
| --- | --- |
| [ArcButton](arkts-arkui-arkui-advanced-arcbutton-arcbutton-s.md) | 弧形按钮组件提供强调、普通等样式按钮，推荐用于圆形屏幕的设备。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [CommonArcButtonOptions](arkts-arkui-arkui-advanced-arcbutton-commonarcbuttonoptions-i.md) | ArcButton的默认样式或自定义样式参数。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ArcButtonPosition](arkts-arkui-arkui-advanced-arcbutton-arcbuttonposition-e.md) | 定义ArcButton可设置的弧形按钮的类型。 |
| [ArcButtonStatus](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstatus-e.md) | 定义ArcButton可设置的弧形按钮状态。 |
| [ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md) | 定义ArcButton可设置弧形按钮样式模式。 |

## 示例

该示例推荐在Wearable设备下运行以获得最佳显示效果，同时支持在其他设备上运行。若要在Wearable设备上运行，需在src/main目录下的工程配置文件[module.json5](../../../quick-start/module-configuration-file.md)中[deviceTypes标签](../../../quick-start/module-configuration-file.md#devicetypes标签)内配置wearable。

```TypeScript
// module.json5
{
  "module": {
    // ...
    "deviceTypes": [
      "wearable",
      "phone"
    ]
    // ...
  }
}
```

```TypeScript
// xxx.ets
import {
  LengthMetrics,
  LengthUnit,
  ArcButton,
  ArcButtonOptions,
  ArcButtonStatus,
  ArcButtonStyleMode,
  ArcButtonPosition,
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local topOptions: ArcButtonOptions = new ArcButtonOptions({});
  @Local bottomOptions: ArcButtonOptions = new ArcButtonOptions({});

  aboutToAppear() {
    this.topOptions = new ArcButtonOptions({
      label: 'ButtonTop',
      status: ArcButtonStatus.NORMAL,
      position: ArcButtonPosition.TOP_EDGE,
      styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true
    })

    this.bottomOptions = new ArcButtonOptions({
      label: 'ButtonBottom',
      styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      onClick: () => {
        console.info('click from ArcButton.');
      }
    })
  }

  build() {
    Stack() {
      Stack() {
        Circle({ width: 233, height: 233 })
          .strokeWidth(0.1)
          .fill(Color.White)

        Column() {
          ArcButton({ options: this.topOptions })
          Blank()
          ArcButton({ options: this.bottomOptions })

        }.width('100%')
        .height('100%')
      }.width(233)
      .height(233)
    }.width('100%')
    .height('100%')
    .alignContent(Alignment.Center)
    .backgroundColor(Color.Gray)
  }
}
```

```TypeScript
// xxx.ets
import {
  LengthMetrics,
  LengthUnit,
  ArcButton,
  ArcButtonOptions,
  ArcButtonStatus,
  ArcButtonStyleMode,
  ArcButtonPosition,
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local topOptions: ArcButtonOptions = new ArcButtonOptions({});
  @Local bottomOptions: ArcButtonOptions = new ArcButtonOptions({});

  aboutToAppear() {
    this.topOptions = new ArcButtonOptions({
      label: 'Add',
      styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
      position: ArcButtonPosition.TOP_EDGE,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      onClick: () => {
        if (this.bottomOptions.progressConfig && this.bottomOptions.progressConfig.value < 100) {
          this.bottomOptions.progressConfig.value = this.bottomOptions.progressConfig.value + 5;
          this.bottomOptions.label = this.bottomOptions.progressConfig.value + '%';
        }
      }
    })

    this.bottomOptions = new ArcButtonOptions({
      label: '0%',
      status: ArcButtonStatus.NORMAL,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      progressConfig: {value:0, total:100}
    })
  }

  build() {
    Stack() {
      Stack() {
        Circle({ width: 233, height: 233 })
          .strokeWidth(0.1)
          .fill(Color.White)

        Column() {
          ArcButton({ options: this.topOptions })
          Blank()
          ArcButton({ options: this.bottomOptions })

        }.width('100%')
        .height('100%')
      }.width(233)
      .height(233)
    }.width('100%')
    .height('100%')
    .alignContent(Alignment.Center)
    .backgroundColor(Color.Gray)
  }
}
```
