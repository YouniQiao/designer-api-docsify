# off

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## off('deviceSelected')

```TypeScript
function off(type: 'deviceSelected', token: number): void
```

Unsubscribes from device connection events.

**Since:** 9

**Deprecated since:** 22

**Substitutes:** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function off(type: 'deviceSelected', token: number): void--><!--Device-continuationManager-function off(type: 'deviceSelected', token: number): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceSelected' | Yes |
| token | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16600004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600004-the-specified-callback-has-been-registered) |
| [16600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceSelected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```


## off('deviceUnselected')

```TypeScript
function off(type: 'deviceUnselected', token: number): void
```

Unsubscribes from device disconnection events.

**Since:** 9

**Deprecated since:** 22

**Substitutes:** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function off(type: 'deviceUnselected', token: number): void--><!--Device-continuationManager-function off(type: 'deviceUnselected', token: number): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceUnselected' | Yes |
| token | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16600004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600004-the-specified-callback-has-been-registered) |
| [16600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) |
| [16600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceUnselected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```


## off('deviceConnect')

```TypeScript
function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void
```

Unsubscribes from device connection events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void--><!--Device-continuationManager-function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceConnect' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinuationResult&gt; | No |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```


## off('deviceDisconnect')

```TypeScript
function off(type: 'deviceDisconnect', callback?: Callback<string>): void
```

Unsubscribes from device disconnection events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function off(type: 'deviceDisconnect', callback?: Callback<string>): void--><!--Device-continuationManager-function off(type: 'deviceDisconnect', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceDisconnect' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```
