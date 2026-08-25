# on（系统接口）

## 导入模块

```TypeScript
import { inputDeviceCooperate } from 'kits/@kit.InputKit';
```

## on('cooperation')

```TypeScript
function on(type: 'cooperation', callback: AsyncCallback<{ deviceDescriptor: string, eventMsg: EventMsg }>): void
```

注册监听键鼠穿越状态，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-on-f-sys.md)

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cooperation' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{ deviceDescriptor: string, eventMsg: EventMsg }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
