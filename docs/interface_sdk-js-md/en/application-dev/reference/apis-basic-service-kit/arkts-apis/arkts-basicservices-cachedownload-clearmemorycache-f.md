# clearMemoryCache

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## clearMemoryCache

```TypeScript
function clearMemoryCache(): void
```

清除缓存下载内容的内存缓存。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cacheDownload-function clearMemoryCache(): void--><!--Device-cacheDownload-function clearMemoryCache(): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Examples

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
  
cacheDownload.clearMemoryCache();
```

