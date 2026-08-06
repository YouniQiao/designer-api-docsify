# off (System API)

## off('interfaceStateChange')

```TypeScript
function off(type: 'interfaceStateChange', callback?: Callback<InterfaceStateInfo>): void
```

Unregister a callback from the ethernet interface active state change.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function off(type: 'interfaceStateChange', callback?: Callback<InterfaceStateInfo>): void--><!--Device-ethernet-function off(type: 'interfaceStateChange', callback?: Callback<InterfaceStateInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'interfaceStateChange' | Yes | Indicates Event name. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;InterfaceStateInfo&gt; | No | Including iface Indicates the ethernet interface, and active Indicates whether the interface is active. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |

**Example**

```TypeScript
import { ethernet } from '@kit.NetworkKit';

ethernet.off('interfaceStateChange');
```

