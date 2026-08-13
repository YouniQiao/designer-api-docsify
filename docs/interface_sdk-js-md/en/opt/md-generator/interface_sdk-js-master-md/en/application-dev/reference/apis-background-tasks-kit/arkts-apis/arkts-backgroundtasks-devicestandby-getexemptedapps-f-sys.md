# getExemptedApps (System API)

## Modules to Import

```TypeScript
import { deviceStandby } from '@kit.BackgroundTasksKit';
```

## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: number, callback: AsyncCallback<Array<ExemptedAppInfo>>): void
```

Returns the information about the specified exempted application.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DEVICE_STANDBY_EXEMPTION

<!--Device-deviceStandby-function getExemptedApps(resourceTypes: int, callback: AsyncCallback<Array<ExemptedAppInfo>>): void--><!--Device-deviceStandby-function getExemptedApps(resourceTypes: int, callback: AsyncCallback<Array<ExemptedAppInfo>>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceTypes | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ExemptedAppInfo](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800003](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [18700001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#18700001-caller-information-verification-failure-for-an-energy-resource-request) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { deviceStandby } from '@kit.BackgroundTasksKit';

let resourceTypes: deviceStandby.ResourceType  = deviceStandby.ResourceType.TIMER | deviceStandby.ResourceType.NETWORK;
deviceStandby.getExemptedApps(resourceTypes, (err: BusinessError, res: Array<deviceStandby.ExemptedAppInfo>) => {
  if (err) {
    console.error('DEVICE_STANDBY getExemptedApps callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('DEVICE_STANDBY getExemptedApps callback success.');
    for (let i = 0; i < res.length; i++) {
      console.info('DEVICE_STANDBY getExemptedApps callback result ' + JSON.stringify(res[i]));
    }
  }
});
```


## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: number): Promise<Array<ExemptedAppInfo>>
```

Returns the information about the specified exempted application.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.DEVICE_STANDBY_EXEMPTION

<!--Device-deviceStandby-function getExemptedApps(resourceTypes: int): Promise<Array<ExemptedAppInfo>>--><!--Device-deviceStandby-function getExemptedApps(resourceTypes: int): Promise<Array<ExemptedAppInfo>>-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceTypes | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ExemptedAppInfo](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-system-service-failure) |
| [9800001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-memory-operation-failure) |
| [9800003](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc-failure) |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel-operation-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [18700001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#18700001-caller-information-verification-failure-for-an-energy-resource-request) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { deviceStandby } from '@kit.BackgroundTasksKit';

let resourceTypes: deviceStandby.ResourceType = deviceStandby.ResourceType.TIMER | deviceStandby.ResourceType.NETWORK;
deviceStandby.getExemptedApps(resourceTypes).then( (res: Array<deviceStandby.ExemptedAppInfo>) => {
  console.info('DEVICE_STANDBY getExemptedApps promise success.');
  for (let i = 0; i < res.length; i++) {
    console.info('DEVICE_STANDBY getExemptedApps promise result ' + JSON.stringify(res[i]));
  }
}).catch( (err: BusinessError) => {
  console.error('DEVICE_STANDBY getExemptedApps promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```
