# String

**ArkTS模式：** 仅支持ArkTS-Dyn

## anchor

```TypeScript
anchor(name: string): string
```

Returns an `&lt;a&gt;` HTML anchor element and sets the name attribute to the text value

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-anchor(name: string): string--><!--Device-String-anchor(name: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## big

```TypeScript
big(): string
```

Returns a `&lt;big&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-big(): string--><!--Device-String-big(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## blink

```TypeScript
blink(): string
```

Returns a `&lt;blink&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-blink(): string--><!--Device-String-blink(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## bold

```TypeScript
bold(): string
```

Returns a `&lt;b&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-bold(): string--><!--Device-String-bold(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## codePointAt

```TypeScript
codePointAt(pos: number): number | undefined
```

Returns a nonnegative integer Number less than 1114112 (0x110000) that is the code point value of the UTF-16 encoded code point starting at the string element at position pos in the String resulting from converting this object to a String.If there is no element at that position, the result is undefined.If a valid UTF-16 surrogate pair does not begin at pos, the result is the code unit at pos.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-codePointAt(pos: number): number | undefined--><!--Device-String-codePointAt(pos: number): number | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## endsWith

```TypeScript
endsWith(searchString: string, endPosition?: number): boolean
```

Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at endPosition – length(this). Otherwise returns false.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-endsWith(searchString: string, endPosition?: number): boolean--><!--Device-String-endsWith(searchString: string, endPosition?: number): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 |  |
| endPosition | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## fixed

```TypeScript
fixed(): string
```

Returns a `&lt;tt&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-fixed(): string--><!--Device-String-fixed(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## fontcolor

```TypeScript
fontcolor(color: string): string
```

Returns a `&lt;font&gt;` HTML element and sets the color attribute value

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-fontcolor(color: string): string--><!--Device-String-fontcolor(color: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## fontsize

```TypeScript
fontsize(size: number): string
```

Returns a `&lt;font&gt;` HTML element and sets the size attribute value

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-fontsize(size: number): string--><!--Device-String-fontsize(size: number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## fontsize

```TypeScript
fontsize(size: string): string
```

Returns a `&lt;font&gt;` HTML element and sets the size attribute value

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-fontsize(size: string): string--><!--Device-String-fontsize(size: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## includes

```TypeScript
includes(searchString: string, position?: number): boolean
```

Returns true if searchString appears as a substring of the result of converting this object to a String, at one or more positions that are greater than or equal to position; otherwise, returns false.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-includes(searchString: string, position?: number): boolean--><!--Device-String-includes(searchString: string, position?: number): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 |  |
| position | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## italics

```TypeScript
italics(): string
```

Returns an `&lt;i&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-italics(): string--><!--Device-String-italics(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## link

```TypeScript
link(url: string): string
```

Returns an `&lt;a&gt;` HTML element and sets the href attribute value

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-link(url: string): string--><!--Device-String-link(url: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## normalize

```TypeScript
normalize(form: "NFC" | "NFD" | "NFKC" | "NFKD"): string
```

Returns the String value result of normalizing the string into the normalization form named by form as specified in Unicode Standard Annex #15, Unicode Normalization Forms.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-normalize(form: "NFC" | "NFD" | "NFKC" | "NFKD"): string--><!--Device-String-normalize(form: "NFC" | "NFD" | "NFKC" | "NFKD"): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| form | "NFC" \| "NFD" \| "NFKC" \| "NFKD" | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## normalize

```TypeScript
normalize(form?: string): string
```

Returns the String value result of normalizing the string into the normalization form named by form as specified in Unicode Standard Annex #15, Unicode Normalization Forms.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-normalize(form?: string): string--><!--Device-String-normalize(form?: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| form | string | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## repeat

```TypeScript
repeat(count: number): string
```

Returns a String value that is made from count copies appended together. If count is 0,the empty string is returned.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-repeat(count: number): string--><!--Device-String-repeat(count: number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## small

```TypeScript
small(): string
```

Returns a `&lt;small&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-small(): string--><!--Device-String-small(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## startsWith

```TypeScript
startsWith(searchString: string, position?: number): boolean
```

Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at position. Otherwise returns false.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-startsWith(searchString: string, position?: number): boolean--><!--Device-String-startsWith(searchString: string, position?: number): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 |  |
| position | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## strike

```TypeScript
strike(): string
```

Returns a `&lt;strike&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-strike(): string--><!--Device-String-strike(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## sub

```TypeScript
sub(): string
```

Returns a `&lt;sub&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-sub(): string--><!--Device-String-sub(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## sup

```TypeScript
sup(): string
```

Returns a `&lt;sup&gt;` HTML element

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-sup(): string--><!--Device-String-sup(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

