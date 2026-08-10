# ReadLock

A read lock that allows concurrent read access to a shared resource

**继承/实现关系：** ReadLock implements [Lock](arkts-arkts-syncprimitives-lock-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class ReadLock implements Lock--><!--Device-unnamed-export class ReadLock implements Lock-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(lock: RWLock)
```

Constructs a new ReadLock associated with the given RWLock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadLock-constructor(lock: RWLock)--><!--Device-ReadLock-constructor(lock: RWLock)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lock | [RWLock](arkts-arkts-syncprimitives-rwlock-c.md) | 是 | the RWLock this ReadLock is associated with. |

## lock

```TypeScript
lock(): void
```

Acquires the read lock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadLock-lock(): void--><!--Device-ReadLock-lock(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## unlock

```TypeScript
unlock(): void
```

Releases the read lock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadLock-unlock(): void--><!--Device-ReadLock-unlock(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

