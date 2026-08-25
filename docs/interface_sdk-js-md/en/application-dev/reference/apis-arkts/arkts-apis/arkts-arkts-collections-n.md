# collections(Defines the collections for ArkTS)

The collections module provides ArkTS containers for efficient data transfer in concurrency scenarios. The ArkTS containers provide similar functionalities as their JavaScript counterparts, except that their properties cannot be added or updated through `.` or `[]`. By default, ArkTS containers are passed by reference between concurrent instances. This means that multiple concurrent instances can simultaneously operate the same container instance. Pass-by-copy is also supported. In this mode, each concurrent instance holds an ArkTS container instance. ArkTS containers are not thread-safe. They adopt the fail-fast approach. An exception is thrown if multiple concurrent instances make structural changes to a container instance at the same time. Therefore, in multi-thread read/write scenarios, you must use the ArkTS asynchronous lock to ensure secure access to the ArkTS containers. Currently, the following ArkTS containers are provided: [Array](#collections), [Map](#collections), [Set](#collections), TypedArray ([Int8Array](#collections), [Uint8Array](#collections), [Int16Array](#collections), [Uint16Array](#collections), [Int32Array](#collections), [Uint32Array](#collections), [Uint8ClampedArray](#collections) and [Float32Array](#collections)), [ArrayBuffer](#collections), [BitVector](#collections), and [ConcatArray](#collections).

> **NOTE：**&gt;
> - This module can be imported only to ArkTS files (with the file name extension .ets).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from '@kit.ArkTS';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Array(Defines the collections for ArkTS)](arkts-arkts-collections-array-c.md) |
| [Map(Defines the collections for ArkTS)](arkts-arkts-collections-map-c.md) |
| [Set(Defines the collections for ArkTS)](arkts-arkts-collections-set-c.md) |
| [ArrayBuffer(Defines the collections for ArkTS)](arkts-arkts-collections-arraybuffer-c.md) |
| [Int8Array(Defines the collections for ArkTS)](arkts-arkts-collections-int8array-c.md) |
| [Uint8ClampedArray(Defines the collections for ArkTS)](arkts-arkts-collections-uint8clampedarray-c.md) |
| [Uint8Array(Defines the collections for ArkTS)](arkts-arkts-collections-uint8array-c.md) |
| [Int16Array(Defines the collections for ArkTS)](arkts-arkts-collections-int16array-c.md) |
| [Uint16Array(Defines the collections for ArkTS)](arkts-arkts-collections-uint16array-c.md) |
| [Int32Array(Defines the collections for ArkTS)](arkts-arkts-collections-int32array-c.md) |
| [Uint32Array(Defines the collections for ArkTS)](arkts-arkts-collections-uint32array-c.md) |
| [Float32Array(Defines the collections for ArkTS)](arkts-arkts-collections-float32array-c.md) |
| [BitVector(Defines the collections for ArkTS)](arkts-arkts-collections-bitvector-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConcatArray(Defines the collections for ArkTS)](arkts-arkts-collections-concatarray-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TypedArrayFromMapFn(Defines the collections for ArkTS)](arkts-arkts-collections-typedarrayfrommapfn-t.md) |
| [TypedArrayPredicateFn(Defines the collections for ArkTS)](arkts-arkts-collections-typedarraypredicatefn-t.md) |
| [TypedArrayForEachCallback(Defines the collections for ArkTS)](arkts-arkts-collections-typedarrayforeachcallback-t.md) |
| [TypedArrayMapCallback(Defines the collections for ArkTS)](arkts-arkts-collections-typedarraymapcallback-t.md) |
| [TypedArrayReduceCallback(Defines the collections for ArkTS)](arkts-arkts-collections-typedarrayreducecallback-t.md) |
| [TypedArrayCompareFn(Defines the collections for ArkTS)](arkts-arkts-collections-typedarraycomparefn-t.md) |
| [ArrayFromMapFn(Defines the collections for ArkTS)](arkts-arkts-collections-arrayfrommapfn-t.md) |
| [ArrayPredicateFn(Defines the collections for ArkTS)](arkts-arkts-collections-arraypredicatefn-t.md) |
| [ArrayElementPredicateFn(Defines the collections for ArkTS)](arkts-arkts-collections-arrayelementpredicatefn-t.md) |
| [ArrayReduceCallback(Defines the collections for ArkTS)](arkts-arkts-collections-arrayreducecallback-t.md) |
| [ISendable(Defines the collections for ArkTS)](arkts-arkts-collections-isendable-t.md) |
