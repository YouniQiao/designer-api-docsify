# ConnectResult

Represents the connection result, which is returned after the client calls **connect()**.

**Since:** 23

<!--Device-linkEnhance-interface ConnectResult--><!--Device-linkEnhance-interface ConnectResult-End-->

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

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-deviceId: string--><!--Device-ConnectResult-deviceId: string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## reason

```TypeScript
reason: int
```

Number indicating the result code. If the connection is successful, **0** is returned. If the connection fails, an error code is returned: - 32390200: The client connection times out. - 32390201: The server service is not started. - 32390300: Internal error. For details about the error codes, see [Link Enhancement Error Codes](../../apis-distributedservice-kit/errorcode-link-enhance.md).

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-reason: int--><!--Device-ConnectResult-reason: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## success

```TypeScript
success: boolean
```

Connection result. The value **true** indicates that the connection is successful, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectResult-success: boolean--><!--Device-ConnectResult-success: boolean-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

