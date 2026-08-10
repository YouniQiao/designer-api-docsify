# AppBriefInfo (System API)

简要应用信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface AppBriefInfo--><!--Device-cloudExtension-export interface AppBriefInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## appId

```TypeScript
appId: string
```

应用程序ID。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AppBriefInfo-appId: string--><!--Device-AppBriefInfo-appId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

应用包名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AppBriefInfo-bundleName: string--><!--Device-AppBriefInfo-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## cloudSwitch

```TypeScript
cloudSwitch: boolean
```

应用程序的云开关。true表示启用云，false表示不启用云。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AppBriefInfo-cloudSwitch: boolean--><!--Device-AppBriefInfo-cloudSwitch: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## instanceId

```TypeScript
instanceId: int
```

应用分身ID，0表示应用本身，分身ID依次递增。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AppBriefInfo-instanceId: int--><!--Device-AppBriefInfo-instanceId: int-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

