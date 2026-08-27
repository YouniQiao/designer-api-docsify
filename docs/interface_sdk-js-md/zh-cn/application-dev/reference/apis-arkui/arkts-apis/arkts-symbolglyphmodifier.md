# SymbolGlyphModifier

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-c.md) | Defines SymbolGlyph Modifier |

## 示例

该示例通过[SymbolGlyphModifier](#symbolglyphmodifier)和TextInput组件的[cancelButton](./ts-basic-components-textinput.md#cancelbutton18)属性展示了自定义右侧symbol类型清除按钮样式的效果。

```TypeScript
import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State text: string = '';
  symbolGlyphModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .height(50)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolGlyphModifier // 从API version 18开始支持SymbolGlyph类型
        })
    }.margin(10)
  }
}
```
