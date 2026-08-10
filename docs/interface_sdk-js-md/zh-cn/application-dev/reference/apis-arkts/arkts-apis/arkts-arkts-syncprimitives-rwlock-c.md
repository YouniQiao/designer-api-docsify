# RWLock

A read-write lock that allows concurrent read access but exclusive write access

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class RWLock--><!--Device-unnamed-export class RWLock-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a new RWLock instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RWLock-constructor()--><!--Device-RWLock-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## readLock

```TypeScript
readLock(): ReadLock
```

Returns a ReadLock associated with this RWLock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RWLock-readLock(): ReadLock--><!--Device-RWLock-readLock(): ReadLock-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReadLock](arkts-arkts-syncprimitives-readlock-c.md) | the read lock |

## writeLock

```TypeScript
writeLock(): WriteLock
```

Returns a WriteLock associated with this RWLock

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RWLock-writeLock(): WriteLock--><!--Device-RWLock-writeLock(): WriteLock-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WriteLock](arkts-arkts-syncprimitives-writelock-c.md) | the write lock |

