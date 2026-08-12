# destroyVlanInterface (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## destroyVlanInterface

```TypeScript
function destroyVlanInterface(ifName: string, vlanId: number): Promise<void>
```

Destroy vlan interface by vlanId.To invoke this method, you must have the {@code ohos.permission.CONNECTIVITY_INTERNAL} permission.

**Since:** 23

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function destroyVlanInterface(ifName: string, vlanId: int): Promise<void>--><!--Device-connection-function destroyVlanInterface(ifName: string, vlanId: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ifName | string | Yes |
| vlanId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100400](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100400-incorrect-nic-name-nonethernet) |
| [2100002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let ifName = "eth0";
let vlanId = 1;
connection.destroyVlanInterface(ifName, vlanId).then(() => {
  console.info(`Destroy vlan success`);
}).catch((error: BusinessError) => {
  console.error(`Failed to destroy vlan. Code:${error.code}, message:${error.message}`);
});
```
