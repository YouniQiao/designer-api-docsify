# off_interfaceStateChange (System API)

## Modules to Import

```TypeScript
```

## off_interfaceStateChange

```TypeScript
function off(type: 'interfaceStateChange', callback?: Callback<InterfaceStateInfo>): void
```

Unregister a callback from the ethernet interface active state change.

**Since:** 11

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function off(type: 'interfaceStateChange', callback?: Callback<InterfaceStateInfo>): void--><!--Device-ethernet-function off(type: 'interfaceStateChange', callback?: Callback<InterfaceStateInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'interfaceStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InterfaceStateInfo](arkts-network-ethernet-interfacestateinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { ethernet } from '@kit.NetworkKit';

ethernet.off('interfaceStateChange');
```
