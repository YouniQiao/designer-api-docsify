# DataShareHelperOptions (System API)

Represents the optional parameters of [DataShareHelper](#datasharehelperoptions-system-api).

**Since:** 10

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import dataShare from '@kit.ArkData';
import dataSharePredicates from '@kit.ArkDataPredicates';
```

## isProxy

```TypeScript
isProxy?: boolean
```

Whether the [DataShareHelper](#datasharehelperoptions-system-api) is in proxy mode. The default value is **false**.If the value is **true**, the [DataShareHelper](#datasharehelperoptions-system-api) to be created is in proxy mode, and all operations will not open the data provider application unless the database does not exist. If the database does not exist, [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f-sys.md) will start the data provider to create a database.

**Type:** boolean

**Default:** false

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## waitTime

```TypeScript
waitTime?: number
```

Waiting time for starting the data provider process, in seconds. The default value is **2**.

**Type:** number

**Default:** 2

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.
