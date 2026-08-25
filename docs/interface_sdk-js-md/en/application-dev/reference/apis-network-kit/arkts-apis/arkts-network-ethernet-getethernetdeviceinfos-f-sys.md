# getEthernetDeviceInfos (System API)

## Modules to Import

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## getEthernetDeviceInfos

```TypeScript
function getEthernetDeviceInfos(): Promise<Array<EthernetDeviceInfos>>
```

Obtains the device information (such as the vendor name, product name, and maximum connection rate) of the local Ethernet NIC. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[EthernetDeviceInfos](arkts-network-ethernet-ethernetdeviceinfos-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2201005](../errorcode-net-ethernet.md#2201005-device-information-not-exist) |
