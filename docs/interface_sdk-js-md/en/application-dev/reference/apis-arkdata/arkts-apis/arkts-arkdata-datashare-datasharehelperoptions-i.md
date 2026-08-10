# DataShareHelperOptions

指定[DataShareHelper](arkts-arkdata-datashare-datasharehelperoptions-i.md)的可选参数，包含是否在代理模式下，以及非静默访问的拉起等待时间。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataShareHelperOptions--><!--Device-dataShare-interface DataShareHelperOptions-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## isProxy

```TypeScript
isProxy?: boolean
```

默认为false，如果为true，则要创建的[DataShareHelper](arkts-arkdata-datashare-datasharehelperoptions-i.md)处于代理模式，所有操作都不会打开数据提供者APP，除非数据库不存在，当数据库不存在时，  
[createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f.md#createdatasharehelper)会拉起数据提供者创建数据库。

**Type:** boolean

**Default:** false

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelperOptions-isProxy?: boolean--><!--Device-DataShareHelperOptions-isProxy?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## waitTime

```TypeScript
waitTime?: int
```

拉起数据提供者进程的等待时间（单位：秒），默认值为2秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 2

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelperOptions-waitTime?: int--><!--Device-DataShareHelperOptions-waitTime?: int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

