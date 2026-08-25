# SEService

SEService表示可用于连接到系统中所有可用SE的连接（服务），通过[createService](arkts-connectivity-omapi-createservice-f.md)获取SEService实例。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

## 导入模块

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## getReaders

```TypeScript
getReaders(): Reader[]
```

返回可用SE Reader的数组，包含该设备上支持的所有的安全单元。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| 类型 |
| --- |
| [Reader](arkts-connectivity-omapi-reader-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## getVersion

```TypeScript
getVersion(): string
```

返回此实现所基于的Open Mobile API规范的版本号。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## isConnected

```TypeScript
isConnected(): boolean
```

检查SE服务是否已连接。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## shutdown

```TypeScript
shutdown(): void
```

释放该Service分配的所有SE资源。此后[isConnected](#isconnected)将返回false。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
