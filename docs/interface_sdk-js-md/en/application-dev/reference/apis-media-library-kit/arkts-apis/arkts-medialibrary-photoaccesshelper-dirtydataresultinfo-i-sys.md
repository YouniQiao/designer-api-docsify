# DirtyDataResultInfo (System API)

```TypeScript
interface DirtyDataResultInfo
```

Dirty data query results.

**Since:** 26.2.0

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## elapsedTime

```TypeScript
elapsedTime: number
```

Execution time in milliseconds. Unit: milliseconds. The value should be an integer.

**Type:** number

**Since:** 26.2.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## errorMsg

```TypeScript
errorMsg: string
```

Error description. Returns an empty string when no error occurs, otherwise contains the error description.

**Type:** string

**Since:** 26.2.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## profit

```TypeScript
profit: number
```

Benefit of cleanable dirty data size in bytes. Unit: bytes. The value should be an integer.

**Type:** number

**Since:** 26.2.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.
