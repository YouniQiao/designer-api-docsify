# RWLock

A read-write lock that allows concurrent read access but exclusive write access

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class RWLock--><!--Device-unnamed-export class RWLock-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a new RWLock instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RWLock-constructor()--><!--Device-RWLock-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## readLock

```TypeScript
readLock(): ReadLock
```

Returns a ReadLock associated with this RWLock

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RWLock-readLock(): ReadLock--><!--Device-RWLock-readLock(): ReadLock-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [ReadLock](arkts-na-syncprimitives-readlock-c.md) | the read lock |

## writeLock

```TypeScript
writeLock(): WriteLock
```

Returns a WriteLock associated with this RWLock

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RWLock-writeLock(): WriteLock--><!--Device-RWLock-writeLock(): WriteLock-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [WriteLock](arkts-na-syncprimitives-writelock-c.md) | the write lock |

