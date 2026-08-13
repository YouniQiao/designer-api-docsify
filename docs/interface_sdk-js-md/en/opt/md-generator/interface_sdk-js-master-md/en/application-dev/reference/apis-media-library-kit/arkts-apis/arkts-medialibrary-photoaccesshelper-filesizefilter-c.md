# FileSizeFilter

Describes the configuration for file size filtering.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-photoAccessHelper-class FileSizeFilter--><!--Device-photoAccessHelper-class FileSizeFilter-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## extraFileSize

```TypeScript
extraFileSize?: number
```

Maximum file size in **FilterOperator.BETWEEN** mode. The default value is **-1**. The unit is bytes.

**Type:** number

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FileSizeFilter-extraFileSize?: long--><!--Device-FileSizeFilter-extraFileSize?: long-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## fileSize

```TypeScript
fileSize: number
```

File size used for filtering. The unit is bytes.

**Type:** number

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FileSizeFilter-fileSize: long--><!--Device-FileSizeFilter-fileSize: long-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## filterOperator

```TypeScript
filterOperator: FilterOperator
```

Filter operator. For example, files can be filtered based on being greater than or less than a certain file size.

**Type:** [FilterOperator](arkts-medialibrary-photoaccesshelper-filteroperator-e.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FileSizeFilter-filterOperator: FilterOperator--><!--Device-FileSizeFilter-filterOperator: FilterOperator-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
