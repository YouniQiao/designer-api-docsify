# unregisterMissionListener (System API)

## unregisterMissionListener

```TypeScript
function unregisterMissionListener(listenerId: number, callback: AsyncCallback<void>): void
```

Unregisters a mission status listener. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.missionManager/missionManager#off

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function unregisterMissionListener(listenerId: number, callback: AsyncCallback<void>): void--><!--Device-missionManager-function unregisterMissionListener(listenerId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| listenerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import missionManager from '@ohos.application.missionManager';

console.info('registerMissionListener');
let listenerId = missionManager.registerMissionListener({
  onMissionCreated: (mission) => {
    console.info('--------onMissionCreated-------');
  },
  onMissionDestroyed: (mission) => {
    console.info('--------onMissionDestroyed-------');
  },
  onMissionSnapshotChanged: (mission) => {
    console.info('--------onMissionSnapshotChanged-------');
  },
  onMissionMovedToFront: (mission) => {
    console.info('--------onMissionMovedToFront-------');
  },
  onMissionIconUpdated: (mission, icon) => {
    console.info('--------onMissionIconUpdated-------');
  },
  onMissionClosed: (mission) => {
    console.info('--------onMissionClosed-------');
  },
  onMissionLabelUpdated: (mission) => {
    console.info('--------onMissionLabelUpdated-------');
  }
});

missionManager.unregisterMissionListener(listenerId, (error) => {
  console.error(`unregisterMissionListener fail, error: ${JSON.stringify(error)}`);
});
```


## unregisterMissionListener

```TypeScript
function unregisterMissionListener(listenerId: number): Promise<void>
```

Unregisters a mission status listener. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.missionManager/missionManager#off

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function unregisterMissionListener(listenerId: number): Promise<void>--><!--Device-missionManager-function unregisterMissionListener(listenerId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| listenerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import missionManager from '@ohos.application.missionManager';
import { BusinessError } from '@ohos.base';

console.info('registerMissionListener');
let listenerId = missionManager.registerMissionListener({
  onMissionCreated: (mission) => {
    console.info('--------onMissionCreated-------');
  },
  onMissionDestroyed: (mission) => {
    console.info('--------onMissionDestroyed-------');
  },
  onMissionSnapshotChanged: (mission) => {
    console.info('--------onMissionSnapshotChanged-------');
  },
  onMissionMovedToFront: (mission) => {
    console.info('--------onMissionMovedToFront-------');
  },
  onMissionIconUpdated: (mission, icon) => {
    console.info('--------onMissionIconUpdated-------');
  },
  onMissionClosed: (mission) => {
    console.info('--------onMissionClosed-------');
  },
  onMissionLabelUpdated: (mission) => {
    console.info('--------onMissionLabelUpdated-------');
  }
});

missionManager.unregisterMissionListener(listenerId)
  .then(() => {
    console.info(`UnregisterMissionListener success.`)
  })
  .catch((error: BusinessError) => {
    console.error(`UnregisterMissionListener fail, error: ${JSON.stringify(error)}.`);
  });
```
