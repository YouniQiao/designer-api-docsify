# unlockMission (System API)

## unlockMission

```TypeScript
function unlockMission(missionId: number, callback: AsyncCallback<void>): void
```

Unlocks a given mission. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [unlockMission](arkts-ability-missionmanager-unlockmission-f-sys.md#unlockMission-(System-API))

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function unlockMission(missionId: number, callback: AsyncCallback<void>): void--><!--Device-missionManager-function unlockMission(missionId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| missionId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import missionManager from '@ohos.application.missionManager';

let testMissionId = 2;
try {
  missionManager.unlockMission(testMissionId, (err, data) => {
    if (err) {
      console.error(`unlockMission failed: ${err.message}`);
    } else {
      console.info(`unlockMission successfully: ${JSON.stringify(data)}`);
    }
  });
} catch (err) {
  console.error(`unlockMission failed: ${err.message}`);
}
```


## unlockMission

```TypeScript
function unlockMission(missionId: number): Promise<void>
```

Unlocks a given mission. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [unlockMission](arkts-ability-missionmanager-unlockmission-f-sys.md#unlockMission-(System-API))

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function unlockMission(missionId: number): Promise<void>--><!--Device-missionManager-function unlockMission(missionId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| missionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
import missionManager from '@ohos.application.missionManager';
import { BusinessError } from '@ohos.base';

let testMissionId = 2;
try {
  missionManager.unlockMission(testMissionId).then((data) => {
    console.info(`unlockMission successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`unlockMission failed. Cause: ${error.message}`);
  });
} catch (error) {
  console.error(`unlockMission failed. Cause: ${error.message}`);
}
```
