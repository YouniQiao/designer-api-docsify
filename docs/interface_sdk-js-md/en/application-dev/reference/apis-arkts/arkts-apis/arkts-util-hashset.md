# @ohos.util.HashSet

HashSet is implemented based on [HashMap](arkts-util-hashmap.md). In HashSet, only the **value** object is
 processed.
 Unlike [TreeSet](arkts-util-treeset.md), which stores and accesses data in sorted order, HashSet sorts data by
 hash value. This means that HashSet may use a different order when storing and accessing elements. Both of them allow
 only unique elements. However, null values are allowed in HashSet, but not in TreeSet, because null values may affect
 the order of elements in the container.
 **Recommended use case**: Use HashSet when you need a set that has only unique elements or need to deduplicate a set.
 This topic uses the following to identify the use of generics:
 - T: Type
 > **NOTE**
 >
 > - Container classes, implemented in static languages, have restrictions on storage locations and properties, and do
 > not support custom properties or methods.


## Modules to Import

```TypeScript
import { HashSet } from 'kits/@kit.ArkTS';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [HashSet](arkts-arkts-util-hashset-hashset-c.md) | HashSet is implemented based on HashMap. In HashSet, only the value object is processed. |

### Types

| Name | Description |
| --- | --- |
| [HashSetCbFn](arkts-arkts-hashsetcbfn-t.md) | The type of HashSet callback function. |

