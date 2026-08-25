# Reader

Reader的实例表示该设备支持的SE，如果支持eSE、SIM和SIM2，则返回3个实例，其中SIM2从API version 22开始支持。通过 [SEService.getReaders](arkts-connectivity-omapi-seservice-i.md#getreaders)获取Reader实例。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

## 导入模块

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## closeSessions

```TypeScript
closeSessions(): void
```

关闭在此Reader上打开的所有Session。所有这些Session打开的所有Channel都将关闭。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |

## getName

```TypeScript
getName(): string
```

返回此Reader的名称。如果此读卡器是SIM Reader，则其名称必须为“SIM”。如果此读卡器是SIM2 Reader，则其名称必须为“SIM2”。如果读卡器是eSE，则其名称须为“eSE”。

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

## isSecureElementPresent

```TypeScript
isSecureElementPresent(): boolean
```

检查当前Reader所对应的安全单元是否可用。

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
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |

## openSession

```TypeScript
openSession(): Session
```

在SE Reader实例上创建连接会话，返回Session实例。在一个Reader上可能同时打开多个会话。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| 类型 |
| --- |
| [Session](../../apis-camera-kit/arkts-apis/arkts-camera-camera-session-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |
