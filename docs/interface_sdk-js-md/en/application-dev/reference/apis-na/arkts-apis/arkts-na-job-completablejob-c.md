# CompletableJob

A completable job that extends Job, allowing manual completion or failure.

**Inheritance/Implementation:** CompletableJob extends Job<T>

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class CompletableJob--><!--Device-unnamed-export class CompletableJob-End-->

**System capability:** SystemCapability.Utils.Lang

## Await

```TypeScript
Await(): T
```

Waits for the completion of the job and returns the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletableJob-Await(): T--><!--Device-CompletableJob-Await(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | The result of the task. |

## constructor

```TypeScript
constructor()
```

Constructs a CompletableJob instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletableJob-constructor()--><!--Device-CompletableJob-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## fail

```TypeScript
fail(): void
```

Fails the job with an empty Error.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletableJob-fail(): void--><!--Device-CompletableJob-fail(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## fail

```TypeScript
fail(error: Error): void
```

Fails the job with a specific error.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletableJob-fail(error: Error): void--><!--Device-CompletableJob-fail(error: Error): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | Error | Yes | The error to fail the job with. |

## finish

```TypeScript
finish(): void
```

Finishes the job with undefined value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletableJob-finish(): void--><!--Device-CompletableJob-finish(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## finish

```TypeScript
finish<T>(value: T): void
```

Finishes the job with a value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompletableJob-finish<T>(value: T): void--><!--Device-CompletableJob-finish<T>(value: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value to finish the job with. |

