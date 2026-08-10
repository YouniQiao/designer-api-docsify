# getDeviceInfo

## Modules to Import

```TypeScript
import { deviceInfo } from 'kits/@kit.MDMKit';
```

## getDeviceInfo

```TypeScript
function getDeviceInfo(admin: Want, label: string): string
```

获取设备信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_GET_DEVICE_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceInfo-function getDeviceInfo(admin: Want, label: string): string--><!--Device-deviceInfo-function getDeviceInfo(admin: Want, label: string): string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件，用于指定具有设备管理能力的目标应用。Want对象中必须包含abilityName（扩展能力名称）和bundleName（应用包名）两个必填字段。 |
| label | string | Yes | 支持获取的设备信息标签。&lt;br/&gt;- deviceName：设备名称。&lt;br/&gt;- deviceSerial：设备序列号。&lt;br/&gt;- simInfo：SIM卡信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | Device information obtained. &lt;br&gt;If **label** is **simInfo**, the return value is the SIM card information in a JSON string. For example, [{"slotId": 0, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": "", "NUMBER": ""}, {"slotId": 1, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": "", "NUMBER": ""}], where **slotId:0** indicates card slot 1, and **slotId:1** indicates card slot 2. **NUMBER** indicates the phone number and is supported since API version 23. The value is in the E.164 international standard format ( for example, +8612345678901) that contains the country code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200007 | The system ability works abnormally. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { deviceInfo } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace with actual values.
  let result: string = deviceInfo.getDeviceInfo(wantTemp, 'deviceName');
  console.info(`Succeeded in getting device name, result : ${result}`);
} catch (err) {
  console.error(`Failed to get device name. Code: ${err.code}, message: ${err.message}`);
}
```

