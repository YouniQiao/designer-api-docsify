# @ohos.arkui.WithEnv(Define the WithEnv component that allows setting environment properties for child components.)

## Modules to Import

```TypeScript
import { WithEnv, WithEnvAttribute} from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [WithEnvAttribute](arkts-arkui-arkui-withenv-withenvattribute-c.md) | Define the WithEnv attribute functions. |

### Types

| Name | Description |
| --- | --- |
| [WithEnvInterface](arkts-arkui-withenvinterface-t.md) | Define the WithEnv component's type. |

### Constants

| Name | Description |
| --- | --- |
| [WithEnv](arkts-arkui-arkui-withenv-con.md) | Define the WithEnv component that allows setting environment properties for child components. |
| [WithEnvInstance](arkts-arkui-arkui-withenv-con.md#withenvinstance) | Define WithEnv Logic Component Instance. |

## Examples

This example uses  to set a local font scale for components within the scope.
Since API version 26.0.0, the env attribute and the key WritableEnvKey.FONT_SCALE are added.

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
        Button('Zoom out 0.5x')
          .onClick(() => {
            this.fontScale = 0.5;
          })
        Button('Normal 1.0x')
          .onClick(() => {
            this.fontScale = 1.0;
          })
        Button('Zoom in 1.5x')
          .onClick(() => {
            this.fontScale = 1.5;
          })
      }

      WithEnv() {
        Column({ space: 8 }) {
          Text('Text within the current font scale scope')
            .fontSize(16)
          Text('This text is also affected by the WithEnv font scaling')
            .fontSize(14)
            .fontColor('#99182431')
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
      }
      .env(WritableEnvKey.FONT_SCALE, this.fontScale) // Set the local font scale ratio.
    }
    .padding(12)
    .width('100%')
  }
}
```

This example uses  to set the local layout direction for components within the scope.
Since API version 26.0.0, the env attribute and the key WritableEnvKey.DIRECTION are added.

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
      .env(WritableEnvKey.DIRECTION, this.directionValue) // Set local layout direction.

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
