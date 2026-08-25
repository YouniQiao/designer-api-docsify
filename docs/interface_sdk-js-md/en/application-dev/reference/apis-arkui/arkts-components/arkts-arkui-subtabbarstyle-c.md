# SubTabBarStyle

Implements the subtab style. A transition animation is played when the user switches between tabs.

**Since:** 9

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## board

```TypeScript
board(value: BoardStyle): SubTabBarStyle
```

Sets the background style (board style) of the selected subtab. It takes effect only in the horizontal layout.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BoardStyle](arkts-arkui-boardstyle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## constructor

```TypeScript
constructor(content: ResourceStr)
```

Constructor used to create a **SubTabBarStyle** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

## constructor

```TypeScript
constructor(content: ResourceStr | ComponentContent)
```

Constructor used to create a **SubTabBarStyle** instance. You can set custom content with **ComponentContent**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | Yes |

## id

```TypeScript
id(value: string): SubTabBarStyle
```

Sets the ID of the subtab.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## indicator

```TypeScript
indicator(value: IndicatorStyle): SubTabBarStyle
```

Sets the indicator style of the selected subtab. It takes effect only in the horizontal layout.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## indicator

```TypeScript
indicator(value: IndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle
```

Sets the indicator style of the selected subtab. Compared with [indicator](#indicator), the image format is added. For details about the display effect of the image, see [ImageFit.Cover](../arkts-apis/arkts-arkui-imagefit-e.md). It takes effect only in the horizontal layout.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [IndicatorStyle](arkts-arkui-indicatorstyle-i.md) \| [DrawableTabBarIndicator](arkts-arkui-drawabletabbarindicator-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## labelStyle

```TypeScript
labelStyle(value: LabelStyle): SubTabBarStyle
```

Sets the style of the label text and font for the subtab.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LabelStyle](arkts-arkui-labelstyle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## of

```TypeScript
static of(content: ResourceStr): SubTabBarStyle
```

Static constructor used to create a **SubTabBarStyle** instance.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## of

```TypeScript
static of(content: ResourceStr | ComponentContent): SubTabBarStyle
```

Static constructor used to create a **SubTabBarStyle** instance. You can set custom content with **ComponentContent**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## padding

```TypeScript
padding(value: Padding | Dimension): SubTabBarStyle
```

Sets the padding of the subtab. It cannot be set in percentage. When the parameter is of the Dimension type, the value applies to all sides.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Padding \| [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## padding

```TypeScript
padding(padding: LocalizedPadding): SubTabBarStyle
```

Sets the padding of the subtab. This API supports mirroring but does not support percentage-based settings.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [padding](#padding) | [LocalizedPadding](../arkts-apis/arkts-arkui-localizedpadding-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |

## selectedMode

```TypeScript
selectedMode(value: SelectedMode): SubTabBarStyle
```

Sets the display mode of the selected subtab. It takes effect only in the horizontal layout.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SelectedMode](arkts-arkui-selectedmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubTabBarStyle](arkts-arkui-subtabbarstyle-c.md) |
