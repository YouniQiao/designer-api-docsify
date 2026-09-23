# FontInfo

```TypeScript
interface FontInfo
```

Information about the system font.

**Since:** 10

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

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## italic

```TypeScript
italic: boolean
```

Whether the system font is italic.

Default value: **false**

The value **true** indicates an italic font, and **false** indicates a non-italic font.

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## monoSpace

```TypeScript
monoSpace: boolean
```

Whether the system font is monospaced.

Default value: **false**

The value **true** indicates a monospaced font, and **false** indicates a non-monospaced font.

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

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

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolic

```TypeScript
symbolic: boolean
```

Whether the system font supports symbolic fonts.

Default value: **false**

The value **true** indicates that symbolic fonts are supported, and **false** indicates that symbolic fonts are not supported.

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## weight

```TypeScript
weight: number
```

Weight of the system font.

Value range: [100, 900], with an interval of 100, corresponding to the values in [FontWeight](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontweight-e.md).

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

Width of the system font.

Value range: [1, 9], with an interval of 1, corresponding to the values in [FontWidth](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontwidth-e.md).

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
