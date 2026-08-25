# off

## Modules to Import

```TypeScript
import { deviceStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## off('steadyStandingDetect')

```TypeScript
function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void
```

Unsubscribes from steady standing state events.

**Since:** 18

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'steadyStandingDetect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32500001](../errorcode-deviceStatus.md#32500001-abnormal-service) |
| [32500003](../errorcode-deviceStatus.md#32500003-unsubscription-failed) |
