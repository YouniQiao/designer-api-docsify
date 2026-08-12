# disableEthernetInterface (System API)

## Modules to Import

```TypeScript
import { ethernet } from '@kit.NetworkKit';
```

## disableEthernetInterface

```TypeScript
function disableEthernetInterface(): Promise<void>
```

Disable the ethernet interface.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-ethernet-function disableEthernetInterface(): Promise<void>--><!--Device-ethernet-function disableEthernetInterface(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
