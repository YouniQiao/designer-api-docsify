# DataParams

Describes the parameters for Data.

**Since:** 26.0.0

<!--Device-dataTransfer-interface DataParams--><!--Device-dataTransfer-interface DataParams-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

Indicates the connected device address.The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataParams-address: string--><!--Device-DataParams-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## data

```TypeScript
data: ArrayBuffer
```

Indicates the data buffer.

**Type:** ArrayBuffer

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataParams-data: ArrayBuffer--><!--Device-DataParams-data: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## uuid

```TypeScript
uuid: string
```

Indicates the service UUID.The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.<br>NearLink standard UUIDs are not allowed.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataParams-uuid: string--><!--Device-DataParams-uuid: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

