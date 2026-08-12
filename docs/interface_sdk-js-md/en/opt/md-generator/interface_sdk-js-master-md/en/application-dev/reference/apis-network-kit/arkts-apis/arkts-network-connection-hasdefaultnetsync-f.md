# hasDefaultNetSync

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## hasDefaultNetSync

```TypeScript
function hasDefaultNetSync(): boolean
```

Checks whether the default data network is activated.

**Since:** 10

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function hasDefaultNetSync(): boolean--><!--Device-connection-function hasDefaultNetSync(): boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let hasDefaultNet = connection.hasDefaultNetSync();
```
