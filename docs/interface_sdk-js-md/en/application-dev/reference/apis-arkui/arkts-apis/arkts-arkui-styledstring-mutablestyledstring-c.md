# MutableStyledString

MutableStyledString

**Inheritance/Implementation:** MutableStyledString extends [StyledString](arkts-arkui-styledstring-styledstring-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class MutableStyledString extends StyledString--><!--Device-unnamed-export declare class MutableStyledString extends StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appendStyledString

```TypeScript
appendStyledString(other: StyledString): void
```

Append new StyledString at the end.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-appendStyledString(other: StyledString): void--><!--Device-MutableStyledString-appendStyledString(other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes | new StyledString. |

## clearStyles

```TypeScript
clearStyles(): void
```

Delete all attributes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-clearStyles(): void--><!--Device-MutableStyledString-clearStyles(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)--><!--Device-MutableStyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| ImageAttachment \| CustomSpan | Yes | indicates the current object value of the MutableStyledString. |
| styles | Array&lt;StyleOptions&gt; | No | indicates the SpanStyle objects. |

## insertString

```TypeScript
insertString(start: int, other: string): void
```

Insert the string at the specified location.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-insertString(start: int, other: string): void--><!--Device-MutableStyledString-insertString(start: int, other: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the insertedString. |
| other | string | Yes | must be unicode string. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## insertStyledString

```TypeScript
insertStyledString(start: int, other: StyledString): void
```

Insert new StyledString at the specified location.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-insertStyledString(start: int, other: StyledString): void--><!--Device-MutableStyledString-insertStyledString(start: int, other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the insertedStyledString. |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes | new StyledString. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## removeString

```TypeScript
removeString(start: int, length: int): void
```

Remove the string of the specified range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-removeString(start: int, length: int): void--><!--Device-MutableStyledString-removeString(start: int, length: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the removedString. |
| length | int | Yes | the length of the removedString's characters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## removeStyle

```TypeScript
removeStyle(start: int, length: int, styledKey: StyledStringKey): void
```

Delete the specified type attributes for the specified range string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-removeStyle(start: int, length: int, styledKey: StyledStringKey): void--><!--Device-MutableStyledString-removeStyle(start: int, length: int, styledKey: StyledStringKey): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the removedAttributeStyledString. |
| length | int | Yes | the length of the removedAttributeStyledString's characters. |
| styledKey | [StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md) | Yes | the specified attribute type's key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## removeStyles

```TypeScript
removeStyles(start: int, length: int): void
```

Delete all attributes for the specified range styledString.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-removeStyles(start: int, length: int): void--><!--Device-MutableStyledString-removeStyles(start: int, length: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the attributeRemovedStyledString's characters. |
| length | int | Yes | the length of the attributeRemovedStyledString's characters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## replaceString

```TypeScript
replaceString(start: int, length: int, other: string): void
```

Replace the string of the specified range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-replaceString(start: int, length: int, other: string): void--><!--Device-MutableStyledString-replaceString(start: int, length: int, other: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the replacedString. |
| length | int | Yes | the length of the replacedString's characters. |
| other | string | Yes | must be unicode string. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## replaceStyle

```TypeScript
replaceStyle(spanStyle: SpanStyle): void
```

Replace the specified range string attribute.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-styledstring-spanstyle-i.md) | Yes | the SpanStyle Object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## replaceStyledString

```TypeScript
replaceStyledString(start: int, length: int, other: StyledString): void
```

Replace the StyledString of the specified range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-replaceStyledString(start: int, length: int, other: StyledString): void--><!--Device-MutableStyledString-replaceStyledString(start: int, length: int, other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the replacedStyledString. |
| length | int | Yes | the length of the replacedStyledString's characters. |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes | new StyledString. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## setStyle

```TypeScript
setStyle(spanStyle: SpanStyle): void
```

Add attributes to the specified range string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-styledstring-spanstyle-i.md) | Yes | the SpanStyle Object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. |

