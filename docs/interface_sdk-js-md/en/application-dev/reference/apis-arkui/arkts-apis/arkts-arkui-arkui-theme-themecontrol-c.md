# ThemeControl

Class ThemeControl provides the Theme management for whole Ability and pages.

**Since:** 12

<!--Device-unnamed-export declare class ThemeControl--><!--Device-unnamed-export declare class ThemeControl-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Colors, CustomColors, Theme, ThemeControl, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```

## setDefaultTheme

```TypeScript
static setDefaultTheme(theme: CustomTheme): void
```

Sets the default Theme:

- for whole Ability when invoked from the Ability level code. - for the ArkUI page and for later opened pages when invoked at the ArkUI page level.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme): void--><!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | [CustomTheme](../../apis-default/arkts-apis/arkts-arkui-theme-customtheme-i.md) | Yes |  |

**Examples**

```TypeScript
import { CustomTheme, CustomColors, ThemeControl } from '@kit.ArkUI';
// Custom theme color
class BlueColors implements CustomColors {
  fontPrimary = "#FF707070";
  backgroundPrimary = "#FF2787D9";
  brand = "#FFEEAAFF"; // Brand color.
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}
// Create an instance.
const BlueColorsTheme = new PageCustomTheme(new BlueColors());
// Call ThemeControl.setDefaultTheme before page build to set the default application style to BlueColorsTheme.
ThemeControl.setDefaultTheme(BlueColorsTheme);

@Entry
@Component
struct Index {

  build() {
    Row() {
      Column() {
        // Apply fontPrimary to the text color.
        Text('This is a piece of text.')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin('5%')
        // Apply backgroundPrimary to the QR code background color.
        QRCode('Hello')
          .width(100)
          .height(100)
        // Apply brand to the input box cursor color.
        TextInput({placeholder: 'input your word...'})
          .width('80%')
          .height(40)
          .margin(20)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

