# createAVSession

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## createAVSession

```TypeScript
function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void
```

创建会话对象，一个应用程序仅允许存在一个会话，重复创建会失败，结果通过callback异步回调方式返回。

> **说明：**&gt;
> - 在业务执行阶段需要保持avsession对象存活，避免后台管控静音、设备选择异常、通知/锁屏/胶囊播控卡片显示异常等情况。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| tag | string | 是 |
| type | [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVSession](arkts-avsession-avsession-avsession-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |


## createAVSession

```TypeScript
function createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>
```

创建会话对象，一个应用进程仅允许存在一个会话，重复创建会失败，结果通过Promise异步回调方式返回。

> **说明：**&gt;
> - 在业务执行阶段需要保持avsession对象存活，避免后台管控静音、设备选择异常、通知/锁屏/胶囊播控卡片显示异常等情况。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| tag | string | 是 |
| type | [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVSession](arkts-avsession-avsession-avsession-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
