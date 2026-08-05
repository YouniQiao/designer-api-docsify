# clearFileCache

## clearFileCache

```TypeScript
function clearFileCache(): void
```

Clears this file cache.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cacheDownload-function clearFileCache(): void--><!--Device-cacheDownload-function clearFileCache(): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Example**

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
  
cacheDownload.clearFileCache();
```

