# getMissionInfos (System API)

## Modules to Import

```TypeScript
```

## getMissionInfos

```TypeScript
function getMissionInfos(deviceId: string, numMax: number, callback: AsyncCallback<Array<MissionInfo>>): void
```

Obtains information about all missions. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getMissionInfos](arkts-ability-missionmanager-getmissioninfos-f-sys.md#getmissioninfos-system-api)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: number, callback: AsyncCallback<Array<MissionInfo>>): void--><!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: number, callback: AsyncCallback<Array<MissionInfo>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| numMax | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MissionInfo](arkts-ability-missioninfo-i-sys.md)&gt;&gt; | Yes |

**Examples**

```TypeScript
import missionManager from '@ohos.application.missionManager';

missionManager.getMissionInfos('', 10, (error, missions) => {
  if (error.code) {
    console.error(`getMissionInfos failed, error.code: ${error.code}, error.message: ${error.message}`);
    return;
  }
  console.info(`size = ${missions.length}`);
  console.info(`missions = ${JSON.stringify(missions)}`);
});
```


## getMissionInfos

```TypeScript
function getMissionInfos(deviceId: string, numMax: number): Promise<Array<MissionInfo>>
```

Obtains information about all missions. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getMissionInfos](arkts-ability-missionmanager-getmissioninfos-f-sys.md#getmissioninfos-system-api)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: number): Promise<Array<MissionInfo>>--><!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: number): Promise<Array<MissionInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| numMax | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MissionInfo](arkts-ability-missioninfo-i-sys.md)&gt;&gt; |

**Examples**

```TypeScript
import missionManager from '@ohos.application.missionManager';
import { BusinessError } from '@ohos.base';

try {
  missionManager.getMissionInfos('', 10).then((data) => {
    console.info(`getMissionInfos successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`getMissionInfos failed. Cause: ${error.message}`);
  });
} catch (error) {
  console.error(`getMissionInfos failed. Cause: ${error.message}`);
}
```
