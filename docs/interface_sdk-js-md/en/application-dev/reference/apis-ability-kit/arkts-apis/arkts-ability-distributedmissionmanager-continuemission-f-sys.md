# continueMission (System API)

## Modules to Import

```TypeScript
import { distributedMissionManager } from 'kits/@kit.AbilityKit';
```

## continueMission

```TypeScript
function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback, callback: AsyncCallback<void>): void
```

通过指定任务ID（missionId）的方式进行迁移任务。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback, callback: AsyncCallback<void>): void--><!--Device-distributedMissionManager-function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [ContinueDeviceInfo](arkts-ability-distributedmissionmanager-continuedeviceinfo-t-sys.md) | Yes | 迁移信息。 |
| options | [ContinueCallback](arkts-ability-distributedmissionmanager-continuecallback-t-sys.md) | Yes | 迁移任务完成回调函数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，迁移任务完成时，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16300504 | The application is not installed on the remote end but installation-free is supported, try again with freeInstall flag. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 16300505 | The operation device must be the device where the application to be continuedis located or the target device to be continued. |
| 16300506 | The local continuation task is already in progress. |
| 201 | Permission denied. |
| 202 | The application is not system-app, can not use system-api. |
| 16300501 | The system ability work abnormally. |
| 16300502 | Failed to get the missionInfo of the specified missionId. |
| 16300503 | The application is not installed on the remote end and installation-free isnot supported. |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Implement a callback function.
function onContinueDone(resultCode: number): void {
  console.info('onContinueDone resultCode: ' + JSON.stringify(resultCode));
};
try {
  // Call continueMission.
  distributedMissionManager.continueMission(
    {
      srcDeviceId: "",
      dstDeviceId: "",
      missionId: 1,
      wantParam: {"key": "value"}
    },
    { onContinueDone: onContinueDone },
    (error: BusinessError) => {
      if (error) {
        console.error('continueMission failed, cause: ' + JSON.stringify(error));
        return;
      }
      console.info('continueMission finished');
  })
} catch (error) {
  console.error('continueMission failed, cause: ' + JSON.stringify(error));
}
```


## continueMission

```TypeScript
function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback): Promise<void>
```

通过指定任务ID（missionId）的方式进行迁移任务。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback): Promise<void>--><!--Device-distributedMissionManager-function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [ContinueDeviceInfo](arkts-ability-distributedmissionmanager-continuedeviceinfo-t-sys.md) | Yes | 迁移信息。 |
| options | [ContinueCallback](arkts-ability-distributedmissionmanager-continuecallback-t-sys.md) | Yes | 迁移任务完成回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16300504 | The application is not installed on the remote end but installation-free is supported, try again with freeInstall flag. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 16300505 | The operation device must be the device where the application to be continuedis located or the target device to be continued. |
| 16300506 | The local continuation task is already in progress. |
| 201 | Permission denied. |
| 202 | The application is not system-app, can not use system-api. |
| 16300501 | The system ability work abnormally. |
| 16300502 | Failed to get the missionInfo of the specified missionId. |
| 16300503 | The application is not installed on the remote end and installation-free isnot supported. |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Implement a callback function.
function onContinueDone(resultCode: number): void {
  console.info('onContinueDone resultCode: ' + JSON.stringify(resultCode));
};
try {
  // Call continueMission.
  distributedMissionManager.continueMission(
    {
      srcDeviceId: "",
      dstDeviceId: "",
      missionId: 1,
      wantParam: {"key": "value"}
    },
    { onContinueDone: onContinueDone }).then(() => {
      console.info('continueMission finished successfully');
    }).catch((error: BusinessError) => {
    console.error('continueMission failed, cause: ' + JSON.stringify(error));
  })
} catch (error) {
  console.error('continueMission failed, cause: ' + JSON.stringify(error));
}
```


## continueMission

```TypeScript
function continueMission(parameter: ContinueMissionInfo, callback: AsyncCallback<void>): void
```

通过指定包名（bundleName）的方式进行迁移任务。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function continueMission(parameter: ContinueMissionInfo, callback: AsyncCallback<void>): void--><!--Device-distributedMissionManager-function continueMission(parameter: ContinueMissionInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [ContinueMissionInfo](arkts-ability-continuemissioninfo-i-sys.md) | Yes | 迁移信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，通过指定包名迁移任务完成时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16300504 | The application is not installed on the remote end but installation-free is supported, try again with freeInstall flag. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 16300505 | The operation device must be the device where the application to be continuedis located or the target device to be continued. |
| 16300506 | The local continuation task is already in progress. |
| 16300507 | Failed to get the missionInfo of the specified bundle name. |
| 201 | Permission denied. |
| 202 | The application is not system-app, can not use system-api. |
| 16300501 | The system ability work abnormally. |
| 16300503 | The application is not installed on the remote end and installation-free isnot supported. |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  distributedMissionManager.continueMission(
    {
      srcDeviceId: "",
      dstDeviceId: "",
      bundleName: "ohos.test.continueapp",
      wantParam: {"key": "value"}
    },
    (error: BusinessError) => {
      if (error) {
        console.error('continueMission failed, cause: ' + JSON.stringify(error));
        return;
      }
      console.info('continueMission finished');
  })
} catch (error) {
  console.error('continueMission failed, cause: ' + JSON.stringify(error));
}
```


## continueMission

```TypeScript
function continueMission(parameter: ContinueMissionInfo): Promise<void>
```

通过指定包名（bundleName）的方式进行迁移任务。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function continueMission(parameter: ContinueMissionInfo): Promise<void>--><!--Device-distributedMissionManager-function continueMission(parameter: ContinueMissionInfo): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [ContinueMissionInfo](arkts-ability-continuemissioninfo-i-sys.md) | Yes | 迁移信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16300504 | The application is not installed on the remote end but installation-free is supported, try again with freeInstall flag. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 16300505 | The operation device must be the device where the application to be continuedis located or the target device to be continued. |
| 16300506 | The local continuation task is already in progress. |
| 16300507 | Failed to get the missionInfo of the specified bundle name. |
| 201 | Permission denied. |
| 202 | The application is not system-app, can not use system-api. |
| 16300501 | The system ability work abnormally. |
| 16300503 | The application is not installed on the remote end and installation-free isnot supported. |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    distributedMissionManager.continueMission(
      {
        srcDeviceId: "",
        dstDeviceId: "",
        bundleName: "ohos.test.continueapp",
        wantParam: {"key": "value"}
      }
    ).then(() => {
        console.info('continueMission finished successfully');
    }).catch((error: BusinessError) => {
        console.error('continueMission failed, cause: ' + JSON.stringify(error));
    })
} catch (error) {
    console.error('continueMission failed, cause: ' + JSON.stringify(error));
}
```

