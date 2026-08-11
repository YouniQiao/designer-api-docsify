# on

## Modules to Import

```TypeScript
import { systemLoad } from 'kits/@kit.BasicServicesKit';
```

## on('systemLoadChange')

```TypeScript
function on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void
```

Enables listening for system load level changes. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-systemLoad-function on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemLoadChange' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SystemLoadLevel&gt; | Yes |

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
    systemLoad.on('systemLoadChange', onSystemLoadChange);
    console.info(`register systemload callback succeeded. `);
} catch (err) {
    console.error(`register systemload callback failed: ` + JSON.stringify(err));
}
```
