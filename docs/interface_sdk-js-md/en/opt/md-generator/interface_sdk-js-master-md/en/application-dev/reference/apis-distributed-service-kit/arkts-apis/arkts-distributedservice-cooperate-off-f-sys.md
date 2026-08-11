# off (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## off('cooperate')

```TypeScript
function off(type: 'cooperate', callback?: Callback<void>): void
```

Disables listening for screen hopping status change events.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** off(type:

<!--Device-cooperate-function off(type: 'cooperate', callback?: Callback<void>): void--><!--Device-cooperate-function off(type: 'cooperate', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cooperate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## off('cooperateMessage')

```TypeScript
function off(type: 'cooperateMessage', callback?: Callback<CooperateMessage>): void
```

Disables listening for screen hopping status change events.

**Since:** 11

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function off(type: 'cooperateMessage', callback?: Callback<CooperateMessage>): void--><!--Device-cooperate-function off(type: 'cooperateMessage', callback?: Callback<CooperateMessage>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cooperateMessage' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CooperateMessage&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## off('cooperateMouse')

```TypeScript
function off(type: 'cooperateMouse', networkId: string, callback?: Callback<MouseLocation>): void
```

Unregisters the listener for the mouse cursor position of a device.

**Since:** 12

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function off(type: 'cooperateMouse', networkId: string, callback?: Callback<MouseLocation>): void--><!--Device-cooperate-function off(type: 'cooperateMouse', networkId: string, callback?: Callback<MouseLocation>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cooperateMouse' | Yes |
| networkId | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MouseLocation&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
