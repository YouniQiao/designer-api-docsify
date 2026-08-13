# setNTPServer

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## setNTPServer

```TypeScript
function setNTPServer(admin: Want, server: string): void
```

Sets the Network Time Protocol (NTP) time server. After successful configuration, the system will use the specified NTP server for time synchronization to calibrate the system time. This API is suitable for scenarios where enterprise devices require unified time synchronization, ensuring that device time remains consistent with standard time and avoiding business issues caused by inaccurate time, such as inconsistent log timestamps and certificate validation failures.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function setNTPServer(admin: Want, server: string): void--><!--Device-systemManager-function setNTPServer(admin: Want, server: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| server | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

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
