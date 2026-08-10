# UnifiedDataProperties

定义统一数据对象中所有数据记录的属性，包含时间戳、标签、粘贴范围以及一些附加数据等。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class UnifiedDataProperties--><!--Device-unifiedDataChannel-class UnifiedDataProperties-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## getDelayData

```TypeScript
getDelayData?: GetDelayData
```

延迟获取数据回调。当前只支持同设备剪贴板场景，当用户从剪贴板读取数据时触发该回调。非必填字段，默认值为undefined。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedDataProperties-getDelayData?: GetDelayData--><!--Device-UnifiedDataProperties-getDelayData?: GetDelayData-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## extras

```TypeScript
extras?: Record<string, object>
```

是一个字典类型对象，用于设置其他附加属性数据。非必填字段，默认值为空字典对象。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, object&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedDataProperties-extras?: Record<string, object>--><!--Device-UnifiedDataProperties-extras?: Record<string, object>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## shareOptions

```TypeScript
shareOptions?: ShareOptions
```

指示[UnifiedData](arkts-arkdata-unifieddatachannel-unifieddata-c.md)支持的设备内使用范围，非必填字段，默认值为CROSS_APP。

**Type:** [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedDataProperties-shareOptions?: ShareOptions--><!--Device-UnifiedDataProperties-shareOptions?: ShareOptions-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## tag

```TypeScript
tag?: string
```

用户自定义标签。非必填字段，默认值为空字符串。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedDataProperties-tag?: string--><!--Device-UnifiedDataProperties-tag?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## timestamp

```TypeScript
readonly timestamp?: Date
```

[UnifiedData](arkts-arkdata-unifieddatachannel-unifieddata-c.md)的生成时间戳。默认值为1970年1月1日（UTC）。

**Type:** Date

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedDataProperties-readonly timestamp?: Date--><!--Device-UnifiedDataProperties-readonly timestamp?: Date-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uriAuthorizationPolicies

```TypeScript
uriAuthorizationPolicies?: Array<UriPermission>
```

用于拖拽场景的URI授权策略。默认值为READ+WRITE+PERSIST，只对单次数据生效，优先级较低，具体策略见[UriPermission](arkts-arkdata-unifieddatachannel-uripermission-e.md)。

**Type:** Array&lt;UriPermission&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-UnifiedDataProperties-uriAuthorizationPolicies?: Array<UriPermission>--><!--Device-UnifiedDataProperties-uriAuthorizationPolicies?: Array<UriPermission>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

