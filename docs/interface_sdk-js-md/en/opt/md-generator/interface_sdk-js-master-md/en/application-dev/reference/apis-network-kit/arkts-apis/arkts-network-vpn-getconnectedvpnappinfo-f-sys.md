# getConnectedVpnAppInfo (System API)

## Modules to Import

```TypeScript
import { vpn } from '@kit.NetworkKit';
```

## getConnectedVpnAppInfo

```TypeScript
function getConnectedVpnAppInfo(): Promise<Array<string>>
```

Get the connected VPN App Info.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getConnectedVpnAppInfo(): Promise<Array<string>>--><!--Device-vpn-function getConnectedVpnAppInfo(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [19900002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-vpn.md#19900002-system-internal-error) |
| [19900001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-vpn.md#19900001-invalid-parameter) |
