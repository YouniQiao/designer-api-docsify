# subscribeThermalLevel

## subscribeThermalLevel

```TypeScript
function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void
```

Subscribes to the thermal level changes. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [thermal.registerThermalLevelCallback](arkts-basicservices-thermal-registerthermallevelcallback-f.md#registerthermallevelcallback)

<!--Device-thermal-function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void--><!--Device-thermal-function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void-End-->

**System capability:** SystemCapability.PowerManager.ThermalManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ThermalLevel&gt; | Yes | Callback used to return thermal level. This parameter is of the function type. |

**Example**

```TypeScript
thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
    console.info('thermal level is: ' + level);
});
```

