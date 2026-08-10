# StringConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## fromCodePoint

```TypeScript
fromCodePoint(...codePoints: number[]): string
```

Return the String value whose elements are, in order, the elements in the List elements.If length is 0, the empty string is returned.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-StringConstructor-fromCodePoint(...codePoints: number[]): string--><!--Device-StringConstructor-fromCodePoint(...codePoints: number[]): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| codePoints | number[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## raw

```TypeScript
raw(template: { raw: readonly string[] | ArrayLike<string>}, ...substitutions: any[]): string
```

String.raw is usually used as a tag function of a Tagged Template String. When called as such, the first argument will be a well formed template call site object and the rest parameter will contain the substitution values. It can also be called directly, for example,to interleave strings and values from your own tag function, and in this case the only thing it needs from the first argument is the raw property.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-StringConstructor-raw(template: { raw: readonly string[] | ArrayLike<string>}, ...substitutions: any[]): string--><!--Device-StringConstructor-raw(template: { raw: readonly string[] | ArrayLike<string>}, ...substitutions: any[]): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| template | { raw: readonly string[] \| ArrayLike&lt;string&gt;} | 是 |  |
| substitutions | any[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

