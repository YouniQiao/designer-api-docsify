# BundleInfo (System API)

端云协同应用信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cloudData-interface BundleInfo--><!--Device-cloudData-interface BundleInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## bundleName

```TypeScript
bundleName: string
```

应用包名。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleInfo-bundleName: string--><!--Device-BundleInfo-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## storeId

```TypeScript
storeId?: string
```

数据库名称。默认值为空字符串，此时查询该应用下所有数据库。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleInfo-storeId?: string--><!--Device-BundleInfo-storeId?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

