# on

## on('systemLoadChange')

```TypeScript
function on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void
```

注册系统负载回调，感知系统负载融合档位变化，使用callback异步回调。

**起始版本：** 12

<!--Device-systemLoad-function on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function on(type: 'systemLoadChange', callback: Callback<SystemLoadLevel>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.SystemLoad

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemLoadChange' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SystemLoadLevel&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

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
