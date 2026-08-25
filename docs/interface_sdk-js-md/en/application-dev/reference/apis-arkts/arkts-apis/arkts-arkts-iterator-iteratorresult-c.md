# IteratorResult

Represents an iterator result object containing whether iteration is done and the current element value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Creates an IteratorResult object representing completed iteration

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(done: boolean, value: T | undefined)
```

Creates an IteratorResult object with the specified done status and value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [done](#done) | boolean | Yes |
| [value](#value) | T \| undefined | Yes |

## constructor

```TypeScript
constructor(value: T)
```

Creates an IteratorResult object representing incomplete iteration with the specified value

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [value](#value) | T | Yes |

## done

```TypeScript
done: boolean
```

Indicates whether the iteration has completed. When true, the iterator has finished producing values and value will be undefined; when false, value contains the current element.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## value

```TypeScript
readonly value: T | undefined
```

The current element value returned by the iterator. When done is true, value is undefined; when done is false, value contains the current iteration element of type T.

**Type:** T \| undefined

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
