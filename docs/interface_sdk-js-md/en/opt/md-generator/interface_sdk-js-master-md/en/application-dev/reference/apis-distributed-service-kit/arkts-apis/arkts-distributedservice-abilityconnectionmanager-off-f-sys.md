# off (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## off('receiveImage')

```TypeScript
function off(type: 'receiveImage', sessionId: number,
        callback?: Callback<EventCallbackInfo>): void
```

Unregisters receiveImage event.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function off(type: 'receiveImage', sessionId: number,        callback?: Callback<EventCallbackInfo>): void--><!--Device-abilityConnectionManager-function off(type: 'receiveImage', sessionId: number,        callback?: Callback<EventCallbackInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'receiveImage' | Yes |
| sessionId | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;EventCallbackInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';

let sessionId = 100;
abilityConnectionManager.off("receiveImage", sessionId);
```


## off('collaborateEvent')

```TypeScript
function off(type: 'collaborateEvent', sessionId: number,
        callback?: Callback<CollaborateEventInfo>): void
```

Unregisters collaborateEvent event.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function off(type: 'collaborateEvent', sessionId: number,        callback?: Callback<CollaborateEventInfo>): void--><!--Device-abilityConnectionManager-function off(type: 'collaborateEvent', sessionId: number,        callback?: Callback<CollaborateEventInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'collaborateEvent' | Yes |
| sessionId | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CollaborateEventInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';

let sessionId = 100;
abilityConnectionManager.off("collaborateEvent", sessionId);
```
