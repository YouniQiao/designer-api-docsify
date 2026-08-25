# Server

服务对象，提供启动服务、停止服务、关闭服务、注册/取消注册服务端回调等方法。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 导入模块

```TypeScript
import { linkEnhance } from 'kits/@kit.DistributedServiceKit';
```

## close

```TypeScript
close(): void
```

当业务执行完毕，服务端清理资源时，调用close()方法，销毁Server对象，释放相关资源。之后如果再次与对端设备交互，需要重新创建Server对象。close()会销毁Server对象并释放资源，之后需重新创建Server 对象；stop()仅停止服务，Server对象仍可重新启动。如果还需重新启动服务，使用stop()；如果业务完全结束，使用close()。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## off('connectionAccepted')

```TypeScript
off(type: 'connectionAccepted', callback?: Callback<Connection>): void
```

取消注册connectionAccepted事件的回调监听。需要在创建服务成功后调用。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connectionAccepted' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Connection](arkts-distributedservice-linkenhance-connection-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [32390206](../errorcode-link-enhance.md#32390206-参数非法) |

## off('serverStopped')

```TypeScript
off(type: 'serverStopped', callback?: Callback<number>): void
```

取消注册serverStopped事件的回调监听。需要在创建服务成功后调用。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'serverStopped' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [32390206](../errorcode-link-enhance.md#32390206-参数非法) |

## on('connectionAccepted')

```TypeScript
on(type: 'connectionAccepted', callback: Callback<Connection>): void
```

创建服务成功后，注册connectionAccepted事件的回调监听，等待对端连接。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'connectionAccepted' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Connection](arkts-distributedservice-linkenhance-connection-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [32390206](../errorcode-link-enhance.md#32390206-参数非法) |

## on('serverStopped')

```TypeScript
on(type: 'serverStopped', callback: Callback<number>): void
```

在创建服务成功后，注册serverStopped回调，监听服务异常停止。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'serverStopped' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [32390206](../errorcode-link-enhance.md#32390206-参数非法) |

## start

```TypeScript
start(): void
```

创建服务成功后，需要调用start()开启该服务，方可被客户端连接，最大服务个数为10。服务开启后，可通过stop()停止服务，可以重新通过start()再次开启服务。服务使用完毕后，需调用close()销毁Server对象释 放资源。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [32390202](../errorcode-link-enhance.md#32390202-服务个数超出限制) |
| [32390300](../errorcode-link-enhance.md#32390300-内部错误) |

## stop

```TypeScript
stop(): void
```

使用完服务时，调用`stop`停止服务，停止后可以调用`start`重新开启服务。

**起始版本：** 20

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
