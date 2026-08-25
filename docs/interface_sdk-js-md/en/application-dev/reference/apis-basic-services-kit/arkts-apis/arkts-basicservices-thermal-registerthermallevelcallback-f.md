# registerThermalLevelCallback

## Modules to Import

```TypeScript
import { thermal } from 'kits/@kit.BasicServicesKit';
```

## registerThermalLevelCallback

```TypeScript
function registerThermalLevelCallback(callback: Callback<ThermalLevel>): void
```

Registers a callback to be invoked when the thermal level changes. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.PowerManager.ThermalManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
