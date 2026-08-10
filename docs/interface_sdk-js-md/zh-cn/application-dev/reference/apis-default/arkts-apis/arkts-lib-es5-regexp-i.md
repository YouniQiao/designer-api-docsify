# RegExp

**ArkTS模式：** 仅支持ArkTS-Dyn

## compile

```TypeScript
compile(pattern: string, flags?: string): this
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility 

<!--Device-RegExp-compile(pattern: string, flags?: string): this--><!--Device-RegExp-compile(pattern: string, flags?: string): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | string | 是 |  |
| flags | string | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## exec

```TypeScript
exec(string: string): RegExpExecArray | null
```

Executes a search on a string using a regular expression pattern, and returns an array containing the results of that search.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-exec(string: string): RegExpExecArray | null--><!--Device-RegExp-exec(string: string): RegExpExecArray | null-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| string | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpExecArray](../../apis-arkts/arkts-apis/arkts-arkts-regexp-regexpexecarray-c.md) |  |

## test

```TypeScript
test(string: string): boolean
```

Returns a Boolean value that indicates whether or not a pattern exists in a searched string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-test(string: string): boolean--><!--Device-RegExp-test(string: string): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| string | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## global

```TypeScript
readonly global: boolean
```

Returns a Boolean value indicating the state of the global flag (g) used with a regular expression. Default is false. Read-only.

**类型：** boolean

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-readonly global: boolean--><!--Device-RegExp-readonly global: boolean-End-->

## ignoreCase

```TypeScript
readonly ignoreCase: boolean
```

Returns a Boolean value indicating the state of the ignoreCase flag (i) used with a regular expression. Default is false. Read-only.

**类型：** boolean

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-readonly ignoreCase: boolean--><!--Device-RegExp-readonly ignoreCase: boolean-End-->

## lastIndex

```TypeScript
lastIndex: number
```

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

## multiline

```TypeScript
readonly multiline: boolean
```

Returns a Boolean value indicating the state of the multiline flag (m) used with a regular expression. Default is false. Read-only.

**类型：** boolean

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-readonly multiline: boolean--><!--Device-RegExp-readonly multiline: boolean-End-->

## source

```TypeScript
readonly source: string
```

Returns a copy of the text of the regular expression pattern. Read-only. The regExp argument is a Regular expression object. It can be a variable name or a literal.

**类型：** string

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-readonly source: string--><!--Device-RegExp-readonly source: string-End-->

