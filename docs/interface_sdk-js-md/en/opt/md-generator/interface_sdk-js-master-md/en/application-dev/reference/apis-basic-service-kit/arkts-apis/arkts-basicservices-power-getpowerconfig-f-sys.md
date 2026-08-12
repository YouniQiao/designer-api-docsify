# getPowerConfig (System API)

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## getPowerConfig

```TypeScript
function getPowerConfig(sceneName: string): string
```

Query the power configuration value for a given scene name.

**Since:** 26.0.0

**Required permissions:** ohos.permission.POWER_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-power-function getPowerConfig(sceneName: string): string--><!--Device-power-function getPowerConfig(sceneName: string): string-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sceneName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-unifiedgroupinfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900400](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900400-incorrect-input-parameter) |
| [4900101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |
| [4900501](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900501-failure-to-read-the-power-supply-configuration-node) |

## Examples

```TypeScript
try {
    let configVal = power.getPowerConfig('scene_name_test');
    console.info('get power config success, configVal: ' + configVal);
} catch(err) {
    console.error('get power config failed, err: ' + err);
}
```
