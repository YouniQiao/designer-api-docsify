# addVlanIp (System API)

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## addVlanIp

```TypeScript
function addVlanIp(ifName: string, vlanId: number, address: LinkAddress): Promise<void>
```

Adds a specified IP address and subnet mask for the VLAN specified by **vlanId** on an Ethernet NIC. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Currently, this API supports only the PC. For other device types, the error code 2100002 is returned when this
> API is called.

**Since:** 23

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ifName | string | Yes |
| vlanId | number | Yes |
| address | [LinkAddress](arkts-network-vpnextension-linkaddress-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2100400](../errorcode-net-connection.md#2100400-incorrect-nic-name-non-ethernet) |
