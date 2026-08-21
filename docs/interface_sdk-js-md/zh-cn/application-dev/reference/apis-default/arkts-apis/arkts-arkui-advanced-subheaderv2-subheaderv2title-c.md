# SubHeaderV2Title

标题设置项。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class SubHeaderV2Title--><!--Device-unnamed-export declare class SubHeaderV2Title-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(options: SubHeaderV2TitleOptions)
```

标题内容信息SubHeaderV2Title构造函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Title-public constructor(options: SubHeaderV2TitleOptions)--><!--Device-SubHeaderV2Title-public constructor(options: SubHeaderV2TitleOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubHeaderV2TitleOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheaderv2-subheaderv2titleoptions-i.md) | 是 | 标题内容信息。 |

## id

```TypeScript
@Trace
  public id?: string
```

标题id。需要为标题设置id的时候设置此参数，缺省时不设置此参数。

默认值：undefined，表示不设置标题id。

**类型：** string

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Title-@Trace  public id?: string--><!--Device-SubHeaderV2Title-@Trace  public id?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@Trace
  public primaryTitle?: ResourceStr
```

标题内容。

当[SubHeaderV2](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheaderv2-subheaderv2-s.md)中同时使用primaryTitle、secondaryTitle、icon属性时，设置primaryTitle属性不生效。

默认值：undefined

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Title-@Trace  public primaryTitle?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  public primaryTitle?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryTitleModifier

```TypeScript
@Trace
  public primaryTitleModifier?: TextModifier
```

设置标题文本属性，如设置标题颜色、字体大小、字重等。

默认值：undefined

**类型：** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Title-@Trace  public primaryTitleModifier?: TextModifier--><!--Device-SubHeaderV2Title-@Trace  public primaryTitleModifier?: TextModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@Trace
  public secondaryTitle?: ResourceStr
```

副标题内容。

默认值：undefined

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Title-@Trace  public secondaryTitle?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  public secondaryTitle?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitleModifier

```TypeScript
@Trace
  public secondaryTitleModifier?: TextModifier
```

设置副标题文本属性，如设置副标题颜色、字体大小、字重等。

默认值：undefined

**类型：** [TextModifier](../../apis-arkui/arkts-apis/arkts-arkui-textmodifier-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Title-@Trace  public secondaryTitleModifier?: TextModifier--><!--Device-SubHeaderV2Title-@Trace  public secondaryTitleModifier?: TextModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## titleAccessibilityText

```TypeScript
@Trace
  public titleAccessibilityText?: ResourceStr
```

设置标题自定义朗读内容。

默认值：undefined

值为undefined时，默认朗读组件显示的标题内容。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Title-@Trace  public titleAccessibilityText?: ResourceStr--><!--Device-SubHeaderV2Title-@Trace  public titleAccessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

