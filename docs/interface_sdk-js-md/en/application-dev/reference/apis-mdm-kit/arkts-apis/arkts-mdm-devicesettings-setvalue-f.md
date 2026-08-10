# setValue

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## setValue

```TypeScript
function setValue(admin: Want, item: string, value: string): void
```

设置设备策略。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setValue(admin: Want, item: string, value: string): void--><!--Device-deviceSettings-function setValue(admin: Want, item: string, value: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | Yes | 设备设置策略类型。&lt;br/&gt;- screenOff：设备息屏策略。对于PC/2in1设备，支持设置电池和电源供电下的设备息屏策略。&lt;br/&gt;- dateTime：设置系统时间。&lt; br/&gt;- powerPolicy：设备电源策略。该能力仅支持PC/2in1设备，策略设置之后不刷新设置—电源和电池页面，在手机平板设备设置后不生效。&lt;br/&gt;对于PC/2in1设备，仅支持设置电池供电下的设备电源策略。设 置设备超时灭屏时睡眠延迟策略，睡眠动作需要在设置—电源和电池页面显示的睡眠时间之后等待设置的delayTime才会生效。&lt;br/&gt;- eyeComfort：从API version 23开始支持，设置护眼模式开关状态，仅支 持全天开启和关闭护眼模式。&lt;br/&gt;- defaultInputMethod：从API version 23开始支持，设置默认输入法。 |
| value | string | Yes | 策略类型值。&lt;br/&gt;当item为screenOff时，value为设备息屏时间（单位：毫秒）。建议value值和设置页面手动操作下拉框中的可选项保持一致。仅在PC/2in1设备 上支持传-1设置永不息屏，其他设备无效。&lt;br/&gt;当item为dateTime时，value为要设置的系统时间（单位：毫秒）。&lt;br/&gt;当item为powerPolicy时，value为JSON字符串，格式：{" powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}。&lt;br/&gt;powerScene为电源策略场景，可设置参数如下：&lt;br/&gt;- 0：超 时灭屏场景。&lt;br/&gt;powerPolicyAction为休眠动作策略场景，可设置参数如下：&lt;br/&gt;- 0：不执行动作。&lt;br/&gt;- 1：自动进入睡眠。&lt;br/&gt;- 2：强制进入睡眠。&lt;br/&gt;- 3：进入休眠，该策略暂 不生效。&lt;br/&gt;- 4：关机。&lt;br/&gt;delayTime为延迟时间（单位：毫秒），不支持设置为30000毫秒，其余数值均在允许范围内。&lt;br/&gt;当item为eyeComfort时，value为护眼模式开关状态的字符串。 &lt;br/&gt;- on：全天开启护眼模式。&lt;br/&gt;- off：关闭护眼模式。&lt;br/&gt;当item为defaultInputMethod时，value为输入法应用包名字符串。&lt;br/&gt;- 可以通过 [getCurrentInputMethod](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-getcurrentinputmethod-f.md/arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod)获取当前输入法应用包名。 |

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
  // Replace with actual values.
  deviceSettings.setValue(wantTemp, 'screenOff', '3000');
  console.info(`Succeeded in setting screen off time.`);
} catch (err) {
  console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
}
```

