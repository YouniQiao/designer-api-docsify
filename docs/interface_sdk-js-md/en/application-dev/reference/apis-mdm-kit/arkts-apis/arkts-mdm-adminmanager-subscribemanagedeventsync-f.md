# subscribeManagedEventSync

## Modules to Import

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## subscribeManagedEventSync

```TypeScript
function subscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void
```

Subscribes to system management events. After the call is successful, the device administrator application will receive a notification when a subscribed system management event occurs.Since API version 26.0.0, error code 9200002 is returned when a non-super device administrator application calls this API to subscribe to the [MANAGED_EVENT_POLICIES_CHANGED](arkts-mdm-adminmanager-managedevent-e.md) event.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| managedEvents | Array&lt;[ManagedEvent](arkts-mdm-adminmanager-managedevent-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200008](../errorcode-enterpriseDeviceManager.md#9200008-invalid-system-subscription-event) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
