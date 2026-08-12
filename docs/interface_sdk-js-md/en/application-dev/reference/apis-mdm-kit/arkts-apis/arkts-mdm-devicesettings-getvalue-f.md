# getValue

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## getValue

```TypeScript
function getValue(admin: Want, item: string): string
```

Obtains a device setting policy.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function getValue(admin: Want, item: string): string--><!--Device-deviceSettings-function getValue(admin: Want, item: string): string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| item | string | Yes | Type of the policy to set. &lt;br&gt;- **screenOff**: device screen-off policy. For PCs/2-in-1 devices, the screen-off policy for battery supply can be queried. &lt;br&gt;- **powerPolicy**: device power policy, which takes effect only for PCs/2-in-1 devices. Only the power policy for battery supply can be queried. &lt;br&gt;- **eyeComfort**: eye comfort mode. This parameter is supported since API version 23. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Policy type value. &lt;br&gt;If **item** is **screenOff**, the device screen-off time (in ms) is returned. For PCs/2-in-1 devices, the device screen-off time (in ms) in battery mode is returned. &lt;br&gt;If **item** is **powerPolicy**, the power policy is returned. For PCs/2-in-1 devices, the power policy in battery mode is returned. The power policy a JSON string in {"powerScene":xx,"powerPolicy":{"powerPolicyAction" :xx,"delayTime":xx}} format. **powerScene** indicates the power policy scenario, **delayTime** indicates the delay time (in milliseconds), and **powerPolicyAction** indicates the sleep policy. &lt;br&gt;The value of **powerScene** can be: &lt;br&gt;- **0**: timeout. &lt;br&gt;The value of **powerPolicyAction** can be: &lt;br&gt;- **0**: No action is performed. &lt;br&gt;- **1**: enter sleep mode automatically. &lt;br&gt;- **2**: forcibly enter sleep mode. &lt;br&gt;- **3**: enter sleep mode. This policy does not take effect currently. &lt;br&gt;- **4**: power off. &lt;br&gt;If **item** is **eyeComfort**, **value** is a string indicating the status of the eye comfort mode. &lt;br&gt;- **on**: The eye comfort mode is enabled all day. &lt;br&gt;- **off**: The eye comfort mode is disabled. &lt;br&gt;- **unknown**: other modes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  let result: string = deviceSettings.getValue(wantTemp, 'screenOff');
  console.info(`Succeeded in getting screen off time, result : ${result}`);
} catch (err) {
  console.error(`Failed to get screen off time. Code: ${err.code}, message: ${err.message}`);
}
```

