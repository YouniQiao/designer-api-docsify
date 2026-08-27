# SymbolGlyphModifier

## Summary

### Classes

| Name | Description |
| --- | --- |
| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) | Defines SymbolGlyph Modifier |

## Examples

This example demonstrates how to use [SymbolGlyphModifier](#symbolglyphmodifier) and the [cancelButton](ts-basic-components-textinput.md#cancelbutton18) attribute of the TextInput component to customize the style of the symbol-type cancel button on the right side of the text box.

```TypeScript
import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State text: string = '';
  symbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .height(50)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolModifier // The symbol type is supported since API version 18.
        })
    }.margin(10)
  }
}
```
