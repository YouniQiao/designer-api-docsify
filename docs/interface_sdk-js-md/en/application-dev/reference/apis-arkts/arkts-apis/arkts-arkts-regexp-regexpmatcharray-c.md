# RegExpMatchArray

Represents the matching result returned by string.prototype.matchAll(), or the non iterative result of RegExp.prototype.exec() in global mode.

**Inheritance/Implementation:** RegExpMatchArray extends [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

Creates a RegExpMatchArray instance that contains matching results.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [index](#index) | int | Yes |
| [input](#input) | string | Yes |
| result | Array & lt;string \ | undefined & gt; | Yes |
| indices | Array & lt;Array & lt;int & gt; & gt; | Yes |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>)
```

Creates a RegExpMatchArray instance containing matching results.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [index](#index) | int | Yes |
| [input](#input) | string | Yes |
| result | Array & lt;string \ | undefined & gt; | Yes |

## index

```TypeScript
public set index(val: int | undefined)
```

Sets the starting index of the match result.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## input

```TypeScript
public set input(val: string | undefined)
```

Sets the original string used for matching.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
