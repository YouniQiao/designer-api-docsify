# getHardwareUnitPowerValue (System API)

## Modules to Import

```TypeScript
import { batteryStats } from '@kit.BasicServicesKit';
```

## getHardwareUnitPowerValue

```TypeScript
function getHardwareUnitPowerValue(type: ConsumptionType): number
```

Obtains the power consumption of a hardware unit according to the consumption type, in unit of mAh.

**Since:** 23

**Deprecated since:** -1

<!--Device-batteryStats-function getHardwareUnitPowerValue(type: ConsumptionType): double--><!--Device-batteryStats-function getHardwareUnitPowerValue(type: ConsumptionType): double-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ConsumptionType](arkts-basicservices-batterystats-consumptiontype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-service-connection-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
    let value = batteryStats.getHardwareUnitPowerValue(batteryStats.ConsumptionType.CONSUMPTION_TYPE_SCREEN);
    console.info('battery statistics value of hardware is: ' + value);
} catch(err) {
    console.error('get battery statistics percent of hardware failed, err: ' + err);
}
```
