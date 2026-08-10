# String

**ArkTS模式：** 仅支持ArkTS-Dyn

## replaceAll

```TypeScript
replaceAll(searchValue: string | RegExp, replaceValue: string): string
```

Replace all instances of a substring in a string, using a regular expression or search string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-replaceAll(searchValue: string | RegExp, replaceValue: string): string--><!--Device-String-replaceAll(searchValue: string | RegExp, replaceValue: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | 是 |  |
| replaceValue | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## replaceAll

```TypeScript
replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string
```

Replace all instances of a substring in a string, using a regular expression or search string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-String-replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | 是 |  |
| replacer | (substring: string, ...args: any[]) =&gt; string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

