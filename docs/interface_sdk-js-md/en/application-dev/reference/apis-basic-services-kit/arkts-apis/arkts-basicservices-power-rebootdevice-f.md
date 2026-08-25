# rebootDevice

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## rebootDevice

```TypeScript
function rebootDevice(reason: string): void
```

Restarts the system.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reboot](arkts-basicservices-power-reboot-f-sys.md)

**Required permissions:** ohos.permission.REBOOT

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | string | Yes |
