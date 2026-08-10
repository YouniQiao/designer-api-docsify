# rebootDevice

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## rebootDevice

```TypeScript
function rebootDevice(reason: string): void
```

重启系统。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [power.reboot](arkts-basicservices-power-reboot-f-sys.md#reboot)

**Required permissions:** ohos.permission.REBOOT

<!--Device-power-function rebootDevice(reason: string): void--><!--Device-power-function rebootDevice(reason: string): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reason | string | Yes | 重启原因。例如，“updater”表示重启后进入更新模式。如果未指定该参数，系统将在重启后进入正常模式。 |

## Examples

```TypeScript
power.rebootDevice('reboot_test');
```

