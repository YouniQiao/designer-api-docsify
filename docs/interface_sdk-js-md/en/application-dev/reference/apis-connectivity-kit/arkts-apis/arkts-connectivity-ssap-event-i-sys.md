# Event (System API)

```TypeScript
interface Event
```

Represents a service event.

**Since:** 26.0.0

<!--Device-ssap-interface Event--><!--Device-ssap-interface Event-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## eventUuid

```TypeScript
eventUuid: string
```

Event UUID. The data format is the same as that of **serviceUuid**.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-Event-eventUuid: string--><!--Device-Event-eventUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

## parameter

```TypeScript
parameter?: ArrayBuffer
```

Event parameters. The data format is defined by the specific service. By default, this field is not used if not set.

**Type:** ArrayBuffer

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-Event-parameter?: ArrayBuffer--><!--Device-Event-parameter?: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

## serviceUuid

```TypeScript
serviceUuid: string
```

Indicates the UUID of the Sparkling service. The value is a string of 36 characters consisting of 32 hexadecimal digits and four hyphens(-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicates a 128-bit identifier. Starblink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-Event-serviceUuid: string--><!--Device-Event-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.
