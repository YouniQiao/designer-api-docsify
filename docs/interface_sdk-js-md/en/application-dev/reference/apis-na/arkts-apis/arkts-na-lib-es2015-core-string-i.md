# String

**Since:** -1

<!--Device-unnamed-interface String--><!--Device-unnamed-interface String-End-->

## anchor

```TypeScript
anchor(name: string): string
```

Returns an `&lt;a&gt;` HTML anchor element and sets the name attribute to the text value

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-anchor(name: string): string--><!--Device-String-anchor(name: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## big

```TypeScript
big(): string
```

Returns a `&lt;big&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-big(): string--><!--Device-String-big(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## blink

```TypeScript
blink(): string
```

Returns a `&lt;blink&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-blink(): string--><!--Device-String-blink(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## bold

```TypeScript
bold(): string
```

Returns a `&lt;b&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-bold(): string--><!--Device-String-bold(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## codePointAt

```TypeScript
codePointAt(pos: number): number | undefined
```

Returns a nonnegative integer Number less than 1114112 (0x110000) that is the code point value of the UTF-16 encoded code point starting at the string element at position pos in the String resulting from converting this object to a String. If there is no element at that position, the result is undefined. If a valid UTF-16 surrogate pair does not begin at pos, the result is the code unit at pos.

**Since:** -1

<!--Device-String-codePointAt(pos: number): number | undefined--><!--Device-String-codePointAt(pos: number): number | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## endsWith

```TypeScript
endsWith(searchString: string, endPosition?: number): boolean
```

Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at endPosition – length(this). Otherwise returns false.

**Since:** -1

<!--Device-String-endsWith(searchString: string, endPosition?: number): boolean--><!--Device-String-endsWith(searchString: string, endPosition?: number): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchString | string | Yes |  |
| endPosition | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## fixed

```TypeScript
fixed(): string
```

Returns a `&lt;tt&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-fixed(): string--><!--Device-String-fixed(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## fontcolor

```TypeScript
fontcolor(color: string): string
```

Returns a `&lt;font&gt;` HTML element and sets the color attribute value

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-fontcolor(color: string): string--><!--Device-String-fontcolor(color: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## fontsize

```TypeScript
fontsize(size: number): string
```

Returns a `&lt;font&gt;` HTML element and sets the size attribute value

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-fontsize(size: number): string--><!--Device-String-fontsize(size: number): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## fontsize

```TypeScript
fontsize(size: string): string
```

Returns a `&lt;font&gt;` HTML element and sets the size attribute value

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-fontsize(size: string): string--><!--Device-String-fontsize(size: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## includes

```TypeScript
includes(searchString: string, position?: number): boolean
```

Returns true if searchString appears as a substring of the result of converting this object to a String, at one or more positions that are greater than or equal to position; otherwise, returns false.

**Since:** -1

<!--Device-String-includes(searchString: string, position?: number): boolean--><!--Device-String-includes(searchString: string, position?: number): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchString | string | Yes |  |
| position | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## italics

```TypeScript
italics(): string
```

Returns an `&lt;i&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-italics(): string--><!--Device-String-italics(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## link

```TypeScript
link(url: string): string
```

Returns an `&lt;a&gt;` HTML element and sets the href attribute value

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-link(url: string): string--><!--Device-String-link(url: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## normalize

```TypeScript
normalize(form: "NFC" | "NFD" | "NFKC" | "NFKD"): string
```

Returns the String value result of normalizing the string into the normalization form named by form as specified in Unicode Standard Annex #15, Unicode Normalization Forms.

**Since:** -1

<!--Device-String-normalize(form: "NFC" | "NFD" | "NFKC" | "NFKD"): string--><!--Device-String-normalize(form: "NFC" | "NFD" | "NFKC" | "NFKD"): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| form | "NFC" \| "NFD" \| "NFKC" \| "NFKD" | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## normalize

```TypeScript
normalize(form?: string): string
```

Returns the String value result of normalizing the string into the normalization form named by form as specified in Unicode Standard Annex #15, Unicode Normalization Forms.

**Since:** -1

<!--Device-String-normalize(form?: string): string--><!--Device-String-normalize(form?: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| form | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## repeat

```TypeScript
repeat(count: number): string
```

Returns a String value that is made from count copies appended together. If count is 0, the empty string is returned.

**Since:** -1

<!--Device-String-repeat(count: number): string--><!--Device-String-repeat(count: number): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## small

```TypeScript
small(): string
```

Returns a `&lt;small&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-small(): string--><!--Device-String-small(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## startsWith

```TypeScript
startsWith(searchString: string, position?: number): boolean
```

Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at position. Otherwise returns false.

**Since:** -1

<!--Device-String-startsWith(searchString: string, position?: number): boolean--><!--Device-String-startsWith(searchString: string, position?: number): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchString | string | Yes |  |
| position | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## strike

```TypeScript
strike(): string
```

Returns a `&lt;strike&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-strike(): string--><!--Device-String-strike(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## sub

```TypeScript
sub(): string
```

Returns a `&lt;sub&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-sub(): string--><!--Device-String-sub(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## sup

```TypeScript
sup(): string
```

Returns a `&lt;sup&gt;` HTML element

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-sup(): string--><!--Device-String-sup(): string-End-->

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

