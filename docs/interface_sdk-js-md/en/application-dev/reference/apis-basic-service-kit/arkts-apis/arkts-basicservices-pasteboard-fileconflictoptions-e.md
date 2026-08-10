# FileConflictOptions

定义文件拷贝冲突时的选项。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-pasteboard-enum FileConflictOptions--><!--Device-pasteboard-enum FileConflictOptions-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## OVERWRITE

```TypeScript
OVERWRITE = 0
```

目标路径存在同文件名时覆盖。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileConflictOptions-OVERWRITE = 0--><!--Device-FileConflictOptions-OVERWRITE = 0-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## SKIP

```TypeScript
SKIP = 1
```

目标路径存在同文件名时跳过，若设置SKIP，应用获取到的粘贴数据不包含跳过文件。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FileConflictOptions-SKIP = 1--><!--Device-FileConflictOptions-SKIP = 1-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

