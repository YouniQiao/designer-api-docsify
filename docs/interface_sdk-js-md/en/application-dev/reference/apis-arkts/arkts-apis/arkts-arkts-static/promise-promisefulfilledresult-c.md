# PromiseFulfilledResult

Represents the result of a fulfilled promise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class PromiseFulfilledResult<T>--><!--Device-unnamed-export class PromiseFulfilledResult<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs an empty PromiseFulfilledResult.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseFulfilledResult-constructor()--><!--Device-PromiseFulfilledResult-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: T)
```

Constructs a PromiseFulfilledResult with the given value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseFulfilledResult-constructor(value: T)--><!--Device-PromiseFulfilledResult-constructor(value: T)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | the fulfilled value. |

## status

```TypeScript
status: string
```

The status of the promise.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseFulfilledResult-status: string--><!--Device-PromiseFulfilledResult-status: string-End-->

**System capability:** SystemCapability.Utils.Lang

## value

```TypeScript
value: T
```

The value of the fulfilled promise.

**Type:** T

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseFulfilledResult-value: T--><!--Device-PromiseFulfilledResult-value: T-End-->

**System capability:** SystemCapability.Utils.Lang

