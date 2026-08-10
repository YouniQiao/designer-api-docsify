# off

## Modules to Import

```TypeScript
import { systemLoad } from 'kits/@kit.BasicServicesKit';
```

## off('systemLoadChange')

```TypeScript
function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void
```

取消注册系统负载回调，使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-systemLoad-function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'systemLoadChange' | Yes | 固定取值'systemLoadChange'，系统负载变化类型。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SystemLoadLevel&gt; | No | 回调函数，返回本次取消注册系统负载时的系统负载融合档位。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; &lt;br&gt; 2. Unregister type has not register; 3. Parameter verification failed. |

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

