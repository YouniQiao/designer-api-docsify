# getDeviceMacAddress (System API)

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getDeviceMacAddress

```TypeScript
function getDeviceMacAddress(): string[]
```

Obtains the MAC address of a Wi-Fi device. Wi-Fi must be enabled.<p>The MAC address is unique and cannot be changed.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getDeviceMacAddress](arkts-connectivity-wifimanager-getdevicemacaddress-f.md)

**Required permissions:** ohos.permission.GET_WIFI_LOCAL_MAC and ohos.permission.GET_WIFI_INFO

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |
