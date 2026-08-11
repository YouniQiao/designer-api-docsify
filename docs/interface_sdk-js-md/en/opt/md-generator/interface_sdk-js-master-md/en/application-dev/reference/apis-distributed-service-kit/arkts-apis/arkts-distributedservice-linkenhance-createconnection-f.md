# createConnection

## Modules to Import

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## createConnection

```TypeScript
function createConnection(deviceId: string, name: string): Connection
```

Creates a **Connection** object on the device that functions as the client. The device can then initiate connection requests to the device that functions as the server.

**Since:** 20

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-linkEnhance-function createConnection(deviceId: string, name: string): Connection--><!--Device-linkEnhance-function createConnection(deviceId: string, name: string): Connection-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Connection](arkts-distributedservice-linkenhance-connection-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [32390206](../../apis-distributedservice-kit/errorcode-link-enhance.md#32390206-invalid-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

On the device that functions as the client, call the createConnection() to create a Connection object.

```TypeScript
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55"; // BLE MAC address, which needs to be obtained through Bluetooth scanning. For details, see parameter description.
  hilog.info(0x0000, TAG, 'connection server deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```
