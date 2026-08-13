# createClient

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## createClient

```TypeScript
function createClient(address: string): Client
```

Creates a SSAP client instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ssap-function createClient(address: string): Client--><!--Device-ssap-function createClient(address: string): Client-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string | Yes | Indicates the device address of a server &lt;br&gt;The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF. |

**Return value:**

| Type | Description |
| --- | --- |
| [Client](arkts-connectivity-ssap-client-i.md) | Returns a SSAP client instance { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100041 | Invalid address. |

