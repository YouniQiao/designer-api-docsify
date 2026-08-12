# StyledString

StyledString

**Since:** 12

<!--Device-unnamed-declare class StyledString--><!--Device-unnamed-declare class StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)
```

A constructor used to create a styled string.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)--><!--Device-StyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [ImageAttachment](arkts-arkui-imageattachment-c.md) \| [CustomSpan](arkts-arkui-customspan-c.md) | Yes |
| styles | Array&lt;[StyleOptions](arkts-arkui-styleoptions-i.md)&gt; | No |

## equals

```TypeScript
equals(other: StyledString): boolean
```

Checks whether this styled string the same as another styled string.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledString-equals(other: StyledString): boolean--><!--Device-StyledString-equals(other: StyledString): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## fromHtml

```TypeScript
static fromHtml(html: string): Promise<StyledString>
```

Converts an HTML string into a styled string. Currently, the following HTML tags are supported for conversion: \&lt;p&gt;, \&lt;span&gt;, \&lt;img&gt;, \

, \&lt;strong&gt;, \&lt;b&gt;, \&lt;a&gt;, \&lt;i&gt;, \&lt;em&gt;, \&lt;s&gt;, \&lt;u&gt;, \&lt;del&gt;, \&lt;sup&gt;, \&lt;sub&gt;. The **style** attribute within tags can be converted to the corresponding style in the styled string.

For details about how to use this API, see  
[Example 12: Implementing Conversion Using fromHtml and toHtml](../../../reference/apis-arkui/arkui-ts/ts-universal-styled-string.md#example-12-implementing-conversion-using-fromhtml-and-tohtml).

| Tag Name| Description |
| ------------- | ---------------------------- |
| \ & lt;p\ & gt; | Paragraph tag, which separates text into paragraphs. |
| \ & lt;span\ & gt; | Inline text supporting style configuration. |
| \ & lt;img\ & gt; | Image tag, used to insert an image. |
| \ & lt;strong\ & gt; | Bold text tag. |
|  & lt;br & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Line break tag. |
| \ & lt;b\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Bold text tag. |
| \ & lt;a\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Hyperlink tag. |
| \ & lt;i\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Italic text tag. |
| \ & lt;em\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Italic text tag. |
| \ & lt;s\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Strikethrough tag, which adds a line through the text. |
| \ & lt;u\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Underline tag, which adds a decorative underline to the text. |
| \ & lt;del\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Strikethrough tag, which adds a line through the text. |
| \ & lt;sup\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; | Superscript tag. |
| \ & lt;sub\ & gt; & lt;sup & gt;20+ & lt;/sup & gt; |

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledString-static fromHtml(html: string): Promise<StyledString>--><!--Device-StyledString-static fromHtml(html: string): Promise<StyledString>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| html | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [170001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-styled-string.md#170001-conversion-error) |

## getString

```TypeScript
getString(): string
```

Obtains the text of this styled string.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledString-getString(): string--><!--Device-StyledString-getString(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getStyles

```TypeScript
getStyles(start: number, length: number, styledKey?: StyledStringKey): Array<SpanStyle>
```

Obtains the styles in the specified range of a styled string. The specified range must not exceed the string's length.

This API returns only styles explicitly set by the developer.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledString-getStyles(start: number, length: number, styledKey?: StyledStringKey): Array<SpanStyle>--><!--Device-StyledString-getStyles(start: number, length: number, styledKey?: StyledStringKey): Array<SpanStyle>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| [length](#length) | number | Yes |
| styledKey | [StyledStringKey](arkts-arkui-styledstringkey-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[SpanStyle](arkts-arkui-spanstyle-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## subStyledString

```TypeScript
subStyledString(start: number, length?: number): StyledString
```

Obtains a substring of this styled string. The specified range must not exceed the string's length.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledString-subStyledString(start: number, length?: number): StyledString--><!--Device-StyledString-subStyledString(start: number, length?: number): StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| [length](#length) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StyledString](arkts-arkui-styledstring-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## toHtml

```TypeScript
static toHtml(styledString: StyledString): string
```

Converts a styled string into an HTML-formatted string. The supported styled string keys for conversion, as detailed in [StyledStringKey](arkts-arkui-styledstringkey-e.md#StyledStringKey), include: **StyledStringKey.FONT**,  
**StyledStringKey.DECORATION**, **StyledStringKey.LETTER_SPACING**, **StyledStringKey.TEXT_SHADOW**,  
**StyledStringKey.LINE_HEIGHT**, and **StyledStringKey.IMAGE**.

For details about how to use this API, see  
[Example 12: Implementing Conversion Using fromHtml and toHtml](../../../reference/apis-arkui/arkui-ts/ts-universal-styled-string.md#example-12-implementing-conversion-using-fromhtml-and-tohtml).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-StyledString-static toHtml(styledString: StyledString): string--><!--Device-StyledString-static toHtml(styledString: StyledString): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## length

```TypeScript
readonly length: number
```

Length of the styled string.

**NOTE：**

Both **ImageAttachment** and **CustomSpan** in the styled string are counted as length 1.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyledString-readonly length: number--><!--Device-StyledString-readonly length: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
