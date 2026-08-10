# WriteLock

A write lock that provides exclusive write access to a shared resource

**继承/实现关系：** WriteLock implements [Lock](arkts-arkts-syncprimitives-lock-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class WriteLock implements Lock--><!--Device-unnamed-export class WriteLock implements Lock-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(lock: RWLock)
```

Constructs a new WriteLock associated with the given RWLock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WriteLock-constructor(lock: RWLock)--><!--Device-WriteLock-constructor(lock: RWLock)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lock | [RWLock](arkts-arkts-syncprimitives-rwlock-c.md) | 是 | the RWLock this WriteLock is associated with. |

## lock

```TypeScript
lock(): void
```

Acquires the write lock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WriteLock-lock(): void--><!--Device-WriteLock-lock(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## unlock

```TypeScript
unlock(): void
```

Releases the write lock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WriteLock-unlock(): void--><!--Device-WriteLock-unlock(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

