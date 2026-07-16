# ServiceData

Describes the service data.

**Since:** 26.0.0

<!--Device-advertising-interface ServiceData--><!--Device-advertising-interface ServiceData-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { advertising } from '@kit.ConnectivityKit';
```

## serviceData

```TypeScript
serviceData: ArrayBuffer
```

Indicates the service data.

**Type:** ArrayBuffer

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceData-serviceData: ArrayBuffer--><!--Device-ServiceData-serviceData: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## serviceUuid

```TypeScript
serviceUuid: string
```

Indicates the service UUID.The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceData-serviceUuid: string--><!--Device-ServiceData-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

