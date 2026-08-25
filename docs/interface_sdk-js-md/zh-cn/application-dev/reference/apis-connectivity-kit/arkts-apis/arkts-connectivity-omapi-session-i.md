# Session

Session的实例表示在某个SE Reader实例上创建连接会话。通过[Reader.openSession](arkts-connectivity-omapi-reader-i.md#opensession)获取Session实例。

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

关闭与SE的当前会话连接。这将关闭此Session打开的所有Channel。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |

## closeChannels

```TypeScript
closeChannels(): void
```

关闭此Session上打开的所有Channel。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |

## getATR

```TypeScript
getATR(): number[]
```

获取该SE的ATR。如果该SE的ATR不可用，则应返回空数组。

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
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |

## getReader

```TypeScript
getReader(): Reader
```

获取提供此Session的Reader实例。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| 类型 |
| --- |
| [Reader](arkts-connectivity-omapi-reader-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## isClosed

```TypeScript
isClosed(): boolean
```

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

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[]): Promise<Channel>
```

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[], callback: AsyncCallback<Channel>): void
```

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[], p2: number): Promise<Channel>
```

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |
| p2 | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## openBasicChannel

```TypeScript
openBasicChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void
```

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |
| p2 | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[]): Promise<Channel>
```

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[], callback: AsyncCallback<Channel>): void
```

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[], p2: number): Promise<Channel>
```

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |
| p2 | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |

## openLogicalChannel

```TypeScript
openLogicalChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void
```

打开逻辑通道，参考[ISO 7816-4]协议，返回Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aid | number[] | 是 |
| p2 | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Channel](arkts-connectivity-omapi-channel-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3300101](../errorcode-se.md#3300101-se服务状态异常) |
| [3300102](../errorcode-se.md#3300102-找不到对应se安全单元异常) |
| [3300103](../errorcode-se.md#3300103-无法获取访问控制规则异常) |
| [3300104](../errorcode-se.md#3300104-se芯片io异常) |
