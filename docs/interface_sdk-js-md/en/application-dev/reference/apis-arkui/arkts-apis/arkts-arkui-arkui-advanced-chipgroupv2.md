# @ohos.arkui.advanced.ChipGroupV2

## Modules to Import

```TypeScript
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ChipGroupV2Item](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2item-c.md) | Defines chip group item. |
| [ChipGroupV2Items](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2items-c.md) | Defines items of chip group. |
| [ChipGroupV2ItemStyle](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2itemstyle-c.md) | Defines ChipGroupV2 item style. |
| [ChipGroupV2Padding](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2padding-c.md) | Defines chip group padding. |
| [ChipGroupV2Space](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2space-c.md) | Defines chip group space. |

### Structs

| Name | Description |
| --- | --- |
| [ChipGroupV2](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2-s.md) | Defines chipGroupV2. |
| [ChipGroupV2IconGroupSuffix](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2icongroupsuffix-s.md) | Defines IconGroupSuffix. |

### Interfaces

| Name | Description |
| --- | --- |
| [ChipGroupV2IconItemConfig](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2iconitemconfig-i.md) | Defines ChipGroupV2 IconItemConfig. |
| [ChipGroupV2ItemConfig](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2itemconfig-i.md) | Defines chip item config. |
| [ChipGroupV2ItemStyleConfig](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2itemstyleconfig-i.md) | Defines ChipGroupV2 item style. |
| [ChipGroupV2PaddingConfig](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2paddingconfig-i.md) | Defines ChipGroupV2 padding config. |
| [ChipGroupV2SpaceConfig](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2spaceconfig-i.md) | Defines chip group space config. |
| [ChipGroupV2SymbolItemConfig](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2symbolitemconfig-i.md) | Defines symbol item config. |

## Examples

This example implements the effect of [ChipGroupV2](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2-s.md) without the rightmost custom component by not setting the suffix parameter.

```TypeScript
import { ChipV2Size, ChipGroupV2, ChipGroupV2Items, ChipGroupV2ItemStyle, ChipGroupV2Space, ChipGroupV2Padding, ColorMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local selectedIndex: Array<number> = [0];

  build() {
    Column() {
      ChipGroupV2({
        // Each object in items sets the specific attributes of each ChipV2.
        items: new ChipGroupV2Items([
          {
            // Replace $r('app.media.icon') with the image resource file as required.
            prefixIcon: { src: $r('app.media.icon') },
            label: { text: 'Chip 1' },
            suffixIcon: { src: $r('sys.media.ohos_ic_public_cut') },
            allowClose: false
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_copy') },
            label: { text: 'Chip 2' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
            label: { text: 'Chip 3' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: 'Chip 4' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
            label: { text: 'Chip 5' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: 'Chip 6' },
            allowClose: true
          },
        ]),
        // Set the style attribute of ChipV2.
        itemStyle: new ChipGroupV2ItemStyle({
          size: ChipV2Size.SMALL,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          fontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary')),
          selectedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          selectedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
        }),
        selectedIndexes: this.selectedIndex,
        multiple: false,
        chipGroupSpace: new ChipGroupV2Space({ itemSpace: 8, endSpace: 0 }),
        chipGroupPadding: new ChipGroupV2Padding({ top: 10, bottom: 10 }),
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
      })
    }
  }
}
```

This example implements the rightmost custom component effect of [ChipGroupV2](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2-s.md) by setting the suffix parameter.
Since API version 26.0.0, ChipGroupV2 supports the suffix attribute.

```TypeScript
import { ChipV2Size, ChipGroupV2, ChipGroupV2Items, ChipGroupV2IconGroupSuffix, ChipGroupV2ItemStyle, ChipGroupV2Space, ChipGroupV2Padding, ColorMetrics, LengthMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local selectedIndex: Array<number> = [0, 1, 2, 3, 4, 5];
  @Local selectedState: boolean = true;

  @Builder
  ChipGroupSuffix(): void {
    // Implement the rightmost custom component effect by referencing ChipGroupV2IconGroupSuffix.
    ChipGroupV2IconGroupSuffix({
      items: [{
        icon: { src: $r('sys.media.ohos_ic_public_search_filled'), size: { width: LengthMetrics.fp(36), height: LengthMetrics.fp(36) } },
        action: () => {
          if (this.selectedState === false) {
            this.selectedIndex = [0, 1, 2, 3, 4, 5];
            this.selectedState = true;
          } else {
            this.selectedIndex = [];
            this.selectedState = false;
          }
        }
      }
      ]
    })
  }

  build() {
    Column() {
      ChipGroupV2({
        // Each object in items sets the specific attributes of each ChipV2.
        items: new ChipGroupV2Items([
          {
            // Replace $r('app.media.icon') with the image resource file as required.
            prefixIcon: { src: $r('app.media.icon') },
            label: { text: 'Chip 1' },
            suffixIcon: { src: $r('sys.media.ohos_ic_public_cut') },
            allowClose: false
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_copy') },
            label: { text: 'Chip 2' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
            label: { text: 'Chip 3' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: 'Chip 4' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
            label: { text: 'Chip 5' },
            allowClose: true
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: 'Chip 6' },
            allowClose: true
          },
        ]),
        // Set the style attribute of ChipV2.
        itemStyle: new ChipGroupV2ItemStyle({
          size: ChipV2Size.NORMAL,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          fontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary')),
          selectedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          selectedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
        }),
        selectedIndexes: this.selectedIndex,
        multiple: true,
        chipGroupSpace: new ChipGroupV2Space({ itemSpace: 8, endSpace: 0 }),
        chipGroupPadding: new ChipGroupV2Padding({ top: 10, bottom: 10 }),
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
        // Rightmost custom component of ChipGroupV2.
        suffix: this.ChipGroupSuffix
      })
    }
  }
}
```

This example uses [SymbolGlyphModifier](ts-universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) to set symbol icons for [ChipGroupV2IconGroupSuffix](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2icongroupsuffix-s.md) and [ChipGroupV2](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2-s.md).
Since API version 26.0.0, ChipGroupV2IconGroupSuffix and ChipGroupV2 are added.

```TypeScript
import { ChipV2Size, ChipGroupV2, ChipGroupV2Items, ChipGroupV2IconGroupSuffix, SymbolGlyphModifier, ChipGroupV2ItemStyle, ChipGroupV2Space, ChipGroupV2Padding, ColorMetrics } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local selectedIndex: Array<number> = [0, 1, 2, 3, 4, 5];
  @Local selectedState: boolean = true;
  @Local prefixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star'));
  @Local prefixModifierActivated: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]);
  @Local suffixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));
  @Local suffixModifierActivated: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Red]);

  @Builder
  ChipGroupSuffix(): void {
    // Implement a rightmost custom component of the component by referencing ChipGroupV2IconGroupSuffix.
    ChipGroupV2IconGroupSuffix({
      items: [
        new SymbolGlyphModifier($r('sys.symbol.magnifyingglass'))
          .onClick(() => {
            if (this.selectedState === false) {
              this.selectedIndex = [0, 1, 2, 3, 4, 5];
              this.selectedState = true;
            } else {
              this.selectedIndex = [];
              this.selectedState = false;
            }
          })
      ]
    })
  }

  build() {
    Column() {
      ChipGroupV2({
        // Each object in items sets the specific attributes of each ChipV2.
        items: new ChipGroupV2Items([
          {
            prefixSymbolIcon: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
            label: { text: 'Chip 1' },
            suffixSymbolIcon: { normal: this.suffixModifierNormal, activated: this.suffixModifierActivated },
            allowClose: false,
          },
          {
            prefixSymbolIcon: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
            label: { text: 'Chip 2' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
            label: { text: 'Chip 3' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: 'Chip 4' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
            label: { text: 'Chip 5' },
            allowClose: true,
          },
          {
            prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
            label: { text: 'Chip 6' },
            allowClose: true,
          },
        ]),
        // Set the style attribute of ChipV2.
        itemStyle: new ChipGroupV2ItemStyle({
          size: ChipV2Size.NORMAL,
          backgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_button_normal')),
          fontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary')),
          selectedBackgroundColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_emphasize')),
          selectedFontColor: ColorMetrics.resourceColor($r('sys.color.ohos_id_color_text_primary_contrary')),
        }),
        selectedIndexes: this.selectedIndex,
        multiple: true,
        chipGroupSpace: new ChipGroupV2Space({ itemSpace: 8, endSpace: 0 }),
        chipGroupPadding: new ChipGroupV2Padding({ top: 10, bottom: 10 }),
        onChange: (activatedChipsIndex: Array<number>) => {
          console.info('chips on clicked, activated index ' + activatedChipsIndex);
        },
        // Rightmost custom component of ChipGroupV2.
        suffix: this.ChipGroupSuffix
      })
    }
  }
}
```

Classes such as [ChipGroupV2Items](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2items-c.md), [ChipGroupV2Item](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2item-c.md), and [ChipGroupV2ItemStyle](arkts-arkui-arkui-advanced-chipgroupv2-chipgroupv2itemstyle-c.md) are decorated with @ObservedV2, and the ChipGroupV2 component receives attribute parameters through @Param. For primitive-type attributes decorated with @Trace (such as itemSpace of ChipGroupV2Space), @Param can already observe attribute changes and trigger UI refresh without additional processing. However, for internal attributes of object-type attributes in these classes (such as the size of prefixIcon in ChipGroupV2Item), the object types themselves are not decorated with @ObservedV2, so their internal attribute changes cannot be perceived by @Param, causing the UI not to refresh automatically when internal attributes are modified. Using the makeObserved API to wrap object-type attributes can supplement deep observation capability for the internal attributes of the object. For details about the makeObserved API, see [makeObserved API: Changing Unobservable Data to Observable Data](../../../ui/state-management/arkts-new-makeObserved.md).
The following example compares two scenarios: when the Change itemSpace button is tapped to modify the itemSpace attribute of chipGroupSpace (a primitive-type attribute decorated with @Trace, which already supports observation), the UI refreshes automatically; when the Change icon size button is tapped to modify the internal attribute for size of prefixIcon in ChipGroupV2Item (an internal attribute of an object-type attribute, which is observable when size is wrapped with UIUtils.makeObserved), the UI also refreshes automatically.

```TypeScript
import {
  ChipGroupV2,
  ChipGroupV2Items,
  ChipGroupV2ItemStyle,
  ChipGroupV2Space,
  ChipGroupV2Padding,
  LengthMetrics,
  UIUtils
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local items: ChipGroupV2Items = new ChipGroupV2Items([
    {
      // Use UIUtils.makeObserved to wrap size so that the internal attributes width and height can be observed.
      prefixIcon: {
        src: $r('sys.media.ohos_ic_public_clock'),
        size: UIUtils.makeObserved({ width: LengthMetrics.fp(16), height: LengthMetrics.fp(16) })
      },
      label: { text: 'Chip 1' }
    },
    {
      label: { text: 'Chip 2' }
    },
    {
      label: { text: 'Chip 3' }
    }
  ]);
  // The internal attributes of ChipGroupV2Space are already decorated by @Trace, so makeObserved is not required.
  @Local chipGroupSpace: ChipGroupV2Space = new ChipGroupV2Space({ itemSpace: 8 });
  @Local chipGroupPadding: ChipGroupV2Padding = new ChipGroupV2Padding({ top: 10, bottom: 10 });
  @Local itemStyle: ChipGroupV2ItemStyle = new ChipGroupV2ItemStyle({});
  @Local selectedIndexes: number[] = [];
  @Local currentIconSize: number = 16;
  @Local currentItemSpace: number = 8;

  build() {
    Column({ space: 10 }) {
      ChipGroupV2({
        items: this.items,
        $items: (items: ChipGroupV2Items) => { this.items = items; },
        itemStyle: this.itemStyle,
        chipGroupSpace: this.chipGroupSpace,
        chipGroupPadding: this.chipGroupPadding,
        selectedIndexes: this.selectedIndexes,
        $selectedIndexes: (indexes: number[]) => { this.selectedIndexes = indexes; },
      })
      // When a primitive attribute decorated by @Trace is changed, the UI is automatically refreshed.
      Button('Change itemSpace')
        .onClick(() => {
          this.currentItemSpace = this.currentItemSpace === 8 ? 16 : 8;
          this.chipGroupSpace.itemSpace = this.currentItemSpace;
        })
      // When the internal attributes of an object-type attribute is changed, the UI is also automatically refreshed because it is wrapped by makeObserved.
      Button('Change icon size')
        .onClick(() => {
          if (this.items.length >= 1 && this.items[0] && this.items[0].prefixIcon && this.items[0].prefixIcon.size) {
            this.currentIconSize = this.currentIconSize === 16 ? 30 : 16;
            this.items[0].prefixIcon.size.width = LengthMetrics.fp(this.currentIconSize);
            this.items[0].prefixIcon.size.height = LengthMetrics.fp(this.currentIconSize);
          }
        })
    }
  }
}
```
