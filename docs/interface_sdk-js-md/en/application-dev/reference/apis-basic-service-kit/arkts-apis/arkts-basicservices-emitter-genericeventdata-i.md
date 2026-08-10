# GenericEventData

发送事件时传递的泛型数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-emitter-export interface GenericEventData<T>--><!--Device-emitter-export interface GenericEventData<T>-End-->

**System capability:** SystemCapability.Notification.Emitter

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## data

```TypeScript
data?: T
```

发送事件时传递的数据。T：泛型类型，由开发者根据业务需要自定义具体的数据类型。

**Type:** T

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GenericEventData-data?: T--><!--Device-GenericEventData-data?: T-End-->

**System capability:** SystemCapability.Notification.Emitter

