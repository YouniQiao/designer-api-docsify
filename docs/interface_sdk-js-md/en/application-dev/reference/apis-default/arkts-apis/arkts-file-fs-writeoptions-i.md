# WriteOptions

Defines the options used in **write()**. It inherits from [Options](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-options-i.md).

**Inheritance/Implementation:** WriteOptions extends [Options](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-options-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface WriteOptions--><!--Device-unnamed-export interface WriteOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## length

```TypeScript
length?: long
```

Length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WriteOptions-length?: long--><!--Device-WriteOptions-length?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## offset

```TypeScript
offset?: long
```

Start position of the file to write, in bytes. This parameter is optional. By default, data is written from the current position.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WriteOptions-offset?: long--><!--Device-WriteOptions-offset?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

