# unlockMission (System API)

## Modules to Import

```TypeScript
import { missionManager } from '@kit.AbilityKit';
```

## unlockMission

```TypeScript
function unlockMission(missionId: number, callback: AsyncCallback<void>): void
```

Unlocks a given mission. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function unlockMission(missionId: int, callback: AsyncCallback<void>): void--><!--Device-missionManager-function unlockMission(missionId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| missionId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16300001](../errorcode-ability.md#16300001-nonexistent-mission) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testMissionId = 2;

try {
  missionManager.unlockMission(testMissionId, (err: BusinessError, data: void) => {
    if (err) {
      console.error(`unlockMission failed: ${err.message}`);
    } else {
      console.info(`unlockMission successfully: ${JSON.stringify(data)}`);
    }
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`unlockMission failed: ${err.message}`);
}
```


## unlockMission

```TypeScript
function unlockMission(missionId: number): Promise<void>
```

Unlocks a given mission. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function unlockMission(missionId: int): Promise<void>--><!--Device-missionManager-function unlockMission(missionId: int): Promise<void>-End-->

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

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16300001](../errorcode-ability.md#16300001-nonexistent-mission) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testMissionId = 2;

try {
  missionManager.unlockMission(testMissionId).then((data: void) => {
    console.info(`unlockMission successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`unlockMission failed. Cause: ${error.message}`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`unlockMission failed. Cause: ${err.message}`);
}
```
