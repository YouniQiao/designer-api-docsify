# getValue

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## getValue

```TypeScript
function getValue(admin: Want, item: string): string
```

获取设备设置策略。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function getValue(admin: Want, item: string): string--><!--Device-deviceSettings-function getValue(admin: Want, item: string): string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | Yes | 设备设置策略类型。&lt;br/&gt;- screenOff：设备息屏策略，对于PC/2in1设备，支持查询电池供电下的设备息屏策略。&lt;br/&gt;- powerPolicy：设备电源策略，仅对 PC/2in1设备生效，仅支持查询电池供电下的设备电源策略。&lt;br/&gt;- eyeComfort：从API version 23开始支持，护眼模式开关状态。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 策略类型值。&lt;br/&gt;当item为screenOff时，返回设备息屏时间（单位：毫秒），对于PC/2in1设备，返回设备电池供电下的息屏时间（单位：毫秒）。&lt;br/&gt;当item为 powerPolicy时，返回电源策略，对于PC/2in1设备，返回设备电池供电下的电源策略，格式为JSON字符串:{"powerScene":xx,"powerPolicy":{"powerPolicyAction": xx,"delayTime":xx}}。powerScene为电源策略场景；delayTime为延迟时间（单位：毫秒）；powerPolicyAction为休眠策略。&lt;br/&gt;电源策略场景：&lt;br/&gt;- 0：超时场景。&lt; br/&gt;休眠策略：&lt;br/&gt;- 0：不执行动作。&lt;br/&gt;- 1：自动进入睡眠。&lt;br/&gt;- 2：强制进入睡眠。&lt;br/&gt;- 3：进入休眠，该策略暂不生效。&lt;br/&gt;- 4：关机。&lt;br/&gt;当item为eyeComfort 时，返回的value为护眼模式开关状态的字符串。&lt;br/&gt;- on：全天开启护眼模式。&lt;br/&gt;- off：关闭护眼模式。&lt;br/&gt;- unknown：其他模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

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

