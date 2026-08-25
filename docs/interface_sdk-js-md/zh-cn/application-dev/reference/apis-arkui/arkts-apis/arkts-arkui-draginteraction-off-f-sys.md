# off（系统接口）

## 导入模块

```TypeScript
import { dragInteraction } from 'kits/@kit.ArkUI';
```

## off('drag')

```TypeScript
function off(type: 'drag', callback?: Callback<DragState>): void
```

取消监听拖拽状态。

**起始版本：** 10

**系统能力：** SystemCapability.Msdp.DeviceStatus.Drag

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'drag' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DragState](arkts-arkui-draginteraction-dragstate-e-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
