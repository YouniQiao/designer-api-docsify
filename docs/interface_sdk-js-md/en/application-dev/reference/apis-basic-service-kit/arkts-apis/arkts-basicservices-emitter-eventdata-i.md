# EventData

Describes data carried by the emitted event.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-emitter-export interface EventData--><!--Device-emitter-export interface EventData-End-->

**System capability:** SystemCapability.Notification.Emitter

## data

```TypeScript
data?: { [key: string]: any }
```

Data carried by the emitted event. The value can be in any of the following types: Array, ArrayBuffer, Boolean,DataView, Date, Error, Map, Number, Object, Primitive (except symbol), RegExp, Set, String, and TypedArray. The maximum data size is 16 MB. If the data size exceeds the limit, the event fails to be emitted.

**Type:** { [key: string]: any }

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventData-data?: { [key: string]: any }--><!--Device-EventData-data?: { [key: string]: any }-End-->

**System capability:** SystemCapability.Notification.Emitter

