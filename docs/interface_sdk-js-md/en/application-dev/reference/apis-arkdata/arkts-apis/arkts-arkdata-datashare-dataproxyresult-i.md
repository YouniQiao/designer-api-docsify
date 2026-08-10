# DataProxyResult

配置共享批量操作结果的数据结构。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataProxyResult--><!--Device-dataShare-interface DataProxyResult-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## result

```TypeScript
result: DataProxyErrorCode
```

操作结果的错误码。

**Type:** [DataProxyErrorCode](arkts-arkdata-datashare-dataproxyerrorcode-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyResult-result: DataProxyErrorCode--><!--Device-DataProxyResult-result: DataProxyErrorCode-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## uri

```TypeScript
uri: string
```

被操作的URI。固定格式为`"datashareproxy://{bundleName}/{path}"`，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复，字符串长度不超过256个字节。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyResult-uri: string--><!--Device-DataProxyResult-uri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

