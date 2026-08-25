# HceService

提供HCE卡模拟的实现，主要包括接收对端读卡设备的APDU数据，并响应APDU数据到对端读卡设备。使用HCE相关接口前，必须先判断设备是否支持HCE卡模拟能力。

**起始版本：** 8

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

## 导入模块

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## off('hceCmd')

```TypeScript
off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void
```

取消APDU数据接收的订阅。使用callback异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hceCmd' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## on('hceCmd')

```TypeScript
on(type: 'hceCmd', callback: AsyncCallback<number[]>): void
```

订阅回调，用于接收对端读卡设备发送的APDU数据，应用程序需要在HCE卡模拟页面的onCreate函数里面调用该订阅函数。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hceCmd' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## sendResponse

```TypeScript
sendResponse(responseApdu: number[]): void
```

发送APDU数据到对端读卡设备。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [transmit](#transmit)

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| responseApdu | number[] | 是 |

## start

```TypeScript
start(elementName: ElementName, aidList: string[]): void
```

启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 |
| aidList | string[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100301](../errorcode-nfc.md#3100301-nfc卡模拟状态异常) |

## startHCE

```TypeScript
startHCE(aidList: string[]): boolean
```

启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [start](#start)

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aidList | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## stop

```TypeScript
stop(elementName: ElementName): void
```

停止HCE业务功能。包括取消APDU数据接收的订阅，退出当前应用前台优先，释放动态注册的AID列表。应用程序需要在HCE卡模拟页面的onDestroy函数里调用该接口。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100301](../errorcode-nfc.md#3100301-nfc卡模拟状态异常) |

## stopHCE

```TypeScript
stopHCE(): boolean
```

停止HCE业务功能。包括退出当前应用前台优先，释放动态注册的AID列表，释放hceCmd的订阅。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stop](#stop)

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**返回值：**

| 类型 |
| --- |
| boolean |

## transmit

```TypeScript
transmit(response: number[]): Promise<void>
```

发送APDU数据到对端读卡设备，使用Promise异步回调。应用程序必须在 on收到读卡设备发送的APDU数据后，才调用该接口响应数 据。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| response | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100301](../errorcode-nfc.md#3100301-nfc卡模拟状态异常) |

## transmit

```TypeScript
transmit(response: number[], callback: AsyncCallback<void>): void
```

发送APDU数据到对端读卡设备，应用程序必须在on收到读 卡设备发送的APDU数据后，才调用该接口响应数据。使用Callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| response | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100301](../errorcode-nfc.md#3100301-nfc卡模拟状态异常) |
