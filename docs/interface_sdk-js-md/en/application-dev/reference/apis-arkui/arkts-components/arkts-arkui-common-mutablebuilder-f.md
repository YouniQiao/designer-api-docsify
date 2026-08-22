# mutableBuilder

## Modules to Import

```TypeScript
```

## mutableBuilder

```TypeScript
declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>
```

Defining mutableBuilder function.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>--><!--Device-unnamed-declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [BuilderCallback](arkts-arkui-buildercallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MutableBuilder](arkts-arkui-mutablebuilder-c.md)&lt;Args&gt; |  |

**Examples**

```TypeScript
class TextContent {
  text: string = '';
}

@Builder
function textBuilder(p: TextContent) {
  Text(p.text).margin(20)
}

@Builder
function buttonBuilder(p: TextContent) {
  Button(p.text).margin(20)
}

let counter: number = 1;
@Entry
@ComponentV2
struct MyApp {
  @Local message: string = 'init';
  @Local switchingBuilder: MutableBuilder<[TextContent]> = mutableBuilder(textBuilder);
  build() {
    Column() {
      this.switchingBuilder.builder({ text: this.message })
      Button('Click to change')
      .onClick(() => {
        counter++; // Increment the counter on each button click to dynamically switch the global @Builder.
        if(counter % 2 === 0) {
          this.message += 'B';
          this.switchingBuilder = mutableBuilder(buttonBuilder); // textBuilder--->buttonBuilder
        } else {
          this.message += 'T';
          this.switchingBuilder = mutableBuilder(textBuilder); // buttonBuilder--->textBuilder
        }
      })
    }.position({x: 120, y: 60})
  }
}
```

