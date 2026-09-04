# @ohos.arkui.advanced.ChipV2

## Modules to Import

```TypeScript
import { ChipV2Size, ChipV2AccessibilitySelectedType, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2SuffixImageIconConfig, ChipV2SuffixImageIcon, ChipV2Icon, ChipV2PrefixImageIconConfig, ChipV2PrefixImageIcon, ChipV2AccessibilityConfig, ChipV2Accessibility, ChipV2CloseConfig, ChipV2CloseIcon, ChipV2SymbolIconConfig, ChipV2SymbolIcon, ChipV2PrefixSymbolIconConfig, ChipV2PrefixSymbolIcon, ChipV2SuffixSymbolIconConfig, ChipV2SuffixSymbolIcon, ChipV2LabelMarginConfig, ChipV2LocalizedLabelMarginConfig, ChipV2LabelConfig, ChipV2Label, IChipV2OptionsConfig, ChipV2Options, ChipV2 } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ChipV2Accessibility](arkts-arkui-arkui-advanced-chipv2-chipv2accessibility-c.md) | Defines accessibility. |
| [ChipV2CloseIcon](arkts-arkui-arkui-advanced-chipv2-chipv2closeicon-c.md) | Defines default close icon. |
| [ChipV2Icon](arkts-arkui-arkui-advanced-chipv2-chipv2icon-c.md) | Defines chipV2 icon. |
| [ChipV2ImageIcon](arkts-arkui-arkui-advanced-chipv2-chipv2imageicon-c.md) | ChipV2 icon common option |
| [ChipV2Label](arkts-arkui-arkui-advanced-chipv2-chipv2label-c.md) | Defines chip label class. |
| [ChipV2Options](arkts-arkui-arkui-advanced-chipv2-chipv2options-c.md) | Defines chip options class. |
| [ChipV2PrefixImageIcon](arkts-arkui-arkui-advanced-chipv2-chipv2prefiximageicon-c.md) | Defines prefix icon. |
| [ChipV2PrefixSymbolIcon](arkts-arkui-arkui-advanced-chipv2-chipv2prefixsymbolicon-c.md) | Defines chip prefix symbol icon. |
| [ChipV2SuffixImageIcon](arkts-arkui-arkui-advanced-chipv2-chipv2suffiximageicon-c.md) | Defines suffix icon. |
| [ChipV2SuffixSymbolIcon](arkts-arkui-arkui-advanced-chipv2-chipv2suffixsymbolicon-c.md) | Defines accessibility of suffix symbol. |
| [ChipV2SymbolIcon](arkts-arkui-arkui-advanced-chipv2-chipv2symbolicon-c.md) | Defines chip symbol icon. |

### Structs

| Name | Description |
| --- | --- |
| [ChipV2](arkts-arkui-arkui-advanced-chipv2-chipv2-s.md) | Defines chip component with V2 state management. |

### Interfaces

| Name | Description |
| --- | --- |
| [ChipV2AccessibilityConfig](arkts-arkui-arkui-advanced-chipv2-chipv2accessibilityconfig-i.md) | Defines accessibility config. |
| [ChipV2CloseConfig](arkts-arkui-arkui-advanced-chipv2-chipv2closeconfig-i.md) | Defines config of default close icon. |
| [ChipV2ImageIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2imageiconconfig-i.md) | Defines icon common config. |
| [ChipV2LabelConfig](arkts-arkui-arkui-advanced-chipv2-chipv2labelconfig-i.md) | Defines label config. |
| [ChipV2LabelMarginConfig](arkts-arkui-arkui-advanced-chipv2-chipv2labelmarginconfig-i.md) | Defines label margin. |
| [ChipV2LocalizedLabelMarginConfig](arkts-arkui-arkui-advanced-chipv2-chipv2localizedlabelmarginconfig-i.md) | Defines localized label margin. |
| [ChipV2PrefixImageIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2prefiximageiconconfig-i.md) | Defines prefix icon option. |
| [ChipV2PrefixSymbolIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2prefixsymboliconconfig-i.md) | Defines chip prefix symbol icon config. |
| [ChipV2SuffixImageIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2suffiximageiconconfig-i.md) | Defines suffix icon option. |
| [ChipV2SuffixSymbolIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2suffixsymboliconconfig-i.md) | Defines accessibility config of suffix symbol. |
| [ChipV2SymbolIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2symboliconconfig-i.md) | Defines chip symbol icon config. |
| [IChipV2OptionsConfig](arkts-arkui-arkui-advanced-chipv2-ichipv2optionsconfig-i.md) | Defines ChipV2 options interface. |

### Enums

| Name | Description |
| --- | --- |
| [ChipV2AccessibilitySelectedType](arkts-arkui-arkui-advanced-chipv2-chipv2accessibilityselectedtype-e.md) | Enum for ChipV2AccessibilitySelectedType |
| [ChipV2Size](arkts-arkui-arkui-advanced-chipv2-chipv2size-e.md) | Enum for ChipV2 Size |

## Examples

This example sets custom icons through the prefixIcon and suffixIcon attributes of ChipV2Options.
Since API version 26.0.0, ChipV2Options supports the prefixIcon and suffixIcon attributes.

```TypeScript
import { ChipV2, ChipV2Options, ChipV2Label, ChipV2PrefixImageIcon, ChipV2SuffixImageIcon, LengthMetrics, ColorMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  build() {
    Column({ space: 10 }) {
      ChipV2({
        chipV2Options: new ChipV2Options({
          // Set the prefix icon attribute.
          prefixIcon: new ChipV2PrefixImageIcon({
            // Replace 'app.media.chips' with your actual icon resource.
            src: $r('app.media.chips'),
            size: { width: LengthMetrics.fp(16), height: LengthMetrics.fp(16) },
            fillColor: ColorMetrics.resourceColor(Color.Red)
          }),
          // Set the text attribute.
          label: new ChipV2Label({
            text: 'Chip',
            fontSize: LengthMetrics.fp(12),
            fontColor: ColorMetrics.resourceColor(Color.Blue),
            fontFamily: 'HarmonyOS Sans',
            labelMargin: { left: LengthMetrics.fp(20), right: LengthMetrics.fp(30) }
          }),
          // Set the suffix icon attribute.
          suffixIcon: new ChipV2SuffixImageIcon({
            // Replace 'app.media.close' with your actual icon resource.
            src: $r('app.media.close'),
            size: { width: LengthMetrics.fp(16), height: LengthMetrics.fp(16) },
            fillColor: ColorMetrics.resourceColor(Color.Red)
          }),
          size: { width: LengthMetrics.fp(160), height: LengthMetrics.fp(36) },
          enabled: true,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          borderRadius: LengthMetrics.resource($r('sys.float.ohos_id_corner_radius_button')),
          minFontScale: 0.2,
          maxFontScale: 2,
          padding: {
            start: LengthMetrics.fp(20),
            end: LengthMetrics.fp(20)
          },
          fontSize: LengthMetrics.fp(12)
        })
      })
    }
  }
}
```

This example sets the active state of [ChipV2](arkts-arkui-arkui-advanced-chipv2-chipv2-s.md) through the activated attribute of ChipV2Options.
Since API version 26.0.0, ChipV2Options supports the activated attribute.

```TypeScript
import { ChipV2, ChipV2Options, ChipV2Label, ChipV2PrefixImageIcon, ChipV2CloseIcon, LengthMetrics, ColorMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      ChipV2({
        chipV2Options: new ChipV2Options({
          // Set the prefix icon attribute.
          prefixIcon: new ChipV2PrefixImageIcon({
            // Replace 'app.media.icon' with your actual icon resource.
            src: $r('app.media.chips'),
            size: { width: LengthMetrics.fp(16), height: LengthMetrics.fp(16) },
            fillColor: ColorMetrics.resourceColor(Color.Blue),
            activatedFillColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary'))
          }),
          // Set the text attribute.
          label: new ChipV2Label({
            text: 'Chip',
            fontSize: LengthMetrics.fp(12),
            fontColor: ColorMetrics.resourceColor(Color.Blue),
            activatedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
            fontFamily: 'HarmonyOS Sans',
            labelMargin: { left: LengthMetrics.fp(20), right: LengthMetrics.fp(30) }
          }),
          size: { width: LengthMetrics.fp(160), height: LengthMetrics.fp(36) },
          allowClose: true,
          enabled: true,
          activated: this.isActivated,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          activatedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          borderRadius: LengthMetrics.resource($r('sys.float.ohos_id_corner_radius_button')),
          closeIcon: new ChipV2CloseIcon({
            fontSize: LengthMetrics.fp(12)
          }),
          onClose: () => {
            console.info('chip on close');
          },
          onClicked: () => {
            console.info('chip on clicked');
          }
        })
      })
      // Tap "Change active state" to activate and deactivate ChipV2.
      Button('Change active state')
        .onClick(() => {
          this.isActivated = !this.isActivated;
        })
    }
  }
}
```

This example uses [SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) to set a symbol icon for [ChipV2](arkts-arkui-arkui-advanced-chipv2-chipv2-s.md).
Since API version 26.0.0, ChipV2 is introduced.

```TypeScript
import { ChipV2, ChipV2Options, ChipV2Label, ChipV2PrefixSymbolIcon, SymbolGlyphModifier, LengthMetrics, ColorMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      ChipV2({
        chipV2Options: new ChipV2Options({
          // Set the prefix symbol icon attribute.
          prefixIcon: new ChipV2PrefixSymbolIcon({
            normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Green]),
            activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Red]),
          }),
          // Set the text attribute.
          label: new ChipV2Label({
            text: 'Chip',
            fontSize: LengthMetrics.fp(12),
            fontColor: ColorMetrics.resourceColor(Color.Blue),
            activatedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
            fontFamily: 'HarmonyOS Sans',
            labelMargin: { left: LengthMetrics.fp(20), right: LengthMetrics.fp(30) },
          }),
          size: { width: LengthMetrics.fp(160), height: LengthMetrics.fp(36) },
          allowClose: true,
          enabled: true,
          activated: this.isActivated,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          activatedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          borderRadius: LengthMetrics.resource($r('sys.float.ohos_id_corner_radius_button')),
          onClose: () => {
            console.info('chip on close');
          },
          onClicked: () => {
            console.info('chip on clicked');
          }
        })
      })

      Button('Change active state')
        .onClick(() => {
          this.isActivated = !this.isActivated;
        })
    }
  }
}
```

ChipV2Options uses the @ObservedV2 decorator, and the [ChipV2](arkts-arkui-arkui-advanced-chipv2-chipv2-s.md) component receives the ChipV2Options object through @Param. For primitive type attributes decorated by @Trace, @Param can already observe attribute changes and trigger UI refresh. However, for internal attributes (such as start and end of padding) of object-type attributes (such as padding and labelMargin of label), these object types themselves are not decorated by @ObservedV2. Therefore, changes to their internal attributes cannot be perceived by @Param, and the UI is not automatically refreshed when internal attributes are changed. Using makeObserved to wrap object-type attributes (such as padding) can supplement deep observation capability for their internal attributes. In this way, when internal attributes (such as start and end) are changed, the framework can listen for the changes and trigger UI refresh. For detailed description of the makeObserved API, see [makeObserved API: Changing Unobservable Data to Observable Data](../../../ui/state-management/arkts-new-makeObserved.md).
The following example uses makeObserved to wrap padding, and changes the start and end attributes of padding through a button, to verify that changes to internal attributes of object-type attributes can trigger UI refresh of ChipV2.

```TypeScript
import { ChipV2, ChipV2Options, ChipV2Label, LengthMetrics, ColorMetrics, UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local chipV2Options: ChipV2Options = new ChipV2Options({
    // Set the text attribute.
    label: new ChipV2Label({ text: 'Chip' }),
    // Use UIUtils.makeObserved to wrap padding so that the internal attributes start and end are observable.
    padding: UIUtils.makeObserved({ start: LengthMetrics.fp(20), end: LengthMetrics.fp(20) }),
    backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
    borderRadius: LengthMetrics.resource($r('sys.float.ohos_id_corner_radius_button')),
    enabled: true,
  });
  @Local currentPadding: number = 20;

  build() {
    Column({ space: 10 }) {
      ChipV2({ chipV2Options: this.chipV2Options })
      Button('Change padding')
        .onClick(() => {
          if (this.chipV2Options.padding) {
            this.currentPadding = this.currentPadding === 20 ? 10 : 20;
            // Change the internal attributes of padding. The UI is automatically refreshed because padding is wrapped with makeObserved.
            this.chipV2Options.padding.start = LengthMetrics.fp(this.currentPadding);
            this.chipV2Options.padding.end = LengthMetrics.fp(this.currentPadding);
          }
        })
    }
    .padding(20)
  }
}
```
