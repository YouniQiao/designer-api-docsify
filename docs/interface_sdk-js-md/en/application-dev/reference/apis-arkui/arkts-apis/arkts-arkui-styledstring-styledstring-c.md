# StyledString

StyledString

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class StyledString--><!--Device-unnamed-export declare class StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)--><!--Device-StyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| [ImageAttachment](arkts-arkui-styledstring-imageattachment-c.md) \| [CustomSpan](arkts-arkui-styledstring-customspan-c.md) | Yes | indicates the current object value of the StyledString. |
| styles | Array&lt;[StyleOptions](arkts-arkui-styledstring-styleoptions-i.md)&gt; | No | indicates the SpanStyle objects. |

## equals

```TypeScript
equals(other: StyledString): boolean
```

Judge if two attribute strings are equal.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-equals(other: StyledString): boolean--><!--Device-StyledString-equals(other: StyledString): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | Yes | another StyledString. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## fromHtml

```TypeScript
static fromHtml(html: string): Promise<StyledString | undefined>
```

Returns StyledString from the provided HTML string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static fromHtml(html: string): Promise<StyledString | undefined>--><!--Device-StyledString-static fromHtml(html: string): Promise<StyledString | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| html | string | Yes | the html text will be converted to a StyledString. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-styledstring-c.md) \| undefined&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [170001](../errorcode-styled-string.md#170001-conversion-error) | Convert Error. |

## getString

```TypeScript
getString(): string
```

Get the literal content of the StyledString.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-getString(): string--><!--Device-StyledString-getString(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | the literal content of the StyledString |

## getStyles

```TypeScript
getStyles(start: int, length: int, styledKey?: StyledStringKey): Array<SpanStyle> | undefined
```

Get the attribute objects of the subStyledString.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-getStyles(start: int, length: int, styledKey?: StyledStringKey): Array<SpanStyle> | undefined--><!--Device-StyledString-getStyles(start: int, length: int, styledKey?: StyledStringKey): Array<SpanStyle> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the subStyledString. |
| length | int | Yes | the length of the subStyledString's characters. |
| styledKey | [StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md) | No | the specified type. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[SpanStyle](arkts-arkui-styledstring-spanstyle-i.md)&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## subStyledString

```TypeScript
subStyledString(start: int, length?: int): StyledString | undefined
```

Get the substring of the StyledString.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-subStyledString(start: int, length?: int): StyledString | undefined--><!--Device-StyledString-subStyledString(start: int, length?: int): StyledString | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | the start position of the subStyledString. |
| length | int | No | the length of the subStyledString's characters. |

**Return value:**

| Type | Description |
| --- | --- |
| [StyledString](arkts-arkui-styledstring-styledstring-c.md) |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## toHtml

```TypeScript
static toHtml(styledString: StyledString): string
```

Returns HTML string from the provided StyledString.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static toHtml(styledString: StyledString): string--><!--Device-StyledString-static toHtml(styledString: StyledString): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | Yes | the StyledString will be converted to a HTML string. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the HTML string converted from the provided StyledString. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

