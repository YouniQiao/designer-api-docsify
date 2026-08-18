# OperateCheckV2

Declare type OperateCheckV2

**Since:** 26.0.0

<!--Device-unnamed-export declare class OperateCheckV2--><!--Device-unnamed-export declare class OperateCheckV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ComposeListItemV2, ContentItemV2, ContentItemV2Options, IconTypeV2, OperateButtonV2, OperateButtonV2Options, OperateCheckV2, OperateCheckV2Options, OperateIconV2, OperateIconV2Options, OperateItemV2, OperateItemV2Options } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: OperateCheckV2Options)
```

The constructor of OperateCheckV2.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateCheckV2-constructor(options?: OperateCheckV2Options)--><!--Device-OperateCheckV2-constructor(options?: OperateCheckV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [OperateCheckV2Options](../../apis-na/arkts-apis/arkts-na-arkui-advanced-composelistitemv2-operatecheckv2options-i.md) | No | The options of OperateCheckV2 |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

The accessibilityDescription of the checkbox/switch/radio.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateCheckV2-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-OperateCheckV2-@Trace  public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

The accessibilityLevel of the checkbox/switch/radio.

**Type:** string

**Default:** auto

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateCheckV2-@Trace  public accessibilityLevel?: string--><!--Device-OperateCheckV2-@Trace  public accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  public accessibilityText?: ResourceStr
```

The accessibilityText of the checkbox/switch/radio.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateCheckV2-@Trace  public accessibilityText?: ResourceStr--><!--Device-OperateCheckV2-@Trace  public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCheck

```TypeScript
@Trace
  public isCheck?: boolean
```

Whether is checked on default.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateCheckV2-@Trace  public isCheck?: boolean--><!--Device-OperateCheckV2-@Trace  public isCheck?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
@Trace
  public onChange?: OnChangeCallback
```

Callback function when operate the checkbox/switch/radio.

**Type:** [OnChangeCallback](../../apis-na/arkts-apis/arkts-na-onchangecallback-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-OperateCheckV2-@Trace  public onChange?: OnChangeCallback--><!--Device-OperateCheckV2-@Trace  public onChange?: OnChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

