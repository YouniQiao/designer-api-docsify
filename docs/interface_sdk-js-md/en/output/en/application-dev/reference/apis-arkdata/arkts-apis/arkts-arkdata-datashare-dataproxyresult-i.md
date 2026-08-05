# DataProxyResult

Defines a struct for the batch operation result of shared configuration.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataProxyResult--><!--Device-dataShare-interface DataProxyResult-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## result

```TypeScript
result: DataProxyErrorCode
```

Operation result code.

**Type:** DataProxyErrorCode

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyResult-result: DataProxyErrorCode--><!--Device-DataProxyResult-result: DataProxyErrorCode-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## uri

```TypeScript
uri: string
```

URI to be operated, with a maximum of 256 bytes. The value is fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value but must be unique in the same application.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyResult-uri: string--><!--Device-DataProxyResult-uri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

