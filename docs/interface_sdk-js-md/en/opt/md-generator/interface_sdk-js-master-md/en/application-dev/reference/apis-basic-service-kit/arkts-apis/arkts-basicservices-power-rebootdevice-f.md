# rebootDevice

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## rebootDevice

```TypeScript
function rebootDevice(reason: string): void
```

Restarts the system.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reboot](arkts-basicservices-power-reboot-f-sys.md#reboot)

**Required permissions:** ohos.permission.REBOOT

<!--Device-power-function rebootDevice(reason: string): void--><!--Device-power-function rebootDevice(reason: string): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | string | Yes |

## Examples

```TypeScript
power.rebootDevice('reboot_test');
```
