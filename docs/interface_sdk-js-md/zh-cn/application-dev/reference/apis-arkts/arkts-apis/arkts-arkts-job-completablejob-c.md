# CompletableJob

A completable job that extends Job, allowing manual completion or failure.

**继承/实现关系：** CompletableJob extends [Job<T>](Job<T>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class CompletableJob<T> extends Job<T>--><!--Device-unnamed-export class CompletableJob<T> extends Job<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## Await

```TypeScript
Await(): T
```

Waits for the completion of the job and returns the result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletableJob-Await(): T--><!--Device-CompletableJob-Await(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The result of the task. |

## constructor

```TypeScript
constructor()
```

Constructs a CompletableJob instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletableJob-constructor()--><!--Device-CompletableJob-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## fail

```TypeScript
fail(): void
```

Fails the job with an empty Error.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletableJob-fail(): void--><!--Device-CompletableJob-fail(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## fail

```TypeScript
fail(error: Error): void
```

Fails the job with a specific error.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletableJob-fail(error: Error): void--><!--Device-CompletableJob-fail(error: Error): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | Error | 是 | The error to fail the job with. |

## finish

```TypeScript
finish(): void
```

Finishes the job with undefined value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletableJob-finish(): void--><!--Device-CompletableJob-finish(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## finish

```TypeScript
finish<T>(value: T): void
```

Finishes the job with a value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletableJob-finish<T>(value: T): void--><!--Device-CompletableJob-finish<T>(value: T): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | The value to finish the job with. |

