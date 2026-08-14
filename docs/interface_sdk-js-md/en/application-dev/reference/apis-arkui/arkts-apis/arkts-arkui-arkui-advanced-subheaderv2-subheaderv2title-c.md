# SubHeaderV2Title

Defines the title settings for the subheader.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare class SubHeaderV2Title--><!--Device-unnamed-export declare class SubHeaderV2Title-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SubHeaderV2IconType } from 'SubHeaderV2IconType';
import { SubHeaderV2Title } from 'SubHeaderV2Title';
import { SubHeaderV2Select } from 'SubHeaderV2Select';
import { SubHeaderV2 } from 'SubHeaderV2';
import { SubHeaderV2OperationType } from 'SubHeaderV2OperationType';
import { SubHeaderV2OperationItem } from 'SubHeaderV2OperationItem';
import { SubHeaderV2OperationItemType } from 'SubHeaderV2OperationItemType';
```

## constructor

```TypeScript
constructor(options: SubHeaderV2TitleOptions)
```

A constructor used to create a **SubHeaderV2Title** object.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Title-constructor(options: SubHeaderV2TitleOptions)--><!--Device-SubHeaderV2Title-constructor(options: SubHeaderV2TitleOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SubHeaderV2TitleOptions](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2titleoptions-i.md) | Yes | Options for initializing the title. |

## id

```TypeScript
@Trace
  id?: string
```

Set the id of the title.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-SubHeaderV2Title-@Trace  id?: string--><!--Device-SubHeaderV2Title-@Trace  id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@Trace
  primaryTitle?: ResourceStr
```

The first line text of content area.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Title-@Trace  primaryTitle?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  primaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitleModifier

```TypeScript
@Trace
  primaryTitleModifier?: TextModifier
```

Text modifier for primary title.

**Type:** TextModifier

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Title-@Trace  primaryTitleModifier?: TextModifier--><!--Device-SubHeaderV2Title-@Trace  primaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@Trace
  secondaryTitle?: ResourceStr
```

The secondary line text of content area.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Title-@Trace  secondaryTitle?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitleModifier

```TypeScript
@Trace
  secondaryTitleModifier?: TextModifier
```

Text modifier for secondary title.

**Type:** TextModifier

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2Title-@Trace  secondaryTitleModifier?: TextModifier--><!--Device-SubHeaderV2Title-@Trace  secondaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleAccessibilityText

```TypeScript
@Trace
  titleAccessibilityText?: ResourceStr
```

Customized content to be read in the title. Default value: **undefined** If the value is **undefined**, the title content displayed by the component is read by default. Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SubHeaderV2Title-@Trace  titleAccessibilityText?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  titleAccessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

