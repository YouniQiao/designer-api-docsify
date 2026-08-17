# OperateIconV2

Declare type OperateIconV2

**Since:** 26.0.0

<!--Device-unnamed-export declare class OperateIconV2--><!--Device-unnamed-export declare class OperateIconV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ComposeListItemV2 } from 'ComposeListItemV2';
import { ContentItemV2 } from 'ContentItemV2';
import { ContentItemV2Options } from 'ContentItemV2Options';
import { IconTypeV2 } from 'IconTypeV2';
import { OperateButtonV2 } from 'OperateButtonV2';
import { OperateButtonV2Options } from 'OperateButtonV2Options';
import { OperateCheckV2 } from 'OperateCheckV2';
import { OperateCheckV2Options } from 'OperateCheckV2Options';
import { OperateIconV2 } from 'OperateIconV2';
import { OperateIconV2Options } from 'OperateIconV2Options';
import { OperateItemV2 } from 'OperateItemV2';
import { OperateItemV2Options } from 'OperateItemV2Options';
```

## constructor

```TypeScript
constructor(options?: OperateIconV2Options)
```

The constructor of OperateIconV2.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateIconV2-constructor(options?: OperateIconV2Options)--><!--Device-OperateIconV2-constructor(options?: OperateIconV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [OperateIconV2Options](arkts-arkui-arkui-advanced-composelistitemv2-operateiconv2options-i.md) | No | The options of OperateIconV2 |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

The accessibilityDescription of the icon.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateIconV2-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-OperateIconV2-@Trace  public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

The accessibilityLevel of the icon.

**Type:** string

**Default:** auto

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateIconV2-@Trace  public accessibilityLevel?: string--><!--Device-OperateIconV2-@Trace  public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  public accessibilityText?: ResourceStr
```

The accessibilityText of the icon.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateIconV2-@Trace  public accessibilityText?: ResourceStr--><!--Device-OperateIconV2-@Trace  public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
@Trace
  public action?: OnActionCallback
```

Callback function when operate the icon.

**Type:** [OnActionCallback](arkts-arkui-onactioncallback-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateIconV2-@Trace  public action?: OnActionCallback--><!--Device-OperateIconV2-@Trace  public action?: OnActionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
@Trace
  public symbolStyle?: SymbolGlyphModifier
```

The content of text or the address of symbol

**Type:** SymbolGlyphModifier

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateIconV2-@Trace  public symbolStyle?: SymbolGlyphModifier--><!--Device-OperateIconV2-@Trace  public symbolStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
@Trace
  public value: ResourceStr
```

The content of text or the address of icon.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateIconV2-@Trace  public value: ResourceStr--><!--Device-OperateIconV2-@Trace  public value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

