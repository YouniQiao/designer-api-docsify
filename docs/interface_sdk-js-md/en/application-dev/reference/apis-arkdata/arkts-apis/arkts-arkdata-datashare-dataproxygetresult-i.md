# DataProxyGetResult

配置共享批量获取操作结果的数据结构。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataProxyGetResult--><!--Device-dataShare-interface DataProxyGetResult-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## allowList

```TypeScript
allowList: string[] | undefined
```

如果获取操作成功，则为共享配置的允许列表；如果获取操作失败，则未定义。只有发布者才能获取允许列表，其他应用只能获取值。

**Type:** string[] \| undefined

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyGetResult-allowList: string[] | undefined--><!--Device-DataProxyGetResult-allowList: string[] | undefined-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## result

```TypeScript
result: DataProxyErrorCode
```

操作结果的错误码。

**Type:** [DataProxyErrorCode](arkts-arkdata-datashare-dataproxyerrorcode-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyGetResult-result: DataProxyErrorCode--><!--Device-DataProxyGetResult-result: DataProxyErrorCode-End-->

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

<!--Device-DataProxyGetResult-uri: string--><!--Device-DataProxyGetResult-uri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## value

```TypeScript
value: ValueType | undefined
```

如果获取操作成功，则为共享配置的值；如果获取操作失败，则未定义。

**Type:** [ValueType](arkts-arkdata-valuetype-t.md) \| undefined

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyGetResult-value: ValueType | undefined--><!--Device-DataProxyGetResult-value: ValueType | undefined-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

