# WorkerLocal

A thread-local storage container that maintains a separate value per worker

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class WorkerLocal<T>--><!--Device-unnamed-export class WorkerLocal<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a new WorkerLocal instance with no initial value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkerLocal-constructor()--><!--Device-WorkerLocal-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(init: () => T)
```

Constructs a new WorkerLocal instance with an initializer function

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkerLocal-constructor(init: () => T)--><!--Device-WorkerLocal-constructor(init: () => T)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | () =&gt; T | Yes | the initializer function that provides the initial value. |

## delete

```TypeScript
delete(): void
```

Removes the value for the current worker

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkerLocal-delete(): void--><!--Device-WorkerLocal-delete(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## get

```TypeScript
get(): T
```

Returns the value for the current worker

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkerLocal-get(): T--><!--Device-WorkerLocal-get(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | the value for the current worker |

## set

```TypeScript
set(value: T): void
```

Sets the value for the current worker

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkerLocal-set(value: T): void--><!--Device-WorkerLocal-set(value: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | the value to set for the current worker. |

