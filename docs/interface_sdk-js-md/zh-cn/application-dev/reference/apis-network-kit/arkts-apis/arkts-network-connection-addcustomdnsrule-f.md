# addCustomDnsRule

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## addCustomDnsRule

```TypeScript
function addCustomDnsRule(host: string, ip: Array<string>, callback: AsyncCallback<void>): void
```

为当前应用程序添加自定义host和对应的IP地址的映射。使用callback异步回调。

> **说明：**&gt;
> 不需要时可调用[removeCustomDnsRule](arkts-network-connection-removecustomdnsrule-f.md)删除某一条自定义规则或调用
> [clearCustomDnsRules](arkts-network-connection-clearcustomdnsrules-f.md)删除当前应用程序的所有的自定义DNS规则 。

**起始版本：** 11

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |
| ip | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |


## addCustomDnsRule

```TypeScript
function addCustomDnsRule(host: string, ip: Array<string>): Promise<void>
```

为当前应用程序添加自定义host和对应的IP地址的映射。使用Promise异步回调。

> **说明：**&gt;
> 不需要时可调用[removeCustomDnsRule](arkts-network-connection-removecustomdnsrule-f.md)删除某一条自定义规则或调用
> [clearCustomDnsRules](arkts-network-connection-clearcustomdnsrules-f.md)删除当前应用程序的所有的自定义DNS规则 。

**起始版本：** 11

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |
| ip | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
