# setNTPServer

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setNTPServer

```TypeScript
function setNTPServer(admin: Want, server: string): void
```

Sets the Network Time Protocol (NTP) time server. After successful configuration, the system will use the specified NTP server for time synchronization to calibrate the system time. This API is suitable for scenarios where enterprise devices require unified time synchronization, ensuring that device time remains consistent with standard time and avoiding business issues caused by inaccurate time, such as inconsistent log timestamps and certificate validation failures.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function setNTPServer(admin: Want, server: string): void--><!--Device-systemManager-function setNTPServer(admin: Want, server: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| server | string | Yes | NTP server addresses separated by commas (,). For example, **ntpserver1.com,ntpserver2.com**. The value can contain a maximum of 96 bytes, including the null terminator ( **\0**). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let server: string = "ntpserver.com";
try {
  systemManager.setNTPServer(wantTemp, server);
  console.info('Succeeded in setting NTPserver.');
} catch (err) {
  console.error(`Failed to set ntp server. Code is ${err.code}, message is ${err.message}`);
}
```

