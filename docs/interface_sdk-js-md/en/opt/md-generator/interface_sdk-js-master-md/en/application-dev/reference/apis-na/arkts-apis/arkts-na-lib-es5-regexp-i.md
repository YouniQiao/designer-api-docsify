# RegExp

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface RegExp--><!--Device-unnamed-interface RegExp-End-->

## compile

```TypeScript
compile(pattern: string, flags?: string): this
```

**Since:** -1

**Deprecated since:** legacy feature for browser compatibility

<!--Device-RegExp-compile(pattern: string, flags?: string): this--><!--Device-RegExp-compile(pattern: string, flags?: string): this-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | string | Yes |
| flags | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## exec

```TypeScript
exec(string: string): RegExpExecArray | null
```

Executes a search on a string using a regular expression pattern, and returns an array containing the results of that search.

**Since:** -1

**Deprecated since:** -1

<!--Device-RegExp-exec(string: string): RegExpExecArray | null--><!--Device-RegExp-exec(string: string): RegExpExecArray | null-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| string | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RegExpExecArray](arkts-na-lib-es5-regexpexecarray-i.md) |

## test

```TypeScript
test(string: string): boolean
```

Returns a Boolean value that indicates whether or not a pattern exists in a searched string.

**Since:** -1

**Deprecated since:** -1

<!--Device-RegExp-test(string: string): boolean--><!--Device-RegExp-test(string: string): boolean-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| string | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## global

```TypeScript
readonly global: boolean
```

Returns a Boolean value indicating the state of the global flag (g) used with a regular expression. Default is false. Read-only.

**Type:** boolean

**Since:** -1

**Deprecated since:** -1

<!--Device-RegExp-readonly global: boolean--><!--Device-RegExp-readonly global: boolean-End-->

## ignoreCase

```TypeScript
readonly ignoreCase: boolean
```

Returns a Boolean value indicating the state of the ignoreCase flag (i) used with a regular expression. Default is false. Read-only.

**Type:** boolean

**Since:** -1

**Deprecated since:** -1

<!--Device-RegExp-readonly ignoreCase: boolean--><!--Device-RegExp-readonly ignoreCase: boolean-End-->

## lastIndex

```TypeScript
lastIndex: number
```

**Type:** number

**Since:** -1

**Deprecated since:** -1

<!--Device-RegExp-lastIndex: number--><!--Device-RegExp-lastIndex: number-End-->

## multiline

```TypeScript
readonly multiline: boolean
```

Returns a Boolean value indicating the state of the multiline flag (m) used with a regular expression. Default is false. Read-only.

**Type:** boolean

**Since:** -1

**Deprecated since:** -1

<!--Device-RegExp-readonly multiline: boolean--><!--Device-RegExp-readonly multiline: boolean-End-->

## source

```TypeScript
readonly source: string
```

Returns a copy of the text of the regular expression pattern. Read-only. The regExp argument is a Regular expression object. It can be a variable name or a literal.

**Type:** string

**Since:** -1

**Deprecated since:** -1

<!--Device-RegExp-readonly source: string--><!--Device-RegExp-readonly source: string-End-->
