# setPowerConfig (System API)

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## setPowerConfig

```TypeScript
function setPowerConfig(sceneName: string, value: string): void
```

Update the power configuration value for a given scene name.

**Since:** 26.0.0

**Required permissions:** ohos.permission.POWER_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-power-function setPowerConfig(sceneName: string, value: string): void--><!--Device-power-function setPowerConfig(sceneName: string, value: string): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sceneName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-unifiedgroupinfo-i-sys.md) | string | Yes |
| value | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [4900601](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900601-failure-to-write-the-power-supply-configuration-node) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900400](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900400-incorrect-input-parameter) |
| [4900101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

## Examples

```TypeScript
try {
    power.setPowerConfig('scene_name_test', 'value_test');
    console.info('set power config success');
} catch(err) {
    console.error('set power config failed, err: ' + err);
}
```
