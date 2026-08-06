# clearMemoryCache

## clearMemoryCache

```TypeScript
function clearMemoryCache(): void
```

Clears this memory cache.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cacheDownload-function clearMemoryCache(): void--><!--Device-cacheDownload-function clearMemoryCache(): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Example**

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
  
cacheDownload.clearMemoryCache();
```

