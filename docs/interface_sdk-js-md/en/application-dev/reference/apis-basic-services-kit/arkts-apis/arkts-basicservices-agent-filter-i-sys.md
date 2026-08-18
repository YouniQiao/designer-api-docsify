# Filter

Defines the filter criteria.

**Since:** 23

<!--Device-agent-interface Filter--><!--Device-agent-interface Filter-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
import { cacheDownload } from '@kit.BasicServicesKit';
```

## bundle

```TypeScript
bundle?: string
```

Specify the package name of an application. Only for advanced search, common search will be fixed to the caller. A "*" means any bundle.

**Type:** string

**Since:** 23

<!--Device-Filter-bundle?: string--><!--Device-Filter-bundle?: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**System API:** This is a system API.

