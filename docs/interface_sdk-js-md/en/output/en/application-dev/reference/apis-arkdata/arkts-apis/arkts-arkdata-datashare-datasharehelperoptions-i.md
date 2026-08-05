# DataShareHelperOptions

Represents the optional parameters of [DataShareHelper]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataShareHelperOptions--><!--Device-dataShare-interface DataShareHelperOptions-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## isProxy

```TypeScript
isProxy?: boolean
```

Whether the [DataShareHelper]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is in proxy mode. The default value is **false**. If the value is **true**, the [DataShareHelper]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to be created is in proxy mode, and all operations will not open the data provider application unless the database does not exist. If the database does not exist, [createDataShareHelper]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ will start the data provider to create a database.

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

Waiting time for starting the data provider process, in seconds. The default value is **2**.

**Type:** int

**Default:** 2

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelperOptions-waitTime?: int--><!--Device-DataShareHelperOptions-waitTime?: int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

