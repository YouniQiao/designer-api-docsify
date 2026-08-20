# on_interfaceSharingStateChange (System API)

## Modules to Import

```TypeScript
import { sharing } from '@kit.NetworkKit';
```

## on('interfaceSharingStateChange')

```TypeScript
function on(type: 'interfaceSharingStateChange', callback: Callback<InterfaceSharingStateInfo>): void
```

Subscribes to network sharing state changes of a specified NIC. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function on(type: 'interfaceSharingStateChange', callback: Callback<InterfaceSharingStateInfo>): void--><!--Device-sharing-function on(type: 'interfaceSharingStateChange', callback: Callback<InterfaceSharingStateInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'interfaceSharingStateChange' | Yes | Event type.<br/> The value **interfaceSharingStateChange** indicates a network sharing status change event of the NIC. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[InterfaceSharingStateInfo](arkts-network-sharing-interfacesharingstateinfo-i-sys.md)&gt; | Yes | Callback used to return the result. It is called when the network sharing state of a specified NIC changes.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |

**Examples**

```TypeScript
import { sharing } from '@kit.NetworkKit';

sharing.on('interfaceSharingStateChange', (data: object) => {
  console.info('on interfaceSharingStateChange:' + JSON.stringify(data));
});
```

