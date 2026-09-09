# Select

The **Select** component provides a drop-down menu that allows users to select among multiple options.

> **NOTE**

## Child Components

Not supported

## Select

```TypeScript
Select(options: Array<SelectOption>)
```

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | Array&lt;[SelectOption](arkts-arkui-selectoption-i.md)&gt; | Yes | Options of the drop-down menu. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [MenuItemConfiguration](arkts-arkui-menuitemconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. Inherits from [CommonConfiguration](arkts-arkui-commonconfiguration-i.md). |
| [MenuOutlineOptions](arkts-arkui-menuoutlineoptions-i.md) | Defines the outline of the drop-down menu. |
| [SelectOption](arkts-arkui-selectoption-i.md) | Provides information about the drop-down menu options. |

### Types

| Name | Description |
| --- | --- |
| [OnSelectCallback](arkts-arkui-onselectcallback-t.md) | Defines the callback invoked when a drop-down menu option is selected. |

### Enums

| Name | Description |
| --- | --- |
| [ArrowPosition](arkts-arkui-arrowposition-e.md) | Enumerates arrow positions. |
| [AvoidanceMode](arkts-arkui-avoidancemode-e.md) | Enumerates the drop-down menu avoidance modes. |
| [MenuAlignType](arkts-arkui-menualigntype-e.md) | Enumerates drop-down menu alignment modes. |

## Examples

This example implements a dropdown menu by configuring [SelectOption](arkts-arkui-selectoption-i.md), and sets the [avoidance](arkts-arkui-select-attribute.md#avoidance) attribute to implement the menu avoidance mode since API version 19.

```TypeScript
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = 2;
  @State space: number = 8;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // $r('app.media.selection') needs to be replaced with the image resource file required by the developer.
      Select([{ value: 'aaa', icon: $r("app.media.selection") },
        { value: 'bbb', icon: $r("app.media.selection") },
        { value: 'ccc', icon: $r("app.media.selection") },
        { value: 'ddd', icon: $r("app.media.selection") }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .space(this.space)
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        /**
         * Callback invoked when a dropdown option is selected.
         * index: index of the selected item.
         * text: text of the selected item (optional parameter).
         */
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          // Update the selected index state.
          this.index = index;
          // If text exists, update the text displayed in the selection box.
          if (text) {
            this.text = text;
          }
        })
        // When there is not enough space below the component, cover the target component.
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
}
```

This example implements a Select component whose dropdown menu images are Symbols, and implements the menu avoidance mode by setting the [avoidance](arkts-arkui-select-attribute.md#avoidance) attribute since API version 19.

```TypeScript
// xxx.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = 2;
  @State space: number = 8;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;
  @State symbolModifier1: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Green]);
  @State symbolModifier2: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]);
  @State symbolModifier3: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);
  @State symbolModifier4: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);

  build() {
    Column() {
      Select([{ value: 'aaa', symbolIcon: this.symbolModifier1 },
        { value: 'bbb', symbolIcon: this.symbolModifier2 },
        { value: 'ccc', symbolIcon: this.symbolModifier3 },
        { value: 'ddd', symbolIcon: this.symbolModifier4 }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .space(this.space)
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        /**
         * Callback for selecting a dropdown item
         * index: index of the selected item
         * text: text of the selected item (optional parameter)
         */
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          // Update the selected index state.
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        // Cover the target component when there is insufficient space below the component.
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
}
```

This example implements a Select component with custom dropdown menu options. The custom dropdown menu option style is "text + Symbol image + blank spacing + text + drawn triangle". After a menu option is clicked, the Select component displays the text content of the menu option.

```TypeScript
import { SymbolGlyphModifier } from '@kit.ArkUI';

/**
 * Custom dropdown menu item content modifier
 * Implements the standard ContentModifier interface to replace the default Item layout of the Select dropdown panel
 * Allows custom text to be passed in to display additional text at the end of the menu item
 */
class MyMenuItemContentModifier implements ContentModifier<MenuItemConfiguration> {
  modifierText: string = "";

  constructor(text: string) {
    this.modifierText = text;
  }

  applyContent(): WrappedBuilder<[MenuItemConfiguration]> {
    return wrapBuilder(MenuItemBuilder);
  }
}

/**
 * Custom Select dropdown menu item UI builder
 * Completely rewrites the MenuItem layout: left text + icon + custom text + triangle border graphic
 * @param configuration Select internal menu item configuration object, containing information such as value, index, icon, and custom modifier
 */
@Builder
function MenuItemBuilder(configuration: MenuItemConfiguration) {
  Row() {
    Text(configuration.value)
    Blank()
    // Prioritize rendering the system vector Symbol icon.
    if (configuration.symbolIcon) {
      SymbolGlyph().attributeModifier(configuration.symbolIcon).fontSize(24)
    } else if (configuration.icon) {
      Image(configuration.icon).size({ width: 24, height: 24 })
    }
    Blank(30)
    // Read and display the trailing text passed in by the custom modifier.
    Text((configuration.contentModifier as MyMenuItemContentModifier).modifierText)
    Blank(30)
    // Draw a custom triangle path with stroke only and no fill.
    Path()
      .width('100px')
      .height('150px')
      .commands('M40 0 L80 100 L0 100 Z')
      .fillOpacity(0)
      .stroke(Color.Black)
      .strokeWidth(3)
  }
  .padding({left: 8, top: 8})
  .onClick(() => {
    configuration.triggerSelect(configuration.index, configuration.value.valueOf().toString());
  })
}

@Entry
@Component
struct SelectExample {
  @State text: string = "Content Modifier Select";
  @State symbolModifier1: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);
  @State symbolModifier2: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);

  build() {
    Column() {
      Row() {
        // $r('app.media.icon') needs to be replaced with the image resource file required by the developer.
        Select([{ value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier1 },
          { value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier2 }])
          .value(this.text)
          .onSelect((index: number, text?: string) => {
            console.info('Select index:' + index);
            console.info('Select text:' + text);
          })
          // Bind the custom menu item modifier to replace the default layout of the dropdown panel.
          .menuItemContentModifier(new MyMenuItemContentModifier("Content Modifier"))

      }.alignItems(VerticalAlign.Center).height('50%')
    }
  }
}
```

This example implements a dropdown menu with a divider style by configuring the DividerOptions type of divider, and implements the menu avoidance mode by setting the [avoidance](arkts-arkui-select-attribute.md#avoidance) attribute since API version 19.

```TypeScript
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // $r('app.media.icon') needs to be replaced with the image resource file required by the developer.
      Select([{ value: 'aaa', icon: $r("app.media.icon") },
        { value: 'bbb', icon: $r("app.media.icon") },
        { value: 'ccc', icon: $r("app.media.icon") },
        { value: 'ddd', icon: $r("app.media.icon") }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        /**
         * Custom configuration of the divider between dropdown options.
         * strokeWidth: divider thickness.
         * color: divider color.
         * startMargin/endMargin: left and right margins of the divider.
         */
        .divider({
          strokeWidth: 5,
          color: Color.Blue,
          startMargin: 10,
          endMargin: 10
        })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
}
```

This example implements a dropdown menu without dividers by setting divider to null, and implements the menu avoidance mode by setting the [avoidance](arkts-arkui-select-attribute.md#avoidance) attribute since API version 19.

```TypeScript
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      // $r('app.media.icon') needs to be replaced with the image resource file required by the developer.
      Select([{ value: 'aaa', icon: $r("app.media.icon") },
        { value: 'bbb', icon: $r("app.media.icon") },
        { value: 'ccc', icon: $r("app.media.icon") },
        { value: 'ddd', icon: $r("app.media.icon") }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        // Pass null to divider to hide the dividers between options.
        .divider(null)
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .avoidance(AvoidanceMode.COVER_TARGET);
    }.width('100%')
  }
}
```

Since API version 20, this example sets the text and arrow styles through the [textModifier](#textmodifier20) and [arrowModifier](arkts-arkui-select-attribute.md#arrowmodifier) attributes.

```TypeScript
import { TextModifier, SymbolGlyphModifier } from "@kit.ArkUI";

/**
 * Use TextModifier to uniformly control the text style displayed in the selection box.
 * Use SymbolGlyphModifier to customize the size and color of the dropdown arrow icon on the right.
 */
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTTTTTTT".repeat(3);
  @State index: number = 2;
  textModifier: TextModifier = new TextModifier();
  symbolGlyphModifier: SymbolGlyphModifier = new SymbolGlyphModifier();

  aboutToAppear(): void {
    // Initialize the global style of the main text.
    this.textModifier
      .maxLines(2)
      .fontSize(18)
      .textAlign(TextAlign.Center)
      .fontColor('#333333')
      .fontWeight(FontWeight.Medium)
      .textOverflow({overflow:TextOverflow.Clip})

    // Initialize the style of the dropdown arrow icon.
    this.symbolGlyphModifier
      .fontSize(25)
      .fontColor(['#999999'])
  }

  build() {
    Column() {
      Select([
        // $r('app.media.startIcon') needs to be replaced with the image resource file required by the developer.
        { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
        { value: 'Option B', icon: $r("app.media.startIcon") },
        { value: 'Option C', icon: $r("app.media.startIcon") },
        { value: 'Option D', icon: $r("app.media.startIcon") }
      ])
        .selected(this.index)
        .value(this.text)
        // Bind the custom text modifier to uniformly control the text style.
        .textModifier(this.textModifier)
        // Bind the modifier to customize the dropdown arrow.
        .arrowModifier(this.symbolGlyphModifier)
        .onSelect((index: number, text?: string) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        .margin({ top: 20,left:30 })
        .borderRadius(12)
        .width(200)
        .padding(9)
        .backgroundColor(Color.White)
        .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
    }
    .alignItems(HorizontalAlign.Start)
    .padding(10)
    .backgroundColor('#F0F2F5')
    .width('100%')
    .height('100%')
  }
}
```

Since API version 20, this example uses the [optionTextModifier](arkts-arkui-select-attribute.md#optiontextmodifier) and [selectedOptionTextModifier](arkts-arkui-select-attribute.md#selectedoptiontextmodifier) attributes to set the text styles of selected and unselected items in the dropdown menu.

```TypeScript
import { TextModifier } from "@kit.ArkUI";

/**
 * Use two independent TextModifier objects to control the styles of [normal option text] and [selected option text] in the dropdown panel respectively.
 */
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTTTTTTT".repeat(3);
  @State index: number = 2;
  optionTextModifier: TextModifier = new TextModifier();
  selectedOptionTextModifier: TextModifier = new TextModifier();
  aboutToAppear(): void {
    // Initialize the text style of normal dropdown options.
    this.optionTextModifier
      .maxLines(1)
      .fontSize(16)
      .textAlign(TextAlign.Start)
      .fontColor('#666666')
      .fontWeight(FontWeight.Normal)
      .width(200)

    // Initialize the text style of the selected dropdown option (highlighted for distinction).
    this.selectedOptionTextModifier
      .maxLines(1)
      .fontSize(18)
      .textAlign(TextAlign.Start)
      .fontColor('#007BFF')
      .fontWeight(FontWeight.Bold)
      .width(200)
  }

  build() {
    Column() {
      Select([
        // $r('app.media.startIcon') needs to be replaced with the image resource file required by the developer.
        { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
        { value: 'Option B', icon: $r("app.media.startIcon") },
        { value: 'Option C', icon: $r("app.media.startIcon") },
        { value: 'Option D', icon: $r("app.media.startIcon") }
      ])
        .selected(this.index)
        .value(this.text)
        .onSelect((index: number, text?: string) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
        // Bind the text modifier of normal options.
        .optionTextModifier(this.optionTextModifier)
        // Bind the text modifier of the selected option to implement the highlighted differentiated style for the selected item.
        .selectedOptionTextModifier(this.selectedOptionTextModifier)
        .margin({ top: 20,left:30 })
        .borderRadius(12)
        .width(200)
        .padding(9)
        .backgroundColor(Color.White)
        .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
    }
    .alignItems(HorizontalAlign.Start)
    .padding(10)
    .backgroundColor('#F0F2F5')
    .width('100%')
    .height('100%')
  }
}
```

Since API version 19, this example sets the divider mode by configuring the mode attribute of [DividerStyleOptions](ts-types.md#dividerstyleoptions12).

```TypeScript
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Select([{ value: "SelectItem" }, { value: "SelectItem" }, { value: "SelectItem" },])
        .value("Please select")
        /**
         * Customize the complete style of the dropdown option divider.
         * strokeWidth: divider thickness, using the vp unit to adapt to different screens.
         * color: light gray color of the divider.
         * mode: EMBEDDED_IN_MENU embedded mode.
         */
        .dividerStyle({
          strokeWidth: LengthMetrics.vp(5),
          color: '#d5d5d5',
          mode: DividerMode.EMBEDDED_IN_MENU
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

Since API version 20, this example sets the outline style of the dropdown menu by configuring the width and color attributes of menuOutline.

```TypeScript
// xxx.ets
@Entry
@Component
struct SelectExample {
  @State text: string = "TTTTT";
  @State index: number = -1;
  @State arrowPosition: ArrowPosition = ArrowPosition.END;

  build() {
    Column() {
      Select([{ value: 'aaa' },
        { value: 'bbb' },
        { value: 'ccc' },
        { value: 'ddd' }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 16, weight: 400 })
        .optionFont({ size: 16, weight: 400 })
        .arrowPosition(this.arrowPosition)
        .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
        .optionWidth(200)
        .optionHeight(300)
        /**
         * Dropdown menu outline style configuration.
         * width: border thickness 5vp.
         * color: border color blue.
         */
        .menuOutline({
          width: '5vp',
          color: Color.Blue
        })
        .onSelect((index: number, text?: string | undefined) => {
          console.info('Select:' + index);
          this.index = index;
          if (text) {
            this.text = text;
          }
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F0F2F5')
  }
}
```

This example calls the [keyboardAvoidMode](#keyboardavoidmode23) and [minKeyboardAvoidDistance](#minkeyboardavoiddistance23) APIs to make the dropdown menu avoid the soft keyboard and customize the minimum distance for avoiding the soft keyboard.
Since API version 23, the keyboardAvoidMode and minKeyboardAvoidDistance APIs are added.

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { LengthMetrics } from '@kit.ArkUI';

/**
 * Example page for the Select dropdown component + automatic input method mounting
 * Configure the popup menu keyboard avoidance policy, and click the dropdown box to actively mount the input method after a 2-second delay
 */
@Entry
@Component
struct Index {
  private inputController: inputMethod.InputMethodController | null = null;
  onPageShow(): void {
    try {
      this.inputController = inputMethod.getController();
    } catch (err) {
      console.error("get input method controller fail: ", JSON.stringify(err));
    }
  }

  build() {
    RelativeContainer() {
      Select([{ value: 'SelectOption' },
        { value: 'SelectOption' },
        { value: 'SelectOption' },
        { value: 'SelectOption' },
        { value: 'SelectOption' }])
        .value('Click Show Options')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
        })
        // Soft keyboard popup avoidance mode: translate and resize the dropdown popup to avoid being covered by the keyboard
        .keyboardAvoidMode(MenuKeyboardAvoidMode.TRANSLATE_AND_RESIZE)
        // Minimum reserved distance of 20vp between the popup and the soft keyboard
        .minKeyboardAvoidDistance(LengthMetrics.vp(20))
        .onClick(() => {
          setTimeout(() => {
            this.attachAndListener()
          }, 2000)
        })
    }
    .height('100%')
    .width('100%')
  }

  /**
   * Mount the input method listener, an asynchronous method
   * 1. Actively set focus on the page Index identifier
   * 2. Verify the validity of the input method controller instance
   * 3. Mount the input method, and configure the text input type and the search enter key
   */
  async attachAndListener() {
    focusControl.requestFocus('Index')
    if (!this.inputController) {
      console.error('inputController instance is null!');
      return;
    }
    try {
      await this.inputController.attach(true, {
        inputAttribute: {
          textInputType: inputMethod.TextInputType.TEXT, // Normal text input type
          enterKeyType: inputMethod.EnterKeyType.SEARCH // The enter key displays the search text
        }
      })
    } catch (err) {
      console.error('Fail to attach')
    }
  }
}
```

This example calls the [menuSystemMaterial](arkts-arkui-select-attribute.md#menusystemmaterial) API to set the system material of the dropdown menu to achieve the immersive light effect, and calls the [SystemUiMaterial](ts-universal-attributes-image-effect.md#systemuimaterial) API to set the system material of the Select component to achieve the immersive light effect.
The immersive light effect of the component is adaptively adjusted based on the device computing power and the immersive light effect set by the user in the system, and no additional adaptation is required by the developer.
Since API version 26.0.0, the menuSystemMaterial API is added.

```TypeScript
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Select([{ value: 'SelectOption' },
        { value: 'SelectOption' },
        { value: 'SelectOption' },
        { value: 'SelectOption' },
        { value: 'SelectOption' }])
        .value('Click Show Options')
        /**
         * Configure the immersive frosted material of the selection box itself.
         * ULTRA_THIN: ultra-thin and transparent frosted material with high transparency, making the underlying image more visible.
         */
        .systemMaterial(new uiMaterial.ImmersiveMaterial({
            style: uiMaterial.ImmersiveStyle.ULTRA_THIN
          }))
        /**
         * Configure the immersive frosted material of the dropdown pop-up panel.
         * THICK: thick frosted material with lower transparency and a stronger occlusion effect.
         */
        .menuSystemMaterial(new uiMaterial.ImmersiveMaterial({
            style: uiMaterial.ImmersiveStyle.THICK
          }))
    }
    // $r('app.media.img') needs to be replaced with the image resource file required by the developer.
    .backgroundImage($r('app.media.img'))
  }
}
```
