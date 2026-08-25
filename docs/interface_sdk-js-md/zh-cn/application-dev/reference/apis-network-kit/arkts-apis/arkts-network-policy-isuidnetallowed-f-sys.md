# isUidNetAllowed（系统接口）

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## isUidNetAllowed

```TypeScript
function isUidNetAllowed(uid: number, isMetered: boolean, callback: AsyncCallback<boolean>): void
```

判断对应 uid 能否访问计量或非计量网络，使用 callback 异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_NET_STRATEGY

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| isMetered | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |


## isUidNetAllowed

```TypeScript
function isUidNetAllowed(uid: number, isMetered: boolean): Promise<boolean>
```

判断对应 uid 能否访问计量或非计量网络，使用 Promise 异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_NET_STRATEGY

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| isMetered | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |


## isUidNetAllowed

```TypeScript
function isUidNetAllowed(uid: number, iface: string, callback: AsyncCallback<boolean>): void
```

获取对应 uid 能否访问指定的 iface 的网络，使用 callback 异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_NET_STRATEGY

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| iface | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |


## isUidNetAllowed

```TypeScript
function isUidNetAllowed(uid: number, iface: string): Promise<boolean>
```

获取对应 uid 能否访问指定的 iface 的网络，使用 Promise 异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_NET_STRATEGY

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| iface | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
