# MutableStyledString

Inherits from the [StyledString](arkts-arkui-styledstring-c.md#StyledString) class. > **An exception is thrown in the following cases:** > > If the values of **start** and **length** are out of the acceptable range or if any mandatory parameter is passed > as **undefined**, an exception is thrown. > > **styledKey** or **styledValue** is set to an invalid value or they do not match.

**Inheritance/Implementation:** MutableStyledString extends [StyledString](arkts-arkui-styledstring-c.md#StyledString)

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-declare class MutableStyledString--><!--Device-unnamed-declare class MutableStyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appendStyledString

```TypeScript
appendStyledString(other: StyledString): void
```

Appends a styled string.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-appendStyledString(other: StyledString): void--><!--Device-MutableStyledString-appendStyledString(other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes |

## clearStyles

```TypeScript
clearStyles(): void
```

Removes all styles of this styled string. After a style is removed, the value set for the corresponding style attribute in the Text component is used. If the value is not set, the default value is used.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-clearStyles(): void--><!--Device-MutableStyledString-clearStyles(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## insertString

```TypeScript
insertString(start: number, other: string): void
```

Inserts a string.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-insertString(start: number, other: string): void--><!--Device-MutableStyledString-insertString(start: number, other: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| other | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## insertStyledString

```TypeScript
insertStyledString(start: number, other: StyledString): void
```

Inserts a new styled string at the specified position.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-insertStyledString(start: number, other: StyledString): void--><!--Device-MutableStyledString-insertStyledString(start: number, other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## removeString

```TypeScript
removeString(start: number, length: number): void
```

Removes the string in the specified range of this styled string. This API equally works when the styled string contains an image or [CustomSpan](arkts-arkui-customspan-c.md#CustomSpan).

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-removeString(start: number, length: number): void--><!--Device-MutableStyledString-removeString(start: number, length: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| length | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## removeStyle

```TypeScript
removeStyle(start: number, length: number, styledKey: StyledStringKey): void
```

Removes the style for the specified range of this styled string. After a style is removed, the value set for the corresponding style attribute in the Text component is used. If the value is not set, the default value is used. This API equally works when the styled string contains an image.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-removeStyle(start: number, length: number, styledKey: StyledStringKey): void--><!--Device-MutableStyledString-removeStyle(start: number, length: number, styledKey: StyledStringKey): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| length | number | Yes |
| styledKey | [StyledStringKey](arkts-arkui-styledstringkey-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## removeStyles

```TypeScript
removeStyles(start: number, length: number): void
```

Removes all styles for the specified range of this styled string. After a style is removed, the value set for the corresponding style attribute in the Text component is used. If the value is not set, the default value is used. This API equally works when the styled string contains an image.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-removeStyles(start: number, length: number): void--><!--Device-MutableStyledString-removeStyles(start: number, length: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| length | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## replaceString

```TypeScript
replaceString(start: number, length: number, other: string): void
```

Replaces the string in the specified range of this styled string.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-replaceString(start: number, length: number, other: string): void--><!--Device-MutableStyledString-replaceString(start: number, length: number, other: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| length | number | Yes |
| other | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## replaceStyle

```TypeScript
replaceStyle(spanStyle: SpanStyle): void
```

Replaces the style in the specified range of this styled string.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-spanstyle-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## replaceStyledString

```TypeScript
replaceStyledString(start: number, length: number, other: StyledString): void
```

Replaces the styled string in the specified range.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-replaceStyledString(start: number, length: number, other: StyledString): void--><!--Device-MutableStyledString-replaceStyledString(start: number, length: number, other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| length | number | Yes |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setStyle

```TypeScript
setStyle(spanStyle: SpanStyle): void
```

Sets a new style for the specified range of this styled string.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-spanstyle-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
