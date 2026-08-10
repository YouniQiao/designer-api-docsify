# File

File类型数据，是[UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)的子类，也是文件类型数据的基类，用于描述文件类型数据，推荐开发者优先使用File的子类描述数据，如  
[Image](arkts-arkdata-unifieddatachannel-image-c.md)、[Video](arkts-arkdata-unifieddatachannel-video-c.md)、  
[Folder](arkts-arkdata-unifieddatachannel-folder-c.md)等具体子类。

**Inheritance/Implementation:** File extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class File extends UnifiedRecord--><!--Device-unifiedDataChannel-class File extends UnifiedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## details

```TypeScript
details?: Record<string, string>
```

是一个字典类型对象，key和value都是string类型，用于描述文件相关信息。例如，可生成一个details内容为

{

"name":"文件名",

"type":"文件类型"

}

的数据对象，用于描述一个文件。非必填字段，默认值为空字典对象。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-File-details?: Record<string, string>--><!--Device-File-details?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uri

```TypeScript
set uri(value: string)
```

表示统一文件的详细信息。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-File-set uri(value: string)--><!--Device-File-set uri(value: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uriAuthorizationPolicies

```TypeScript
set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)
```

用于拖拽场景的URI授权策略。默认值为READ+WRITE+PERSIST（读+写+持久化授权），只针对单个record使用，优先级最高，具体策略见  
[UriPermission](arkts-arkdata-unifieddatachannel-uripermission-e.md)。

**Type:** Array&lt;UriPermission&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-File-set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)--><!--Device-File-set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

