# PromiseRejectedResult

Represents the result of a rejected promise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class PromiseRejectedResult--><!--Device-unnamed-export class PromiseRejectedResult-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a PromiseRejectedResult with a default error.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseRejectedResult-constructor()--><!--Device-PromiseRejectedResult-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(reason: Error)
```

Constructs a PromiseRejectedResult with the given reason.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseRejectedResult-constructor(reason: Error)--><!--Device-PromiseRejectedResult-constructor(reason: Error)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reason | Error | Yes | the rejection reason. |

## reason

```TypeScript
reason: Error
```

The reason the promise was rejected.

**Type:** Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseRejectedResult-reason: Error--><!--Device-PromiseRejectedResult-reason: Error-End-->

**System capability:** SystemCapability.Utils.Lang

## status

```TypeScript
status: string
```

The status of the promise.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseRejectedResult-status: string--><!--Device-PromiseRejectedResult-status: string-End-->

**System capability:** SystemCapability.Utils.Lang

