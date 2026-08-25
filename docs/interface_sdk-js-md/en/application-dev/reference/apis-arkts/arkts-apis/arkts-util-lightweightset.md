# @ohos.util.LightWeightSet

LightWeightSet stores a set of values, each of which must be unique.
 LightWeightSet is based on generics and uses a lightweight structure. Its default initial capacity is 8, and it has
 the capacity doubled in each expansion.
 The values in such a set are searched using hash values, which are stored in an array.
 Compared with [HashSet](arkts-arkts-util-hashset-hashset-c.md), which can also store values, LightWeightSet occupies less memory.
 **Recommended use case**: Use LightWeightSet when you need a set that has only unique elements or need to deduplicate
 a set.
 This topic uses the following to identify the use of generics:
 - T: Type
 > **NOTE**
 >
 > - Container classes, implemented in static languages, have restrictions on storage locations and properties, and do
 > not support custom properties or methods.


## Modules to Import

```TypeScript
import { LightWeightSet } from 'kits/@kit.ArkTS';
import { LightWeightSetForEachCb } from 'kits/@kit.ArkTS';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md) |
