# UIFontFallbackInfo

UI font configuration of the system.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from '@kit.ArkUI';
```

## family

```TypeScript
family: string
```

Font family name, which is the value of **family** specified in the font file.

**Type:** string

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## language

```TypeScript
language: string
```

Language supported by the font family. The language format is BCP 47.

**Type:** string

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  build() {
    Column() {
      Button("getUIFontConfig")
        .width('60%')
        .height('6%')
        .margin(50)
        .onClick(() => {
          let fontConfig = font.getUIFontConfig();
          console.info("font-dir -----------" + String(fontConfig.fontDir.length));
          for (let i = 0; i < fontConfig.fontDir.length; i++) {
            console.info(fontConfig.fontDir[i]);
          }
          console.info("generic-------------" + String(fontConfig.generic.length));
          for (let i = 0; i < fontConfig.generic.length; i++) {
            console.info("family:" + fontConfig.generic[i].family);
            for (let j = 0; j < fontConfig.generic[i].alias.length; j++) {
              console.info(fontConfig.generic[i].alias[j].name + " " + fontConfig.generic[i].alias[j].weight);
            }
            for (let j = 0; j < fontConfig.generic[i].adjust.length; j++) {
              console.info(fontConfig.generic[i].adjust[j].weight + " " + fontConfig.generic[i].adjust[j].to);
            }
          }
          console.info("fallback------------" + String(fontConfig.fallbackGroups.length));
          for (let i = 0; i < fontConfig.fallbackGroups.length; i++) {
            console.info("fontSetName:" + fontConfig.fallbackGroups[i].fontSetName);
            for (let j = 0; j < fontConfig.fallbackGroups[i].fallback.length; j++) {
              console.info("language:" + fontConfig.fallbackGroups[i].fallback[j].language + " family:" +
              fontConfig.fallbackGroups[i].fallback[j].family);
            }
          }
        })
    }.width('100%')
  }
}
```
