# @ohos.arkui.advanced.ArcButton(Defines the arc button component)

## Modules to Import

```TypeScript
import { ArcButton, ArcButtonOptions, ArcButtonProgressConfig, ArcButtonPosition, ArcButtonStyleMode, ArcButtonStatus } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ArcButtonOptions](arkts-arkui-arkui-advanced-arcbutton-arcbuttonoptions-c.md) | Defines the default or custom style parameters for the **ArcButton** component. |
| [ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md) | Defines the progress indicator configuration options of the **ArcButton** component. |

### Structs

| Name | Description |
| --- | --- |
| [ArcButton](arkts-arkui-arkui-advanced-arcbutton-arcbutton-s.md) | The **ArcButton** component offers various button styles, such as emphasized, normal, and warning. It is recommended for devices with circular screens. |

### Interfaces

| Name | Description |
| --- | --- |
| [CommonArcButtonOptions](arkts-arkui-arkui-advanced-arcbutton-commonarcbuttonoptions-i.md) | Defines the default or custom style parameters for the **ArcButton** component. |

### Enums

| Name | Description |
| --- | --- |
| [ArcButtonPosition](arkts-arkui-arkui-advanced-arcbutton-arcbuttonposition-e.md) | Enumerates the types of arc buttons that can be set for **ArcButton**. |
| [ArcButtonStatus](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstatus-e.md) | Enumerates the states that can be set for **ArcButton**. |
| [ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md) | Enumerates the style modes that can be set for **ArcButton**. |

## Examples

This example is recommended to run on a wearable device for optimal display effects and is also supported on other devices. To run the example on a wearable device, configure wearable in the [deviceTypes](../../../quick-start/module-configuration-file.md#devicetypes) tag of the [module.json5](../../../quick-start/module-configuration-file.md) configuration file in the src/main directory.

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
}  from '@kit.ArkUI';

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

This example is recommended to run on a wearable device for optimal display effects and is also supported on other devices. To run the example on a wearable device, configure wearable in the [deviceTypes](../../../quick-start/module-configuration-file.md#devicetypes) tag of the [module.json5] configuration file (../../../quick-start/module-configuration-file.md) in the src/main directory.

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
}  from '@kit.ArkUI';

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
        if(this.bottomOptions.progressConfig && this.bottomOptions.progressConfig.value < 100) {
          this.bottomOptions.progressConfig.value = this.bottomOptions.progressConfig.value + 5
          this.bottomOptions.label = this.bottomOptions.progressConfig.value + "%"
        }
      }
    })

    this.bottomOptions = new ArcButtonOptions({
      label: '0%',
      status: ArcButtonStatus.NORMAL,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      progressConfig: {value:0, total:100},
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
