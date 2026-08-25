# ConnectResult

Represents the connection result, which is returned after the client calls **connect()**.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { linkEnhance } from '@kit.DistributedServiceKit';
```

## deviceId

```TypeScript
deviceId: string
```

ID of the peer device. If the connection is successful, the device ID of the peer device is returned. If the connection fails, an empty string is returned.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## reason

```TypeScript
reason: int
```

Number indicating the result code. If the connection is successful, **0** is returned. If the connection fails, an error code is returned:  
- 32390200: The client connection times out. - 32390201: The server service is not started. - 32390300: Internal error.  
For details about the error codes, see [Link Enhancement Error Codes](../errorcode-link-enhance.md).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## success

```TypeScript
success: boolean
```

Connection result. The value **true** indicates that the connection is successful, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration
