# off_interfaceSharingStateChange (System API)

## Modules to Import

```TypeScript
import { sharing } from '@kit.NetworkKit';
```

## off_interfaceSharingStateChange('interfaceSharingStateChange')

```TypeScript
function off(type: 'interfaceSharingStateChange', callback?: Callback<InterfaceSharingStateInfo>): void
```

Unsubscribes from network sharing state changes of a specified NIC. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function off(type: 'interfaceSharingStateChange', callback?: Callback<InterfaceSharingStateInfo>): void--><!--Device-sharing-function off(type: 'interfaceSharingStateChange', callback?: Callback<InterfaceSharingStateInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'interfaceSharingStateChange' | Yes | Event type. The value **interfaceSharingStateChange** indicates a network sharing status change event of the NIC. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[InterfaceSharingStateInfo](arkts-network-sharing-interfacesharingstateinfo-i-sys.md)&gt; | No | Callback used to return the result.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { sharing } from '@kit.NetworkKit';

sharing.off('interfaceSharingStateChange', (data: object) => {
  console.info(JSON.stringify(data));
});
```

