# Service

```TypeScript
interface Service
```

Represents the NearLink service.

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

Properties of a service.

**Type:** [Property](arkts-connectivity-ssap-property-i.md)[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-Service-properties: Property[]--><!--Device-Service-properties: Property[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

Indicates the UUID of the Sparkling service. The value is a string of 36 characters consisting of 32 hexadecimal digits and four hyphens(-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicates a 128-bit identifier. Starblink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-Service-serviceUuid: string--><!--Device-Service-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base
