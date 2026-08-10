# clearFileCache

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## clearFileCache

```TypeScript
function clearFileCache(): void
```

清除保存下载内容的文件缓存。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cacheDownload-function clearFileCache(): void--><!--Device-cacheDownload-function clearFileCache(): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Examples

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
  
cacheDownload.clearFileCache();
```

