# FontInfo

Information about the system font.

**Since:** 10

<!--Device-font-interface FontInfo--><!--Device-font-interface FontInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from '@kit.ArkUI';
```

## family

```TypeScript
family: string
```

Family of the system font.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-family: string--><!--Device-FontInfo-family: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fullName

```TypeScript
fullName: string
```

Name of the system font.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-fullName: string--><!--Device-FontInfo-fullName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## italic

```TypeScript
italic: boolean
```

Whether the system font is italic.

Default value: **false**

**true**: The system font is italic. **false**: The system font is not italic.

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-italic: boolean--><!--Device-FontInfo-italic: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## monoSpace

```TypeScript
monoSpace: boolean
```

Whether the system font is monospaced.

Default value: **false**

**true**: The system font is monospaced. **false**: The system font is not monospaced.

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-monoSpace: boolean--><!--Device-FontInfo-monoSpace: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

File path of the system font.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-path: string--><!--Device-FontInfo-path: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## postScriptName

```TypeScript
postScriptName: string
```

PostScript name of the system font.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-postScriptName: string--><!--Device-FontInfo-postScriptName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subfamily

```TypeScript
subfamily: string
```

Subfamily of the system font.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-subfamily: string--><!--Device-FontInfo-subfamily: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolic

```TypeScript
symbolic: boolean
```

Whether the system font supports symbols.

Default value: **false**

**true**: The system font supports symbols. **false**: The system font does not support symbols.

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-symbolic: boolean--><!--Device-FontInfo-symbolic: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## weight

```TypeScript
weight: number
```

Weight of the system font.

Value range: [100, 900], with intervals of 100, corresponding to the values in the [FontWeight](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-fontweight-e.md) enum

Default value: **100**

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-weight: number--><!--Device-FontInfo-weight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

Width of the system font.

Value range: [1, 9], with intervals of 1, corresponding to the values in the [FontWidth](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-fontwidth-e.md) enum

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FontInfo-width: number--><!--Device-FontInfo-width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

