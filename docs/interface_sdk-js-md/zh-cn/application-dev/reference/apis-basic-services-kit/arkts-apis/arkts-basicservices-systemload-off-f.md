# off

## 导入模块

```TypeScript
import { systemLoad } from 'kits/@kit.BasicServicesKit';
```

## off('systemLoadChange')

```TypeScript
function off(type: 'systemLoadChange', callback?: Callback<SystemLoadLevel>): void
```

取消注册系统负载回调，使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.ResourceSchedule.SystemLoad

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemLoadChange' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
