# on (System API)

## Modules to Import

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## on('interfaceStateChange')

```TypeScript
function on(type: 'interfaceStateChange', callback: Callback<InterfaceStateInfo>): void
```

Register a callback for the ethernet interface active state change.

**Since:** 11

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function on(type: 'interfaceStateChange', callback: Callback<InterfaceStateInfo>): void--><!--Device-ethernet-function on(type: 'interfaceStateChange', callback: Callback<InterfaceStateInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'interfaceStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;InterfaceStateInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { ethernet } from '@kit.NetworkKit';

ethernet.on('interfaceStateChange', (data: object) => {
  console.info('on interfaceSharingStateChange: ' + JSON.stringify(data));
});
```
