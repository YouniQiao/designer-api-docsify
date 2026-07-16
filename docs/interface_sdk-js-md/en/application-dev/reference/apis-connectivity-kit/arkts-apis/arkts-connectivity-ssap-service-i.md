# Service

Describes the SSAP service.

**Since:** 26.0.0

<!--Device-ssap-interface Service--><!--Device-ssap-interface Service-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## properties

```TypeScript
properties: Property[]
```

The properties belong to this service.

**Type:** Property[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Service-properties: Property[]--><!--Device-Service-properties: Property[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service.The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.<br>NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Service-serviceUuid: string--><!--Device-Service-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

