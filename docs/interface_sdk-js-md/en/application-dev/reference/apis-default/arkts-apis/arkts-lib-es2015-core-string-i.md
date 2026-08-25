# String

**ArkTS mode:** 

## Modules to Import

```TypeScript
```

## anchor

```TypeScript
anchor(name: string): string
```

Returns an `&lt;a&gt;` HTML anchor element and sets the name attribute to the text value

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## big

```TypeScript
big(): string
```

Returns a `&lt;big&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## blink

```TypeScript
blink(): string
```

Returns a `&lt;blink&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## bold

```TypeScript
bold(): string
```

Returns a `&lt;b&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## codePointAt

```TypeScript
codePointAt(pos: number): number | undefined
```

Returns a nonnegative integer Number less than 1114112 (0x110000) that is the code point value of the UTF-16 encoded code point starting at the string element at position pos in the String resulting from converting this object to a String. If there is no element at that position, the result is undefined. If a valid UTF-16 surrogate pair does not begin at pos, the result is the code unit at pos.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## endsWith

```TypeScript
endsWith(searchString: string, endPosition?: number): boolean
```

Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at endPosition – length(this). Otherwise returns false.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchString | string | Yes |
| endPosition | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## fixed

```TypeScript
fixed(): string
```

Returns a `&lt;tt&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## fontcolor

```TypeScript
fontcolor(color: string): string
```

Returns a `&lt;font&gt;` HTML element and sets the color attribute value

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## fontsize

```TypeScript
fontsize(size: number): string
```

Returns a `&lt;font&gt;` HTML element and sets the size attribute value

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## fontsize

```TypeScript
fontsize(size: string): string
```

Returns a `&lt;font&gt;` HTML element and sets the size attribute value

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## includes

```TypeScript
includes(searchString: string, position?: number): boolean
```

Returns true if searchString appears as a substring of the result of converting this object to a String, at one or more positions that are greater than or equal to position; otherwise, returns false.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchString | string | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## italics

```TypeScript
italics(): string
```

Returns an `&lt;i&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## link

```TypeScript
link(url: string): string
```

Returns an `&lt;a&gt;` HTML element and sets the href attribute value

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## normalize

```TypeScript
normalize(form: "NFC" | "NFD" | "NFKC" | "NFKD"): string
```

Returns the String value result of normalizing the string into the normalization form named by form as specified in Unicode Standard Annex #15, Unicode Normalization Forms.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [form](../../apis-ability-kit/arkts-apis/arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | "NFC" \| "NFD" \| "NFKC" \| "NFKD" | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## normalize

```TypeScript
normalize(form?: string): string
```

Returns the String value result of normalizing the string into the normalization form named by form as specified in Unicode Standard Annex #15, Unicode Normalization Forms.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [form](../../apis-ability-kit/arkts-apis/arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## repeat

```TypeScript
repeat(count: number): string
```

Returns a String value that is made from count copies appended together. If count is 0, the empty string is returned.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## small

```TypeScript
small(): string
```

Returns a `&lt;small&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## startsWith

```TypeScript
startsWith(searchString: string, position?: number): boolean
```

Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at position. Otherwise returns false.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchString | string | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## strike

```TypeScript
strike(): string
```

Returns a `&lt;strike&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## sub

```TypeScript
sub(): string
```

Returns a `&lt;sub&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## sup

```TypeScript
sup(): string
```

Returns a `&lt;sup&gt;` HTML element

**ArkTS mode:** 

**Deprecated since:** legacy feature for browser compatibility

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
