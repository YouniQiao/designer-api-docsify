# clearMission (System API)

## clearMission

```TypeScript
function clearMission(missionId: number, callback: AsyncCallback<void>): void
```

清理指定任务id的任务，无论该任务是否被锁定。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.missionManager/missionManager#clearMission

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function clearMission(missionId: number, callback: AsyncCallback<void>): void--><!--Device-missionManager-function clearMission(missionId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionId | number | Yes | 任务ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当清理指定任务id的任务成功，err为undefined，否则为错误对象。 |

## Examples

```TypeScript
import missionManager from '@ohos.application.missionManager';

let testMissionId = 2;
try {
  missionManager.clearMission(testMissionId, (err, data) => {
    if (err) {
      console.error(`clearMission failed: ${err.message}`);
    } else {
      console.info(`clearMission successfully: ${JSON.stringify(data)}`);
    }
  });
} catch (err) {
  console.error(`clearMission failed: ${err.message}`);
}
```


## clearMission

```TypeScript
function clearMission(missionId: number): Promise<void>
```

清理指定任务id的任务，无论该任务是否被锁定。使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.missionManager/missionManager#clearMission

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function clearMission(missionId: number): Promise<void>--><!--Device-missionManager-function clearMission(missionId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionId | number | Yes | 任务ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## Examples

```TypeScript
import missionManager from '@ohos.application.missionManager';
import { BusinessError } from '@ohos.base';

let testMissionId = 2;
try {
  missionManager.clearMission(testMissionId).then((data) => {
    console.info(`clearMission successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`clearMission failed. Cause: ${error.message}`);
  });
} catch (error) {
  console.error(`clearMission failed. Cause: ${error.message}`);
}
```

