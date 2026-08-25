# createDiscoveryService

## 导入模块

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## createDiscoveryService

```TypeScript
function createDiscoveryService(context: Context, serviceType: string): DiscoveryService
```

返回一个DiscoveryService对象，该对象用于发现指定服务类型（serviceType）的MDNS服务。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| serviceType | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DiscoveryService](arkts-network-mdns-discoveryservice-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
