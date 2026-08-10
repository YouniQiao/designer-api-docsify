# WorkerLocal

A thread-local storage container that maintains a separate value per worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class WorkerLocal<T>--><!--Device-unnamed-export class WorkerLocal<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a new WorkerLocal instance with no initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WorkerLocal-constructor()--><!--Device-WorkerLocal-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(init: () => T)
```

Constructs a new WorkerLocal instance with an initializer function

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WorkerLocal-constructor(init: () => T)--><!--Device-WorkerLocal-constructor(init: () => T)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| init | () =&gt; T | 是 | the initializer function that provides the initial value. |

## delete

```TypeScript
delete(): void
```

Removes the value for the current worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WorkerLocal-delete(): void--><!--Device-WorkerLocal-delete(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## get

```TypeScript
get(): T
```

Returns the value for the current worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WorkerLocal-get(): T--><!--Device-WorkerLocal-get(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | the value for the current worker |

## set

```TypeScript
set(value: T): void
```

Sets the value for the current worker

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WorkerLocal-set(value: T): void--><!--Device-WorkerLocal-set(value: T): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | the value to set for the current worker. |

