# @ohos.file.hash

The **FileHash** module implements hash processing on files.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace hash--><!--Device-unnamed-declare namespace hash-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { hash } from '@kit.CoreFileKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createHash](arkts-corefile-hash-createhash-f.md#createHash) | Creates a **HashStream** instance, which can be used to generate a message digest (a hash value) using the given algorithm. |
| [hash](arkts-corefile-hash-f.md#hash) | Calculates a hash value for a file. This API uses a promise to return the result. |
| [hash](arkts-corefile-hash-f.md#hash) | Calculates a hash value for a file. This API uses an asynchronous callback to return the result. |

### Classes

| Name | Description |
| --- | --- |
| [HashStream](arkts-corefile-hash-hashstream-c.md) | The **HashStream** class is a utility for creating a message digest of data. You can use [createHash](arkts-corefile-hash-createhash-f.md#createHash) to create a **HashStream** instance. |

