# PropertyReadRequest

```TypeScript
interface PropertyReadRequest
```

Represents the Property read request parameter of the client.

**Since:** 26.0.0

<!--Device-ssap-interface PropertyReadRequest--><!--Device-ssap-interface PropertyReadRequest-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

Client device address. The address format is **11:22:33:AA:BB:FF**.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyReadRequest-address: string--><!--Device-PropertyReadRequest-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## propertyUuid

```TypeScript
propertyUuid: string
```

Property UUID, in the same format as **serviceUuid**.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyReadRequest-propertyUuid: string--><!--Device-PropertyReadRequest-propertyUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## requestId

```TypeScript
requestId: number
```

Request ID. The value range is [0, 65535]. The response sent by the server must carry this ID so that the client can associate the request with the response.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PropertyReadRequest-requestId: int--><!--Device-PropertyReadRequest-requestId: int-End-->

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

<!--Device-PropertyReadRequest-serviceUuid: string--><!--Device-PropertyReadRequest-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base
