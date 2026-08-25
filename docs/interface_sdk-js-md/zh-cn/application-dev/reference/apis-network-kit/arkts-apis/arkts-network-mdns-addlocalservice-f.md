# addLocalService

## 导入模块

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## addLocalService

```TypeScript
function addLocalService(context: Context, serviceInfo: LocalServiceInfo,
                           callback: AsyncCallback<LocalServiceInfo>): void
```

添加一个MDNS服务，使用callback方式作为异步方法。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [serviceInfo](arkts-network-mdns-discoveryeventinfo-i.md) | [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2204003](../errorcode-net-mdns.md#2204003-重复注册) |
| [2204008](../errorcode-net-mdns.md#2204008-删除服务失败) |
| [2204010](../errorcode-net-mdns.md#2204010-发送消息失败) |


## addLocalService

```TypeScript
function addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>
```

添加一个MDNS服务，使用Promise方式作为异步方法。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [serviceInfo](arkts-network-mdns-discoveryeventinfo-i.md) | [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2204003](../errorcode-net-mdns.md#2204003-重复注册) |
| [2204008](../errorcode-net-mdns.md#2204008-删除服务失败) |
| [2204010](../errorcode-net-mdns.md#2204010-发送消息失败) |
