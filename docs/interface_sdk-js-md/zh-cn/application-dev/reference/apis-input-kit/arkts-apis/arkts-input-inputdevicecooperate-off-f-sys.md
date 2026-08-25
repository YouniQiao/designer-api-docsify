# off（系统接口）

## 导入模块

```TypeScript
import { inputDeviceCooperate } from 'kits/@kit.InputKit';
```

## off('cooperation')

```TypeScript
function off(type: 'cooperation', callback?: AsyncCallback<void>): void
```

关闭监听键鼠穿越状态，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [off](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-off-f-sys.md)

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cooperation' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
