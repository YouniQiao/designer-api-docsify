# getCellularTxBytes

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getCellularTxBytes

```TypeScript
function getCellularTxBytes(callback: AsyncCallback<number>): void
```

获取当前已处于连接状态的蜂窝网络对应的网卡从最近一次开机开始至接口调用时刻的上行流量总和（单位：字节）。使用callback异步回调。

> **说明：**&gt;
> 本接口建议在蜂窝网络处于连接状态时调用，否则会抛出2103012错误码。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103005](../errorcode-net-statistics.md#2103005-读取系统map失败) |
| [2103011](../errorcode-net-statistics.md#2103011-系统map创建失败) |
| [2103012](../errorcode-net-statistics.md#2103012-获取网卡名失败) |


## getCellularTxBytes

```TypeScript
function getCellularTxBytes(): Promise<number>
```

获取当前已处于连接状态的蜂窝网络对应的网卡从最近一次开机开始至接口调用时刻的上行流量总和（单位：字节）。使用Promise异步回调。

> **说明：**&gt;
> 本接口建议在蜂窝网络处于连接状态时调用，否则会抛出2103012错误码。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103005](../errorcode-net-statistics.md#2103005-读取系统map失败) |
| [2103011](../errorcode-net-statistics.md#2103011-系统map创建失败) |
| [2103012](../errorcode-net-statistics.md#2103012-获取网卡名失败) |
