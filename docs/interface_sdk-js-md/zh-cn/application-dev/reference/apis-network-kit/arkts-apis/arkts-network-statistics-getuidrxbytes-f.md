# getUidRxBytes

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void
```

获取指定应用从最近一次开机开始至接口调用时刻的下行流量总和（单位：字节）。使用callback异步回调。

> **说明：**&gt;
> 若重启后该应用未产生流量消耗，则会抛出2103005错误码。

**起始版本：** 10

**需要权限：** 
- API版本26.0.0+：ohos.permission.GET_NETWORK_STATS

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103005](../errorcode-net-statistics.md#2103005-读取系统map失败) |
| [2103011](../errorcode-net-statistics.md#2103011-系统map创建失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: number): Promise<number>
```

获取指定应用从最近一次开机开始至接口调用时刻的下行流量总和（单位：字节）。使用Promise异步回调。

> **说明：**&gt;
> 若重启后该应用未产生流量消耗，则会抛出2103005错误码。

**起始版本：** 10

**需要权限：** 
- API版本26.0.0+：ohos.permission.GET_NETWORK_STATS

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103005](../errorcode-net-statistics.md#2103005-读取系统map失败) |
| [2103011](../errorcode-net-statistics.md#2103011-系统map创建失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
