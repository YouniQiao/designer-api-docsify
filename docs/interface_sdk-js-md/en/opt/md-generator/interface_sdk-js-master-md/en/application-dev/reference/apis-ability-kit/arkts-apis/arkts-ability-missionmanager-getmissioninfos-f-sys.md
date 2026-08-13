# getMissionInfos (System API)

## Modules to Import

```TypeScript
import { missionManager } from '@kit.AbilityKit';
```

## getMissionInfos

```TypeScript
function getMissionInfos(deviceId: string, numMax: number, callback: AsyncCallback<Array<MissionInfo>>): void
```

Obtains information about all missions. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: int, callback: AsyncCallback<Array<MissionInfo>>): void--><!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: int, callback: AsyncCallback<Array<MissionInfo>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| numMax | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;MissionInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  missionManager.getMissionInfos('', 10, (error: BusinessError, missions: Array<missionManager.MissionInfo>) => {
    if (error) {
      console.error(`getMissionInfos failed, error.code: ${error.code}, error.message: ${error.message}`);
    } else {
      console.info(`size = ${missions.length}`);
      console.info(`missions = ${JSON.stringify(missions)}`);
    }
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`getMissionInfos failed, error code: ${code}, error msg: ${message}.`);
}
```


## getMissionInfos

```TypeScript
function getMissionInfos(deviceId: string, numMax: number): Promise<Array<MissionInfo>>
```

Obtains information about all missions. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: int): Promise<Array<MissionInfo>>--><!--Device-missionManager-function getMissionInfos(deviceId: string, numMax: int): Promise<Array<MissionInfo>>-End-->

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
| Promise & lt;Array & lt;MissionInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  missionManager.getMissionInfos('', 10).then((data: Array<missionManager.MissionInfo>) => {
    console.info(`getMissionInfos successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`getMissionInfos failed. Cause: ${error.message}`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getMissionInfos failed. Cause: ${err.message}`);
}
```
