# Mutex

A mutual exclusion lock that provides exclusive access to a shared resource

**继承/实现关系：** Mutex implements [Lock](arkts-arkts-syncprimitives-lock-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Mutex implements Lock--><!--Device-unnamed-export class Mutex implements Lock-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a new Mutex instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Mutex-constructor()--><!--Device-Mutex-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## lock

```TypeScript
lock(): void
```

Acquires the lock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Mutex-lock(): void--><!--Device-Mutex-lock(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## lockGuard

```TypeScript
lockGuard(callback: () => void): void
```

Executes the callback while holding the lock, automatically releasing it afterwards

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Mutex-lockGuard(callback: () => void): void--><!--Device-Mutex-lockGuard(callback: () => void): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () =&gt; void | 是 | the callback to execute while holding the lock. |

## unlock

```TypeScript
unlock(): void
```

Releases the lock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Mutex-unlock(): void--><!--Device-Mutex-unlock(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

