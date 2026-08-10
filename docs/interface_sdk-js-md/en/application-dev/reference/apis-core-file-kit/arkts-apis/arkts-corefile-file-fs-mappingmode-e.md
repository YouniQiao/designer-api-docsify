# MappingMode

枚举，文件内存映射模式类型，支持mmap接口使用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare enum MappingMode--><!--Device-unnamed-declare enum MappingMode-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## READ_ONLY

```TypeScript
READ_ONLY = 0
```

只读映射模式。文件映射区不可写，修改会抛出异常。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MappingMode-READ_ONLY = 0--><!--Device-MappingMode-READ_ONLY = 0-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## READ_WRITE

```TypeScript
READ_WRITE = 1
```

读写映射模式。修改会写入文件映射区，后续由操作系统同步到文件（非实时）。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MappingMode-READ_WRITE = 1--><!--Device-MappingMode-READ_WRITE = 1-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## PRIVATE

```TypeScript
PRIVATE = 2
```

私有映射模式。是一种写时复制的映射机制，对映射区的修改仅对当前进程可见，不会影响原始文件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MappingMode-PRIVATE = 2--><!--Device-MappingMode-PRIVATE = 2-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

