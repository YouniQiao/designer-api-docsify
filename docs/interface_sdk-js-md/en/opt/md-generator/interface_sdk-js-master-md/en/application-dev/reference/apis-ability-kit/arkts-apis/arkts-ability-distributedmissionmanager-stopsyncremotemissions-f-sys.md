# stopSyncRemoteMissions (System API)

## Modules to Import

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
```

## stopSyncRemoteMissions

```TypeScript
function stopSyncRemoteMissions(parameter: MissionDeviceInfo, callback: AsyncCallback<void>): void
```

Stops synchronizing the remote mission list. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo, callback: AsyncCallback<void>): void--><!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  distributedMissionManager.stopSyncRemoteMissions(
    {
      deviceId: ""
    },
    (error: BusinessError) => {
      if (error) {
        console.error('stopSyncRemoteMissions failed, cause: ' + JSON.stringify(error));
        return;
      }
      console.info('stopSyncRemoteMissions finished');}
  )
} catch (error) {
  console.error('stopSyncRemoteMissions failed, cause: ' + JSON.stringify(error));
}
```


## stopSyncRemoteMissions

```TypeScript
function stopSyncRemoteMissions(parameter: MissionDeviceInfo): Promise<void>
```

Stops synchronizing the remote mission list. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo): Promise<void>--><!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  distributedMissionManager.stopSyncRemoteMissions(
    {
      deviceId: ""
    }).then(() => {
      console.info('stopSyncRemoteMissions finished successfully');
    }).catch((error: BusinessError) => {
    console.error('stopSyncRemoteMissions failed, cause: ' + JSON.stringify(error));
  })
} catch (error) {
  console.error('stopSyncRemoteMissions failed, cause: ' + JSON.stringify(error));
}
```
