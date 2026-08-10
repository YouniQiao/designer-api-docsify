# IteratorResult

Represents an iterator result object containing whether iteration is done and the current element value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class IteratorResult<out T>--><!--Device-unnamed-export class IteratorResult<out T>-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Creates an IteratorResult object representing completed iteration

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IteratorResult-constructor()--><!--Device-IteratorResult-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(done: boolean, value: T | undefined)
```

Creates an IteratorResult object with the specified done status and value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IteratorResult-constructor(done: boolean, value: T | undefined)--><!--Device-IteratorResult-constructor(done: boolean, value: T | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| done | boolean | Yes | Indicates whether iteration is completed |
| value | T \| undefined | Yes | The element value returned by the iterator |

## constructor

```TypeScript
constructor(value: T)
```

Creates an IteratorResult object representing incomplete iteration with the specified value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IteratorResult-constructor(value: T)--><!--Device-IteratorResult-constructor(value: T)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The element value returned by the iterator |

## done

```TypeScript
done: boolean
```

Indicates whether the iteration has completed. When true, the iterator has finished producing values and value will be undefined; when false, value contains the current element.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IteratorResult-done: boolean--><!--Device-IteratorResult-done: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## value

```TypeScript
readonly value: T | undefined
```

The current element value returned by the iterator. When done is true, value is undefined;when done is false, value contains the current iteration element of type T.

**Type:** T \| undefined

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IteratorResult-readonly value: T | undefined--><!--Device-IteratorResult-readonly value: T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

