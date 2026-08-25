# getMissionInfo (System API)

## Modules to Import

```TypeScript
```

## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: number, callback: AsyncCallback<MissionInfo>): void
```

Obtains the information about a given mission. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-f-sys.md)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| missionId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[MissionInfo](arkts-ability-missioninfo-i-sys.md)&gt; | Yes |

**Examples**

```TypeScript
import missionManager from '@ohos.application.missionManager';

let missionId: number = 0;

missionManager.getMissionInfo('', missionId, (error, mission) => {
  if (error.code) {
    console.error(`getMissionInfo failed, error.code: ${error.code}, error.message: ${error.message}`);
    return;
  }

  console.info(`mission.missionId = ${mission.missionId}`);
  console.info(`mission.runningState = ${mission.runningState}`);
  console.info(`mission.lockedState = ${mission.lockedState}`);
  console.info(`mission.timestamp = ${mission.timestamp}`);
  console.info(`mission.label = ${mission.label}`);
  console.info(`mission.iconPath = ${mission.iconPath}`);
});
```

```TypeScript
import missionManager from '@ohos.application.missionManager';
import { BusinessError } from '@ohos.base';

let testMissionId = 1;
try {
  missionManager.getMissionInfo('', testMissionId).then((data) => {
    console.info(`getMissionInfo successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`getMissionInfo failed. Cause: ${error.message}`);
  });
} catch (error) {
  console.error(`getMissionInfo failed. Cause: ${error.message}`);
}
```


## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: number): Promise<MissionInfo>
```

Obtains the information about a given mission. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-f-sys.md)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| missionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MissionInfo](arkts-ability-missioninfo-i-sys.md)&gt; |

**Examples**

See [getMissionInfo](#getmissioninfo)
