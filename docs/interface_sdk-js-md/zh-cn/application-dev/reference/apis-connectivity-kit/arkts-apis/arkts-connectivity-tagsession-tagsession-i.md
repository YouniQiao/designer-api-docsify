# TagSession

本模块是对NFC TagSession的使用说明。

> **注意：**&gt;
> 导入tag模块编辑器报错，在某个具体设备型号上能力可能超出工程默认设备定义的能力集范围，如需要使用此部分能力需额外配置自定义syscap，参考
> [syscap开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap)。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NFC.Tag

## connect

```TypeScript
connect(): void
```

和标签建立连接。在从标签读取数据或将数据写入标签之前，必须调用此方法。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |

## connectTag

```TypeScript
connectTag(): boolean
```

和标签建立连接。在从标签读取数据或将数据写入标签之前，必须调用此方法。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** connect

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| boolean |

## getMaxSendLength

```TypeScript
getMaxSendLength(): number
```

查询可以发送到标签的最大数据长度。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getMaxTransmitSize](#getmaxtransmitsize)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| number |

## getMaxTransmitSize

```TypeScript
getMaxTransmitSize(): number
```

查询可以发送到标签的最大数据长度。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |

## getSendDataTimeout

```TypeScript
getSendDataTimeout(): number
```

查询发送数据到Tag的等待超时时间，单位是毫秒。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getTimeout](#gettimeout)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| number |

## getTagInfo

```TypeScript
getTagInfo(): tag.TagInfo
```

获取该Tag被分发时，NFC服务所提供的Tag数据对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getTagInfo](arkts-connectivity-tag-gettaginfo-f.md)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| tag.TagInfo |

## getTimeout

```TypeScript
getTimeout(): number
```

查询发送数据到Tag的等待超时时间，单位是毫秒。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |

## isConnected

```TypeScript
isConnected(): boolean
```

检查是否已与标签建立连接。如果返回未连接，则需要先调用[tagSession.connect](#connect)建立连接。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## isTagConnected

```TypeScript
isTagConnected(): boolean
```

检查是否已与标签建立连接。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** isConnected

**系统能力：** SystemCapability.Communication.NFC.Tag

**返回值：**

| 类型 |
| --- |
| boolean |

## reset

```TypeScript
reset(): void
```

重置与标签的连接。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [resetConnection](#resetconnection)

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

## resetConnection

```TypeScript
resetConnection(): void
```

重置与标签的连接。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |

## sendData

```TypeScript
sendData(data: number[]): Promise<number[]>
```

发送指令到Tag上。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** transmit

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

## sendData

```TypeScript
sendData(data: number[], callback: AsyncCallback<number[]>): void
```

发送指令到Tag上。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** transmit

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 是 |

## setSendDataTimeout

```TypeScript
setSendDataTimeout(timeout: number): boolean
```

设置发送数据到Tag的等待超时时间，单位是毫秒。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** setTimeout

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setTimeout

```TypeScript
setTimeout(timeout: number): void
```

设置发送数据到Tag的等待超时时间，单位是毫秒。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |

## transmit

```TypeScript
transmit(data: number[]): Promise<number[]>
```

发送指令到Tag上。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
| [3100204](../errorcode-nfc.md#3100204-nfc芯片io异常) |

## transmit

```TypeScript
transmit(data: number[], callback: AsyncCallback<number[]>): void
```

发送指令到Tag上。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
| [3100204](../errorcode-nfc.md#3100204-nfc芯片io异常) |
