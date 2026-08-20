# SubHeaderV2Title

Defines the title settings for the subheader.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class SubHeaderV2Title--><!--Device-unnamed-export declare class SubHeaderV2Title-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(options: SubHeaderV2TitleOptions)
```

A constructor used to create a **SubHeaderV2Title** object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Title-public constructor(options: SubHeaderV2TitleOptions)--><!--Device-SubHeaderV2Title-public constructor(options: SubHeaderV2TitleOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SubHeaderV2TitleOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheaderv2-subheaderv2titleoptions-i.md) | Yes | Options for initializing the title. |

## id

```TypeScript
@Trace
  public id?: string
```

Set the id for the title.

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Title-@Trace  public id?: string--><!--Device-SubHeaderV2Title-@Trace  public id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@Trace
  public primaryTitle?: ResourceStr
```

Primary title.

When **primaryTitle**, **secondaryTitle**, and **icon** are used simultaneously in [SubHeaderV2](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheaderv2-subheaderv2-s.md), **primaryTitle** does not take effect.

Default value: **undefined**

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Title-@Trace  public primaryTitle?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  public primaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitleModifier

```TypeScript
@Trace
  public primaryTitleModifier?: TextModifier
```

Text attributes of the primary title, such as the font color, font size, and font weight.

Default value: **undefined**

Decorator: @Trace

**Type:** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Title-@Trace  public primaryTitleModifier?: TextModifier--><!--Device-SubHeaderV2Title-@Trace  public primaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@Trace
  public secondaryTitle?: ResourceStr
```

Secondary title.

Default value: **undefined**

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Title-@Trace  public secondaryTitle?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  public secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitleModifier

```TypeScript
@Trace
  public secondaryTitleModifier?: TextModifier
```

Text attributes of the secondary title, such as the font color, font size, and font weight.

Default value: **undefined**

Decorator: @Trace

**Type:** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Title-@Trace  public secondaryTitleModifier?: TextModifier--><!--Device-SubHeaderV2Title-@Trace  public secondaryTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleAccessibilityText

```TypeScript
@Trace
  public titleAccessibilityText?: ResourceStr
```

Customized content to be read in the title.

Default value: **undefined**

If the value is **undefined**, the title content displayed by the component is read by default.

Decorator: @Trace

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubHeaderV2Title-@Trace  public titleAccessibilityText?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  public titleAccessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

