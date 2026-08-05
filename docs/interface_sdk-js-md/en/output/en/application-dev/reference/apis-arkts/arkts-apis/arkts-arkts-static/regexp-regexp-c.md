# RegExp

Regular expression

**Inheritance/Implementation:** RegExp extends [Object](../../../apis-na/arkts-apis/arkts-na-dynamic/lib-es5-object-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export class RegExp extends Object--><!--Device-unnamed-export class RegExp extends Object-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
public static $_invoke(pattern: string, flags?: string): RegExp
```

RegExp constructor call signature, used to create new RegExp instances.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public static $_invoke(pattern: string, flags?: string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: string, flags?: string): RegExp-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | string | Yes | regular expression pattern. |
| flags | string | No | regular expression flags. |

**Return value:**

| Type | Description |
| --- | --- |
| RegExp | newly created RegExp instance. |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string, flags?: string): RegExp
```

RegExp constructor call signature, used to create new RegExp instances.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public static $_invoke(pattern: RegExp | string, flags?: string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: RegExp | string, flags?: string): RegExp-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | RegExp \| string | Yes | regular expression pattern or another RegExp instance. |
| flags | string | No | regular expression flags. |

**Return value:**

| Type | Description |
| --- | --- |
| RegExp | newly created RegExp instance. |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string): RegExp
```

RegExp constructor call signature, used to create new RegExp instances.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public static $_invoke(pattern: RegExp | string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: RegExp | string): RegExp-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | RegExp \| string | Yes | regular expression pattern or another RegExp instance. |

**Return value:**

| Type | Description |
| --- | --- |
| RegExp | newly created RegExp instance. |

## advanceStringIndex

```TypeScript
public static advanceStringIndex(s: string, index: int, unicode: boolean): int
```

Advances the string index according to the Unicode flag.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public static advanceStringIndex(s: string, index: int, unicode: boolean): int--><!--Device-RegExp-public static advanceStringIndex(s: string, index: int, unicode: boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| s | string | Yes | original string. |
| index | int | Yes | current index.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| unicode | boolean | Yes | whether to enable Unicode mode. |

**Return value:**

| Type | Description |
| --- | --- |
| int | next index. |

## constructor

```TypeScript
constructor(pattern: string, flags?: string)
```

Constructs a new RegExp using pattern and flags

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-constructor(pattern: string, flags?: string)--><!--Device-RegExp-constructor(pattern: string, flags?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | string | Yes | description of a pattern |
| flags | string | No | description of flags to be used |

## constructor

```TypeScript
constructor(regexp: RegExp, flags?: string)
```

Constructs a new RegExp by other RegExp. It uses other RegExp's flags if flags aren't provided

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-constructor(regexp: RegExp, flags?: string)--><!--Device-RegExp-constructor(regexp: RegExp, flags?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| regexp | RegExp | Yes | other regexp |
| flags | string | No | description of flags to be used |

## constructor

```TypeScript
constructor(regexp: RegExp | string, flags?: string)
```

Constructs a new RegExp by RegExp or string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-constructor(regexp: RegExp | string, flags?: string)--><!--Device-RegExp-constructor(regexp: RegExp | string, flags?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| regexp | RegExp \| string | Yes | The pattern of the regular expression or another RegExp instance. |
| flags | string | No | description of flags to be used. |

## exec

```TypeScript
public exec(str: string, index: int): RegExpExecArray | null
```

Executes a match search on the string starting from the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public exec(str: string, index: int): RegExpExecArray | null--><!--Device-RegExp-public exec(str: string, index: int): RegExpExecArray | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the string to match. |
| index | int | Yes | the index to start matching from.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | if match succeeds, returns an array containing match results, |

## exec

```TypeScript
public exec(str: string): RegExpExecArray | null
```

Executes a search for a match in a specified string and returns a result array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public exec(str: string): RegExpExecArray | null--><!--Device-RegExp-public exec(str: string): RegExpExecArray | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the string to match. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | if match succeeds, returns an array containing match results, |

## match

```TypeScript
public match(str: string): RegExpMatchArray | null
```

Searches the string for matches and returns all matches as an array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public match(str: string): RegExpMatchArray | null--><!--Device-RegExp-public match(str: string): RegExpMatchArray | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the string to match. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | if matches are found, returns an array containing all matches, |

## matchAll

```TypeScript
public matchAll(str: string): IterableIterator<RegExpMatchArray>
```

Returns an iterator that iterates over all matches in the string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public matchAll(str: string): IterableIterator<RegExpMatchArray>--><!--Device-RegExp-public matchAll(str: string): IterableIterator<RegExpMatchArray>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the string to match. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | an iterator that iterates over all match results. |

## replace

```TypeScript
public replace(str: string, replaceValue: string): string
```

Replaces matched substrings in the string using a replacement string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public replace(str: string, replaceValue: string): string--><!--Device-RegExp-public replace(str: string, replaceValue: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the original string. |
| replaceValue | string | Yes | the string used for replacement. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the new string after replacement. |

## replace

```TypeScript
public replace(str: string, replacer: (substr: string, args: Object[]) => string): string
```

Replaces matched substrings in the string using a function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public replace(str: string, replacer: (substr: string, args: Object[]) => string): string--><!--Device-RegExp-public replace(str: string, replacer: (substr: string, args: Object[]) => string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the original string. |
| replacer | (substr: string, args: Object[]) =&gt; string | Yes | a function used to generate new substrings. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the new string after replacement. |

## search

```TypeScript
public search(str: string): int
```

Searches for matches in the string and returns the starting index of the match.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public search(str: string): int--><!--Device-RegExp-public search(str: string): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the string to search. |

**Return value:**

| Type | Description |
| --- | --- |
| int | if a match is found, returns its starting index; otherwise returns -1. |

## split

```TypeScript
public split(str: string, limit: Int | undefined): string[]
```

Splits the string into an array of substrings using the regular expression.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public split(str: string, limit: Int | undefined): string[]--><!--Device-RegExp-public split(str: string, limit: Int | undefined): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the string to split. |
| limit | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | limits the maximum length of the returned array. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | the array of substrings after splitting. |

## test

```TypeScript
public test(str: string): boolean
```

Executes a search for a match between a regular expression and specified string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public test(str: string): boolean--><!--Device-RegExp-public test(str: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| str | string | Yes | the string against which to match the regular expression. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | if the string has matches, returns true; otherwise returns false. |

## toString

```TypeScript
public toString(): string
```

Returns a string representing the regular expression.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-public toString(): string--><!--Device-RegExp-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation of the regular expression. |

## dotAll

```TypeScript
get dotAll(): boolean
```

Gets the dotAll flag, indicating whether '.' matches newline characters.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get dotAll(): boolean--><!--Device-RegExp-get dotAll(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## flags

```TypeScript
get flags(): string
```

Gets the flags of the regular expression.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get flags(): string--><!--Device-RegExp-get flags(): string-End-->

**System capability:** SystemCapability.Utils.Lang

## global

```TypeScript
get global(): boolean
```

Gets the global flag, indicating whether to perform global matching.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get global(): boolean--><!--Device-RegExp-get global(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## hasIndices

```TypeScript
get hasIndices(): boolean
```

Gets the hasIndices flag, indicating whether to include indices of matching substrings.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get hasIndices(): boolean--><!--Device-RegExp-get hasIndices(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## ignoreCase

```TypeScript
get ignoreCase(): boolean
```

Gets the ignoreCase flag, indicating whether to ignore case.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get ignoreCase(): boolean--><!--Device-RegExp-get ignoreCase(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## multiline

```TypeScript
get multiline(): boolean
```

Gets the multiline flag, indicating whether to perform multiline matching.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get multiline(): boolean--><!--Device-RegExp-get multiline(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## source

```TypeScript
get source(): string
```

Returns a string containing the source text of this regular expression

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get source(): string--><!--Device-RegExp-get source(): string-End-->

**System capability:** SystemCapability.Utils.Lang

## sticky

```TypeScript
get sticky(): boolean
```

Gets the sticky flag, indicating whether to perform sticky matching.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get sticky(): boolean--><!--Device-RegExp-get sticky(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## unicode

```TypeScript
get unicode(): boolean
```

Gets the unicode flag, indicating whether to enable Unicode mode.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get unicode(): boolean--><!--Device-RegExp-get unicode(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## unicodeSets

```TypeScript
get unicodeSets(): boolean
```

Gets the unicodeSets flag, indicating whether Unicode set mode is enabled.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExp-get unicodeSets(): boolean--><!--Device-RegExp-get unicodeSets(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

