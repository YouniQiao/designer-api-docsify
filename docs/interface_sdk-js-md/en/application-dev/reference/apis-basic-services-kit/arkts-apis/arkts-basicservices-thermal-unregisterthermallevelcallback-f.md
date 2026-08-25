# unregisterThermalLevelCallback

## Modules to Import

```TypeScript
import { thermal } from 'kits/@kit.BasicServicesKit';
```

## unregisterThermalLevelCallback

```TypeScript
function unregisterThermalLevelCallback(callback?: Callback<void>): void
```

Unregisters from the thermal level changes. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.PowerManager.ThermalManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
