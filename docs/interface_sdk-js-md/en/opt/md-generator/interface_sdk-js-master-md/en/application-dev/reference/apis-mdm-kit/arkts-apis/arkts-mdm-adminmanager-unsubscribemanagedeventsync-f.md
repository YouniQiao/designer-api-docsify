# unsubscribeManagedEventSync

## Modules to Import

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## unsubscribeManagedEventSync

```TypeScript
function unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void
```

Unsubscribes from system management events. After the API is successfully called, no notifications for the unsubscribed system management events will be received.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void--><!--Device-adminManager-function unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| managedEvents | Array&lt;ManagedEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9200008](../errorcode-enterpriseDeviceManager.md#9200008-invalid-system-subscription-event) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let events: Array<adminManager.ManagedEvent> = [adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_ADDED, adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_REMOVED];

try {
  adminManager.unsubscribeManagedEventSync(wantTemp, events);
  console.info('Succeeded in unsubscribing managed event.');
} catch (err) {
  console.error(`Failed to unsubscribe managed event. Code: ${err.code}, message: ${err.message}`);
}
```
