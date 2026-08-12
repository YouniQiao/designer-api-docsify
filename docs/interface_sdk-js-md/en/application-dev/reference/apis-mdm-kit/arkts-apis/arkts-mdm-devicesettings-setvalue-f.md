# setValue

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## setValue

```TypeScript
function setValue(admin: Want, item: string, value: string): void
```

Sets the device policy.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setValue(admin: Want, item: string, value: string): void--><!--Device-deviceSettings-function setValue(admin: Want, item: string, value: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| item | string | Yes | Type of the policy to set. &lt;br&gt;- **screenOff**: device screen-off policy. For PCs/2-in-1 devices, the device power policy can be set for both battery and power modes. &lt;br&gt;- **dateTime**: system time settings. &lt;br&gt;- **powerPolicy**: device power policy. This capability is supported only on PCs/2-in-1 devices. After the policy is set, the **Settings** > **Power & battery** screen is not refreshed. The settings do not take effect on phones or tablets. &lt;br&gt;For PCs/2-in-1 devices, the device power policy can be set only for battery supply. When the sleep delay policy upon device screen-off due to timeout is set, the sleep action takes effect after the sleep time shown in the **Settings** > **Power & battery** screen, followed by an additional **delayTime**. &lt;br&gt;- **eyeComfort**: eye comfort mode. This parameter is supported since API version 23. This mode can only be enabled all day or disabled. &lt;br&gt;- **defaultInputMethod**: default input method. This parameter is supported since API version 23. |
| value | string | Yes | Policy type value. &lt;br&gt;If **item** is **screenOff**, **value** is the screen-off time, in ms. It is recommended that **value** be consistent with the options in the drop-down list box on the settings page. Passing **-1** to set the screen to never turn off is supported only on PCs/2‑in‑1 devices. This value does not take effect on other device types. &lt;br&gt;If **item** is **dateTime**, **value** is the system time to set, in ms. &lt;br&gt;If **item** is **powerPolicy**, **value** is a JSON string in {"powerScene":xx,"powerPolicy":{" powerPolicyAction":xx,"delayTime":xx}} format. &lt;br&gt;**powerScene** indicates the power policy scenario. The following values are supported: &lt;br&gt;- **0**: screen-off due to timeout. &lt;br&gt;**powerPolicyAction** indicates the sleep action policy scenario. The following values are supported: &lt;br&gt;- **0**: No action is performed. &lt;br&gt;- **1**: enter sleep mode automatically. &lt;br&gt;- **2**: forcibly enter sleep mode. &lt;br&gt;- **3**: enter sleep mode. This policy does not take effect currently. &lt;br&gt;- **4**: power off. &lt;br&gt;**delayTime** indicates the delay time (unit: ms). The value cannot be **30000**. Other values are allowed. &lt;br&gt;If **item** is **eyeComfort**, **value** is a string indicating the status of the eye comfort mode. &lt;br&gt;- **on**: The eye comfort mode is enabled all day. &lt;br&gt;- **off**: The eye comfort mode is disabled. &lt;br&gt;If **item** is **defaultInputMethod**, **value** is a string indicating the name of the input method application bundle. &lt;br&gt;- You can use [getCurrentInputMethod](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-getcurrentinputmethod-f.md#getCurrentInputMethod) to obtain the current input method application bundle name. |

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
  // Replace with actual values.
  deviceSettings.setValue(wantTemp, 'screenOff', '3000');
  console.info(`Succeeded in setting screen off time.`);
} catch (err) {
  console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
}
```

