# EventClassifyInfo (System API)

事件信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface EventClassifyInfo--><!--Device-update-export interface EventClassifyInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## eventClassify

```TypeScript
eventClassify: EventClassify
```

事件类型，用于指定要监听的事件分类。可取值：TASK（任务事件）。

**Type:** [EventClassify](arkts-basicservices-update-eventclassify-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-EventClassifyInfo-eventClassify: EventClassify--><!--Device-EventClassifyInfo-eventClassify: EventClassify-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## extraInfo

```TypeScript
extraInfo: string
```

额外信息，用于传递扩展数据。默认值为空字符串，表示无额外信息。长度范围[0, 128]，单位：字符。有效字符包括字母、数字、下划线、连字符和空格，超出范围或包含无效字符时抛出异常。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-EventClassifyInfo-extraInfo: string--><!--Device-EventClassifyInfo-extraInfo: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

