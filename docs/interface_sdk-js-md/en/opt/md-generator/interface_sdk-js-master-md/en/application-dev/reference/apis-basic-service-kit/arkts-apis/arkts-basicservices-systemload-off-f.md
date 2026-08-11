# off

## Modules to Import

```TypeScript
import { systemLoad } from 'kits/@kit.BasicServicesKit';
```

## off('systemLoadChange')

```TypeScript
function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void
```

Disables listening for system load level changes. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-systemLoad-function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemLoadChange' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SystemLoadLevel&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';

function onSystemLoadChange(res: systemLoad.SystemLoadLevel) {
    console.info(`system load changed, current level ` + res);
}

try {
    systemLoad.off('systemLoadChange', onSystemLoadChange);
    console.info(`unregister systemload callback succeeded:. `);
} catch (err) {
    console.error(`unregister systemload callback failed: ` + JSON.stringify(err));
}
```
