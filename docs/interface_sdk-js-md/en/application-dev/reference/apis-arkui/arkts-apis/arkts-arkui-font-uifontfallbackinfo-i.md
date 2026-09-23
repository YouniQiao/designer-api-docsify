# UIFontFallbackInfo

```TypeScript
interface UIFontFallbackInfo
```

Provides the fallback font of the font set.

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

Language type supported by the font family. The language format is a BCP47 tag (for example, **"zh-Hans"** indicates Simplified Chinese, and **"en"** indicates English).

**Type:** string

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
