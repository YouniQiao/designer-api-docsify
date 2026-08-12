# finishLogCollected

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## finishLogCollected

```TypeScript
function finishLogCollected(admin: Want): void
```

Deletes the device logs collected by the current MDM app under the current user.

> **NOTE：**
> 
> After the app calls [startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md#startCollectLog) to initiate log collection and
> receives the
> [EnterpriseAdminExtensionAbility.onLogCollected](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onLogCollected)
> callback, you are advised to immediately copy or process the logs, and then call this API to delete the collected
> logs.
> 
> If this API is not called, device logs will occupy the system storage space, which does not affect the next call
> of [startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md#startCollectLog) to start a log collection task.

**Since:** 23

**Required permissions:** ohos.permission.ENTERPRISE_READ_LOG

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function finishLogCollected(admin: Want): void--><!--Device-systemManager-function finishLogCollected(admin: Want): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  systemManager.finishLogCollected(wantTemp);
  console.info('Succeeded in finishing log collected.');
} catch (err) {
  console.error(`Failed to finish log collected. Code is ${err.code}, message is ${err.message}`);
}
```
