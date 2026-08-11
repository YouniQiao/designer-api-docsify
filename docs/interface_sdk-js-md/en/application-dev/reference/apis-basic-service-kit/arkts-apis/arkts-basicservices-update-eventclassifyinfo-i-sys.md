# EventClassifyInfo (System API)

Represents event type information.

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

Event type, which specifies the type of event to listen for. The value can be **TASK**, indicating a task event.

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

Additional information, which is used to transfer the extended data. The default value is an empty string, indicating that there is no additional information. The value is a string of 0 to 128 characters. The value can contain letters, digits, underscores (_), hyphens (-), and spaces. If the value is out of range or contains invalid characters, an exception is thrown.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-EventClassifyInfo-extraInfo: string--><!--Device-EventClassifyInfo-extraInfo: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

