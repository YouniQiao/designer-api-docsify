# CloudInfo (System API)

Represents the cloud information.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from '@kit.ArkData';
```

## apps

```TypeScript
apps: Record<string, AppBriefInfo>
```

Brief application information.

**Type:** Record&lt;string, [AppBriefInfo](arkts-arkdata-cloudextension-appbriefinfo-i-sys.md)&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## cloudInfo

```TypeScript
cloudInfo: ServiceInfo
```

Cloud service information.

**Type:** [ServiceInfo](arkts-arkdata-cloudextension-serviceinfo-i-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.
