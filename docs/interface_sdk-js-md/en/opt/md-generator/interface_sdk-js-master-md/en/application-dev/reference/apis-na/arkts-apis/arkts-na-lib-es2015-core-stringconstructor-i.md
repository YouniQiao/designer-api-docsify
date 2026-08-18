# StringConstructor

**Since:** -1

<!--Device-unnamed-interface StringConstructor--><!--Device-unnamed-interface StringConstructor-End-->

## Modules to Import

```TypeScript
```

## fromCodePoint

```TypeScript
fromCodePoint(...codePoints: number[]): string
```

Return the String value whose elements are, in order, the elements in the List elements. If length is 0, the empty string is returned.

**Since:** -1

<!--Device-StringConstructor-fromCodePoint(...codePoints: number[]): string--><!--Device-StringConstructor-fromCodePoint(...codePoints: number[]): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| codePoints | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## raw

```TypeScript
raw(template: { raw: readonly string[] | ArrayLike<string>}, ...substitutions: any[]): string
```

String.raw is usually used as a tag function of a Tagged Template String. When called as such, the first argument will be a well formed template call site object and the rest parameter will contain the substitution values. It can also be called directly, for example, to interleave strings and values from your own tag function, and in this case the only thing it needs from the first argument is the raw property.

**Since:** -1

<!--Device-StringConstructor-raw(template: { raw: readonly string[] | ArrayLike<string>}, ...substitutions: any[]): string--><!--Device-StringConstructor-raw(template: { raw: readonly string[] | ArrayLike<string>}, ...substitutions: any[]): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| template | { raw: readonly string[] \| [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;string&gt;} | Yes |
| substitutions | any[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
