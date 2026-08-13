# getLocationPolicy

## Modules to Import

```TypeScript
import { locationManager } from '@kit.MDMKit';
```

## getLocationPolicy

```TypeScript
function getLocationPolicy(admin: Want): LocationPolicy
```

Queries the location service policy.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_LOCATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-locationManager-function getLocationPolicy(admin: Want): LocationPolicy--><!--Device-locationManager-function getLocationPolicy(admin: Want): LocationPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LocationPolicy](arkts-mdm-locationmanager-locationpolicy-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |


## getLocationPolicy

```TypeScript
function getLocationPolicy(admin: Want | null): LocationPolicy
```

Queries the location service policy. This API can be used in enterprise device administrator applications to check the current location service policy state of the device, for policy compliance verification or state confirmation before policy adjustment. It is suitable for scenarios such as confirming the current policy configuration, reading the policy state when the device administrator application starts, and checking the policy when troubleshooting location service issues.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_LOCATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-locationManager-function getLocationPolicy(admin: Want | null): LocationPolicy--><!--Device-locationManager-function getLocationPolicy(admin: Want | null): LocationPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LocationPolicy](arkts-mdm-locationmanager-locationpolicy-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { locationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: locationManager.LocationPolicy = locationManager.getLocationPolicy(wantTemp);
  console.info(`Succeeded in getting location policy. policy: ${result}`);
} catch(err) {
  console.error(`Failed to get location policy. Code: ${err.code}, message: ${err.message}`);
}
```
