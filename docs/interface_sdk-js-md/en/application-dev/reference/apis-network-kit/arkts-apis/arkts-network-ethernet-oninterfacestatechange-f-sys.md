# on_interfaceStateChange (System API)

## Modules to Import

```TypeScript
import { ethernet } from 'ethernet';
```

## on_interfaceStateChange

```TypeScript
function on(type: 'interfaceStateChange', callback: Callback<InterfaceStateInfo>): void
```

Register a callback for the ethernet interface active state change.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function on(type: 'interfaceStateChange', callback: Callback<InterfaceStateInfo>): void--><!--Device-ethernet-function on(type: 'interfaceStateChange', callback: Callback<InterfaceStateInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'interfaceStateChange' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterfaceStateInfo](arkts-network-ethernet-interfacestateinfo-i-sys.md)&gt; | Yes | Including iface Indicates the ethernet interface, and active Indicates whether the interface is active. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { ethernet } from '@kit.NetworkKit';

ethernet.on('interfaceStateChange', (data: object) => {
  console.info('on interfaceSharingStateChange: ' + JSON.stringify(data));
});
```

