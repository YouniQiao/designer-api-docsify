# continueMission (System API)

## Modules to Import

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
```

## continueMission

```TypeScript
function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback, callback: AsyncCallback<void>): void
```

Continues a mission on a remote device, with the mission ID specified. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [ContinueDeviceInfo](arkts-ability-distributedmissionmanager-continuedeviceinfo-t-sys.md) | Yes |
| options | [ContinueCallback](arkts-ability-distributedmissionmanager-continuecallback-t-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) |
| [16300502](../errorcode-DistributedSchedule.md#16300502-failed-to-get-the-missioninfo-of-the-specified-missionid) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-not-supported) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-supported-try-again-with-the-freeinstall-flag) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-the-operation-device-must-be-the-device-where-the-application-to-be-continued-is-currently-located-or-the-target-device) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-the-local-continuation-task-is-already-in-progress) |

**Examples**

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


## continueMission

```TypeScript
function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback): Promise<void>
```

Continues a mission on a remote device, with the mission ID specified. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [ContinueDeviceInfo](arkts-ability-distributedmissionmanager-continuedeviceinfo-t-sys.md) | Yes |
| options | [ContinueCallback](arkts-ability-distributedmissionmanager-continuecallback-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) |
| [16300502](../errorcode-DistributedSchedule.md#16300502-failed-to-get-the-missioninfo-of-the-specified-missionid) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-not-supported) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-supported-try-again-with-the-freeinstall-flag) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-the-operation-device-must-be-the-device-where-the-application-to-be-continued-is-currently-located-or-the-target-device) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-the-local-continuation-task-is-already-in-progress) |

**Examples**

See [continueMission](#continuemission)


## continueMission

```TypeScript
function continueMission(parameter: ContinueMissionInfo, callback: AsyncCallback<void>): void
```

Continues a mission on a remote device, with the bundle name specified. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [ContinueMissionInfo](arkts-ability-continuemissioninfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-not-supported) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-supported-try-again-with-the-freeinstall-flag) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-the-operation-device-must-be-the-device-where-the-application-to-be-continued-is-currently-located-or-the-target-device) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-the-local-continuation-task-is-already-in-progress) |
| [16300507](../errorcode-DistributedSchedule.md#16300507-failed-to-get-the-missioninfo-of-the-specified-bundlename) |

**Examples**

See [continueMission](#continuemission)


## continueMission

```TypeScript
function continueMission(parameter: ContinueMissionInfo): Promise<void>
```

Continues a mission on a remote device, with the bundle name specified. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [ContinueMissionInfo](arkts-ability-continuemissioninfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-not-supported) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-the-application-is-not-installed-on-the-remote-end-and-installation-free-is-supported-try-again-with-the-freeinstall-flag) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-the-operation-device-must-be-the-device-where-the-application-to-be-continued-is-currently-located-or-the-target-device) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-the-local-continuation-task-is-already-in-progress) |
| [16300507](../errorcode-DistributedSchedule.md#16300507-failed-to-get-the-missioninfo-of-the-specified-bundlename) |

**Examples**

See [continueMission](#continuemission)
