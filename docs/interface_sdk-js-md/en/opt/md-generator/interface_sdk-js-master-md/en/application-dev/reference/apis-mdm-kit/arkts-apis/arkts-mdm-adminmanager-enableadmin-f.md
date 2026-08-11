# enableAdmin

## Modules to Import

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## enableAdmin

```TypeScript
function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, callback: AsyncCallback<void>): void
```

Enables a device administrator application. The super device administrator application can be enabled only for the first user (u100). After the application is enabled, it cannot be uninstalled. Its  
[EnterpriseAdminExtensionAbility](../../../mdm/mdm-kit-term.md#enterpriseadminextensionability) component will automatically start upon device startup and user switching. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, callback: AsyncCallback<void>): void--><!--Device-adminManager-function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| enterpriseInfo | [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) | Yes |
| type | [AdminType](arkts-mdm-adminmanager-admintype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9200004](../errorcode-enterpriseDeviceManager.md#9200004-failed-to-enable-the-device-administrator-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200007](../errorcode-enterpriseDeviceManager.md#9200007-system-ability-error) |
| [9200003](../errorcode-enterpriseDeviceManager.md#9200003-invalid-administrator-ability-component) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let enterpriseInfo: adminManager.EnterpriseInfo = {
  // Replace with actual values.
  name: 'enterprise name',
  description: 'enterprise description'
};

adminManager.enableAdmin(wantTemp, enterpriseInfo, adminManager.AdminType.ADMIN_TYPE_SUPER, (err) => {
  if (err) {
    console.error(`Failed to enable admin. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in enabling admin');
});
```


## enableAdmin

```TypeScript
function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, userId: number, callback: AsyncCallback<void>): void
```

Enables a device administrator application for a user (specified by **userId**). The super device administrator application can be enabled only for the first user (u100). This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, userId: number, callback: AsyncCallback<void>): void--><!--Device-adminManager-function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, userId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| enterpriseInfo | [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) | Yes |
| type | [AdminType](arkts-mdm-adminmanager-admintype-e.md) | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9200004](../errorcode-enterpriseDeviceManager.md#9200004-failed-to-enable-the-device-administrator-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200007](../errorcode-enterpriseDeviceManager.md#9200007-system-ability-error) |
| [9200003](../errorcode-enterpriseDeviceManager.md#9200003-invalid-administrator-ability-component) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let enterpriseInfo: adminManager.EnterpriseInfo = {
  // Replace with actual values.
  name: 'enterprise name',
  description: 'enterprise description'
};

adminManager.enableAdmin(wantTemp, enterpriseInfo, adminManager.AdminType.ADMIN_TYPE_NORMAL, 100, (err) => {
  if (err) {
    console.error(`Failed to enable admin. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in enabling admin');
});
```


## enableAdmin

```TypeScript
function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, userId?: number): Promise<void>
```

Enables the device administrator application for the current or specified user. The super device administrator application can be enabled only for the first user (u100). This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, userId?: number): Promise<void>--><!--Device-adminManager-function enableAdmin(admin: Want, enterpriseInfo: EnterpriseInfo, type: AdminType, userId?: number): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| enterpriseInfo | [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) | Yes |
| type | [AdminType](arkts-mdm-adminmanager-admintype-e.md) | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9200004](../errorcode-enterpriseDeviceManager.md#9200004-failed-to-enable-the-device-administrator-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200007](../errorcode-enterpriseDeviceManager.md#9200007-system-ability-error) |
| [9200003](../errorcode-enterpriseDeviceManager.md#9200003-invalid-administrator-ability-component) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let enterpriseInfo: adminManager.EnterpriseInfo = {
  // Replace with actual values.
  name: 'enterprise name',
  description: 'enterprise description'
};

adminManager.enableAdmin(wantTemp, enterpriseInfo, adminManager.AdminType.ADMIN_TYPE_NORMAL, 100).catch(
  (err: BusinessError) => {
    console.error(`Failed to enable admin. Code: ${err.code}, message: ${err.message}`);
  });
```
