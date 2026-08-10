# EventData

发送事件时传递的数据。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-emitter-export interface EventData--><!--Device-emitter-export interface EventData-End-->

**System capability:** SystemCapability.Notification.Emitter

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## data

```TypeScript
data?: { [key: string]: any }
```

发送事件时传递的数据，支持数据类型包括Array、ArrayBuffer、Boolean、DataView、Date、Error、Map、Number、Object、Primitive（除了symbol）、RegExp、Set、String、TypedArray，数据大小最大为16MB，超出限制时事件发送失败。

**Type:** { [key: string]: any }

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventData-data?: { [key: string]: any }--><!--Device-EventData-data?: { [key: string]: any }-End-->

**System capability:** SystemCapability.Notification.Emitter

