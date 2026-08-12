# subscribeThermalLevel

## Modules to Import

```TypeScript
import { thermal } from '@kit.BasicServicesKit';
```

## subscribeThermalLevel

```TypeScript
function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void
```

Subscribes to the thermal level changes. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [registerThermalLevelCallback](arkts-basicservices-thermal-registerthermallevelcallback-f.md#registerThermalLevelCallback)

<!--Device-thermal-function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void--><!--Device-thermal-function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void-End-->

**System capability:** SystemCapability.PowerManager.ThermalManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md)&gt; | Yes |

## Examples

```TypeScript
thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
    console.info('thermal level is: ' + level);
});
```
