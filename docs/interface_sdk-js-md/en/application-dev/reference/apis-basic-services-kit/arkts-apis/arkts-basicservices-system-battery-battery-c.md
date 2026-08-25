# Battery

The module allows you to query the charging status and remaining power of a device.

**Since:** 3

**Deprecated since:** 6

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

## Modules to Import

```TypeScript
import { Battery, BatteryResponse, GetStatusOptions } from 'kits/@kit.BasicServicesKit';
```

## getStatus

```TypeScript
static getStatus(options?: GetStatusOptions): void
```

Obtains the current charging state and battery level.

**Since:** 3

**Deprecated since:** 6

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GetStatusOptions](arkts-basicservices-system-battery-getstatusoptions-i.md) | No |
