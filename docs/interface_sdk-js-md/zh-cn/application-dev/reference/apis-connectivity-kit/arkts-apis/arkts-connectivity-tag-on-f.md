# on

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## on('readerMode')

```TypeScript
function on(type: 'readerMode', elementName: ElementName, discTech: number[], callback: AsyncCallback<TagInfo>): void
```

订阅NFC Tag读卡事件，实现前台应用优先分发。设备会进入读卡器模式，同时关闭卡模拟。通过discTech设置支持的读卡技术类型，通过callback方式获取到Tag的[TagInfo](arkts-connectivity-tag-taginfo-i.md)信 息。需要与取消读卡器模式的 tag.off成对使用，如果已通过 on进行设置，需要在页面退出前台或页面销毁时调用 tag.off。使用 callback异步回调。与注册读卡器模式的 tag.on 互斥使用。

**起始版本：** 11

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'readerMode' | 是 |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 |
| discTech | number[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100202](../errorcode-nfc.md#3100202-应用状态错误) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |


## on('readerModeWithInterval')

```TypeScript
function on(
    type: 'readerModeWithInterval',
    elementName: ElementName,
    discTech: number[],
    callback: Callback<TagInfo>,
    interval: number
  ): void
```

订阅NFC Tag读卡事件，实现前台应用优先分发，并支持卡在位检测间隔设置。使用callback异步回调。  
- 设备会进入读卡器模式，同时关闭卡模拟。  
- 通过discTech设置支持的读卡技术类型，通过callback方式获取到Tag的[TagInfo](arkts-connectivity-tag-taginfo-i.md)信息，通过interval设置卡在位检测间隔。  
- 需要与取消读卡器模式的  
tag.off成对使 用，如果已通过on进行设置，需要在页面退出前台或页面销毁时调用 tag.off。  
- 与注册读卡器模式的  
tag.on 互斥使用。

**起始版本：** 23

**需要权限：** ohos.permission.NFC_TAG

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'readerModeWithInterval' | 是 |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | 是 |
| discTech | number[] | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | 是 |
| interval | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100201](../errorcode-nfc.md#3100201-nfc服务读写tag错误) |
| [3100202](../errorcode-nfc.md#3100202-应用状态错误) |
