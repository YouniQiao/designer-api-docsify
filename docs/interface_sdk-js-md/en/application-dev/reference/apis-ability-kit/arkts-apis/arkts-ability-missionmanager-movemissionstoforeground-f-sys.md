# moveMissionsToForeground (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## moveMissionsToForeground

```TypeScript
function moveMissionsToForeground(missionIds: Array<int>, callback: AsyncCallback<void>): void
```

将指定任务批量切到前台。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function moveMissionsToForeground(missionIds: Array<int>, callback: AsyncCallback<void>): void--><!--Device-missionManager-function moveMissionsToForeground(missionIds: Array<int>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionIds | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | 任务ID数组。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | 执行结果回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

## Examples

```TypeScript
import { abilityManager, missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  missionManager.getMissionInfos("", 10, (error: BusinessError, missionInfos: Array<missionManager.MissionInfo>) => {
    if (error.code) {
      console.error(`getMissionInfos failed, error code: ${error.code}, error msg: ${error.message}.`);
      return;
    }
    if (missionInfos.length < 1) {
      return;
    }

    let toShows = new Array<number>();
    for (let missionInfo of missionInfos) {
      if (missionInfo.abilityState == abilityManager.AbilityState.BACKGROUND) {
        toShows.push(missionInfo.missionId);
      }
    }
    missionManager.moveMissionsToForeground(toShows, (err: BusinessError, data: void) => {
      if (err) {
        console.error(`moveMissionsToForeground failed: ${err.message}`);
      } else {
        console.info(`moveMissionsToForeground successfully: ${JSON.stringify(data)}`);
      }
    });
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message} `);
}
```


## moveMissionsToForeground

```TypeScript
function moveMissionsToForeground(missionIds: Array<int>, topMission: int, callback: AsyncCallback<void>): void
```

将指定任务批量切换到前台，并将任务ID等于topMission的任务移动到最顶层。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function moveMissionsToForeground(missionIds: Array<int>, topMission: int, callback: AsyncCallback<void>): void--><!--Device-missionManager-function moveMissionsToForeground(missionIds: Array<int>, topMission: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionIds | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | 任务ID数组。 |
| topMission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 待移动到最顶层的任务ID |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | 执行结果回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

## Examples

```TypeScript
import { abilityManager, missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  missionManager.getMissionInfos("", 10, (error: BusinessError, missionInfos: Array<missionManager.MissionInfo>) => {
    if (error.code) {
      console.error(`getMissionInfos failed, error code: ${error.code}, error msg: ${error.message}.`);
      return;
    }
    if (missionInfos.length < 1) {
      return;
    }

    let toShows = new Array<number>();
    for (let missionInfo of missionInfos) {
      if (missionInfo.abilityState == abilityManager.AbilityState.BACKGROUND) {
        toShows.push(missionInfo.missionId);
      }
    }
    missionManager.moveMissionsToForeground(toShows, toShows[0], (err: BusinessError, data: void) => {
      if (err) {
        console.error(`moveMissionsToForeground failed: ${err.message}`);
      } else {
        console.info(`moveMissionsToForeground successfully`);
      }
    });
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message} `);
}
```


## moveMissionsToForeground

```TypeScript
function moveMissionsToForeground(missionIds: Array<int>, topMission?: int): Promise<void>
```

将指定任务批量切到前台，并将任务ID等于topMission的任务移动到最顶层。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function moveMissionsToForeground(missionIds: Array<int>, topMission?: int): Promise<void>--><!--Device-missionManager-function moveMissionsToForeground(missionIds: Array<int>, topMission?: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionIds | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | 任务ID数组。 |
| topMission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 待移动到最顶层的任务ID。默认值为-1，表示将默认任务移动到最顶层。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

## Examples

```TypeScript
import { abilityManager, missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  missionManager.getMissionInfos("", 10, (error: BusinessError, missionInfos: Array<missionManager.MissionInfo>) => {
    if (error.code) {
      console.error(`getMissionInfos failed, error code: ${error.code}, error msg: ${error.message}`);
      return;
    }
    if (missionInfos.length < 1) {
      return;
    }

    let toShows = new Array<number>();
    for (let missionInfo of missionInfos) {
      if (missionInfo.abilityState == abilityManager.AbilityState.BACKGROUND) {
        toShows.push(missionInfo.missionId);
      }
    }
    missionManager.moveMissionsToForeground(toShows, toShows[0]).then(() => {
      console.info(`moveMissionsToForeground is called`);
    });
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message} `);
}
```

