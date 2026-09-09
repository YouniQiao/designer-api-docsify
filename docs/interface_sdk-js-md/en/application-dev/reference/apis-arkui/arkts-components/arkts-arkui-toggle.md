# Toggle

The **Toggle** component provides a clickable element of the checkbox, button, or switch type.

> **NOTE**

## Child Components

This component can contain child components only when **ToggleType** is set to **Button**.

## Toggle

```TypeScript
Toggle(options: ToggleOptions)
```

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-arkui-toggleoptions-i.md) | Yes | Options of the toggle. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [SwitchStyle](arkts-arkui-switchstyle-i.md) | Sets the style for the component of the **Switch** type. |
| [ToggleConfiguration](arkts-arkui-toggleconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. This API inherits from [CommonConfiguration](arkts-arkui-commonconfiguration-i.md). |
| [ToggleOptions](arkts-arkui-toggleoptions-i.md) | Options of the toggle. |

### Enums

| Name | Description |
| --- | --- |
| [ToggleType](arkts-arkui-toggletype-e.md) | Enumerates toggle types. |

## Examples

This example demonstrates how to configure the style for different types of toggles (checkbox, switch, and button) using ToggleType.

```TypeScript
// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Checkbox, isOn: false })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Checkbox, isOn: true })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Button, isOn: false }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })

        Toggle({ type: ToggleType.Button, isOn: true }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })
      }
    }.width('100%').padding(24)
  }
}
```

This example implements a toggle of the Switch type with custom settings, including the radius and color of the circular slider, background color in the off state, and radius of the slider track border corners.

```TypeScript
// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .selectedColor('#007DFF')
          .switchStyle({
            pointRadius: 15,
            trackBorderRadius: 10,
            pointColor: '#D2B48C',
            unselectedColor: Color.Pink })
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }
    }.width('100%').padding(24)
  }
}
```

This example shows how to implement a custom toggle style. The toggle button switches the background color. Clicking the blue circle changes the background to blue. Clicking the yellow circle changes it to yellow.

```TypeScript
// xxx.ets
// Custom Switch style modifier that implements the ContentModifier API to customize the Toggle content area.
class MySwitchStyle implements ContentModifier<ToggleConfiguration> {
  // Background color when the switch is on.
  selectedColor: Color = Color.White;
  // Text displayed on the button.
  lamp: string = 'string';

  constructor(selectedColor: Color, lamp: string) {
    this.selectedColor = selectedColor;
    this.lamp = lamp;
  }

  applyContent(): WrappedBuilder<[ToggleConfiguration]> {
    return wrapBuilder(buildSwitch);
  }
}

@Builder
function buildSwitch(config: ToggleConfiguration) {
  Column({ space: 50 }) {
    Circle({ width: 150, height: 150 })
      .fill(config.isOn ? (config.contentModifier as MySwitchStyle).selectedColor : Color.Blue)
    Row() {
      Button('Blue ' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(false);
        })
      Button('Yellow ' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
        .onClick(() => {
          config.triggerChange(true);
        })
    }
  }
}

@Entry
@Component
struct Index {
  build() {
    Column({ space: 50 }) {
      // Use the custom style modifier to customize the Toggle content, and listen for state changes through onChange.
      Toggle({ type: ToggleType.Switch })
        .enabled(true)
        .contentModifier(new MySwitchStyle(Color.Yellow, 'light'))
        .onChange((isOn: boolean) => {
          console.info('Switch Log:' + isOn);
        })
    }.height('100%').width('100%')
  }
}
```

This example shows the effect comparison of the Switch type of the Toggle component before and after the immersive light effect is enabled, including the effects of not setting the system material, setting undefined, setting the system material, and setting the system material together with [switchPointColor](arkts-arkui-toggle-attribute.md#switchpointcolor) to set the point light source color. The example uses the universal attribute [systemMaterial](ts-universal-attributes-image-effect.md#systemmaterial) API to implement the immersive light effect.
The immersive light effect of the component is adaptively adjusted based on the device computing power and the immersive light effect set by the user in the system, and no additional adaptation is required by developers.
Since API version 26.0.0, the systemMaterial attribute is added.
> NOTE
> 
> The actual display effect of the system material is related to the computing power tier of the device. The same code produces different display effects on devices of different computing power tiers, and a simplified material effect is displayed on low-computing-power devices. The computing power tier is automatically divided and managed by the system based on the hardware capabilities of the device. Applications do not need to be aware of it or perform additional settings. The system automatically adapts the material display effect based on the computing power tier of the current device.

```TypeScript
import { uiMaterial } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct ToggleMaterialTest {
  build() {
    Column({ space: 10 }) {
      // Do not set the system material API, and there is no immersive light effect.
      Toggle({ type: ToggleType.Switch, isOn: true })

      // Set systemMaterial to undefined to restore the effect without immersive light.
      Toggle({ type: ToggleType.Switch, isOn: true })
        .systemMaterial(undefined)

      // Set the system material to enable the immersive light effect (the systemMaterial parameter is arbitrary and serves only as the system material switch; the component-side fixed parameters are ultimately used), with a white point light source by default (the color is the default value of switchPointColor).
      Toggle({ type: ToggleType.Switch, isOn: true })
        .systemMaterial(new uiMaterial.Material())

      // Set the system material to enable the immersive light effect (the systemMaterial parameter is arbitrary and serves only as the system material switch; the component-side fixed parameters are ultimately used), with the point light color following the switchPointColor setting.
      Toggle({ type: ToggleType.Switch, isOn: true })
        .systemMaterial(new uiMaterial.Material())
        .switchPointColor(Color.Red)
    }
    .width('100%')
  }
}
```
