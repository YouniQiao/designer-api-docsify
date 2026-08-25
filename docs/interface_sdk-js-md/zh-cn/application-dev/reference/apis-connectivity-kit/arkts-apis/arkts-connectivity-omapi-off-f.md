# off

## 导入模块

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## off('stateChanged')

```TypeScript
function off(type: 'stateChanged', callback?: Callback<ServiceState>): void
```

取消订阅服务状态更改事件。

**起始版本：** 18

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChanged' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceState](arkts-connectivity-omapi-servicestate-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
