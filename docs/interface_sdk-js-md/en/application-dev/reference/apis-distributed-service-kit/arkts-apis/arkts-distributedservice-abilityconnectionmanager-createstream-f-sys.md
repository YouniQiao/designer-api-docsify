# createStream (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## createStream

```TypeScript
function createStream(sessionId: number, param: StreamParam): Promise<number>
```

Creating a Stream.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| param | [StreamParam](arkts-distributedservice-abilityconnectionmanager-streamparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [32300001](../errorcode-device-manager.md#32300001-transport-stream-repeatedly-created) |
| [32300003](../errorcode-device-manager.md#32300003-bit-rate-not-supported) |
| [32300004](../errorcode-device-manager.md#32300004-color-space-not-supported) |
