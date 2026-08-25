# @arkts.collections(Defines the collections for ArkTS)

The collections module provides ArkTS containers for efficient data transfer in concurrency scenarios. The ArkTS containers provide similar functionalities as their JavaScript counterparts, except that their properties cannot be added or updated through `.` or `[]`. By default, ArkTS containers are passed by reference between concurrent instances. This means that multiple concurrent instances can simultaneously operate the same container instance. Pass-by-copy is also supported. In this mode, each concurrent instance holds an ArkTS container instance. ArkTS containers are not thread-safe. They adopt the fail-fast approach. An exception is thrown if multiple concurrent instances make structural changes to a container instance at the same time. Therefore, in multi-thread read/write scenarios, you must use the ArkTS asynchronous lock to ensure secure access to the ArkTS containers. Currently, the following ArkTS containers are provided: [Array](arkts-arkts-collections-n.md), [Map](arkts-arkts-collections-n.md), [Set](arkts-arkts-collections-n.md), TypedArray ([Int8Array](arkts-arkts-collections-n.md), [Uint8Array](arkts-arkts-collections-n.md), [Int16Array](arkts-arkts-collections-n.md), [Uint16Array](arkts-arkts-collections-n.md), [Int32Array](arkts-arkts-collections-n.md), [Uint32Array](arkts-arkts-collections-n.md), [Uint8ClampedArray](arkts-arkts-collections-n.md) and [Float32Array](arkts-arkts-collections-n.md)), [ArrayBuffer](arkts-arkts-collections-n.md), [BitVector](arkts-arkts-collections-n.md), and [ConcatArray](arkts-arkts-collections-n.md).

> **NOTE：**&gt;
> - This module can be imported only to ArkTS files (with the file name extension .ets).

## Modules to Import

```TypeScript
import { collections } from '@kit.ArkTS';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [collections(Defines the collections for ArkTS)](arkts-arkts-collections-n.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BuiltinArray(Defines the collections for ArkTS)](arkts-arkts-builtinarray-t.md) |
| [BuiltinMap(Defines the collections for ArkTS)](arkts-arkts-builtinmap-t.md) |
