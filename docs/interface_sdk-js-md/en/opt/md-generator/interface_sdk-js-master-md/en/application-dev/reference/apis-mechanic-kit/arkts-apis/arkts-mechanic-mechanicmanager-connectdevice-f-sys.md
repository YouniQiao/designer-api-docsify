# connectDevice (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## connectDevice

```TypeScript
function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>
```

Connecting devices based on addresses

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECT_MECHANIC_HARDWARE

**Model restriction:** This API can be used only in the stage model.

<!--Device-mechanicManager-function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>--><!--Device-mechanicManager-function connectDevice(addrInfo: AddressInfo, params: ConnectParam): Promise<AttachStateChangeInfo>-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| addrInfo | [AddressInfo](arkts-mechanic-mechanicmanager-addressinfo-i-sys.md) | Yes |
| params | [ConnectParam](arkts-mechanic-mechanicmanager-connectparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AttachStateChangeInfo](arkts-mechanic-mechanicmanager-attachstatechangeinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
