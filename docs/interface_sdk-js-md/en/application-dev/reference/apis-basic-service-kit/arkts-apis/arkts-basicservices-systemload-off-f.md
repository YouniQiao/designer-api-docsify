# off

## Modules to Import

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';
```

## off('systemLoadChange')

```TypeScript
function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void
```

Disables listening for system load level changes. This API uses an asynchronous callback to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-systemLoad-function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'systemLoadChange' | Yes | Change type. This parameter has a fixed value of **systemLoadChange**. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md)&gt; | No | Callback used to return the system load level. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1. Callback parameter error; &lt;br&gt; 2. Unregister type has not register; 3. Parameter verification failed. |

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

