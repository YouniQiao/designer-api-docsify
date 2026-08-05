# DataProxyConfig

Defines a struct for the data proxy configuration.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataProxyConfig--><!--Device-dataShare-interface DataProxyConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## maxValueLength

```TypeScript
maxValueLength?: DataProxyMaxValueLength
```

Sets the maximum length of the data proxy value. The default value is MAX\_LENGTH\_4K, indicating that the maximum value length is 4096 bytes. If the length of the value that is actually transferred or obtained exceeds the maximum value length specified by this parameter, the publish or get operation will fail. Default value: MAX\_LENGTH\_4K.

**Type:** DataProxyMaxValueLength

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyConfig-maxValueLength?: DataProxyMaxValueLength--><!--Device-DataProxyConfig-maxValueLength?: DataProxyMaxValueLength-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## type

```TypeScript
type: DataProxyType
```

Type of the data proxy.

**Type:** DataProxyType

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyConfig-type: DataProxyType--><!--Device-DataProxyConfig-type: DataProxyType-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

