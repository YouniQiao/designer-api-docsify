# Channel

Channel的实例表示在某个Session实例上创建通道，可能为基础通道或逻辑通道。通过 [Session.openBasicChannel](arkts-connectivity-omapi-session-i.md#openbasicchannel)或 [Session.openLogicalChannel](arkts-connectivity-omapi-session-i.md#openlogicalchannel)获取Channel实例。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

## 导入模块

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## close

```TypeScript
close(): void
```

关闭Channel。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## getSelectResponse

```TypeScript
getSelectResponse(): number[]
```

获取SELECT Applet时的响应数据，包含状态字。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| 类型 |
| --- |
| number[] |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## getSession

```TypeScript
getSession(): Session
```

获取打开该Channel的Session对象。

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

## isBasicChannel

```TypeScript
isBasicChannel(): boolean
```

检查该Channel是否为基础Channel。

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

## isClosed

```TypeScript
isClosed(): boolean
```

检查该Channel是否已被关闭。

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

## transmit

```TypeScript
transmit(command: number[]): Promise<number[]>
```

向SE发送APDU数据，数据符合ISO/IEC 7816规范。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## transmit

```TypeScript
transmit(command: number[], callback: AsyncCallback<number[]>): void
```

向SE发送APDU数据，数据符合ISO/IEC 7816规范。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |
