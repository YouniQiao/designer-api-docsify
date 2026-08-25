# SystemPasteboard

系统剪贴板对象。 在调用SystemPasteboard的接口前，需要先通过[getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md)获取系统剪贴板。

**起始版本：** 6

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 导入模块

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

清空系统剪贴板内容，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [clearData](#cleardata)(callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clear

```TypeScript
clear(): Promise<void>
```

清空系统剪贴板内容，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [clearData](#cleardata)()

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## clearData

```TypeScript
clearData(callback: AsyncCallback<void>): void
```

清空系统剪贴板内容，使用callback异步回调。调用此方法后，系统将删除剪贴板中的所有数据，触发已注册的'update'监听回调。 清空成功后，剪贴板中将没有任何数据，hasData方法将返回false。适用于需要异步清空剪贴板且不阻塞主线程的场景，如UI响应优先的交互流程。 与同步接口[clearDataSync](#cleardatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clearData

```TypeScript
clearData(): Promise<void>
```

清空系统剪贴板内容，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## clearDataSync

```TypeScript
clearDataSync(): void
```

清空系统剪贴板内容，此接口为同步接口。适用于需要在关键业务流程中同步清空剪贴板数据，或需要立即确认清空结果的场景。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

| 错误码ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |

## detectPatterns

```TypeScript
detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>
```

检测**本地**剪贴板中存在的[Pattern](arkts-basicservices-pasteboard-pattern-e.md)模式，使用Promise异步回调。 本地剪贴板指当前设备上的剪贴板数据，不包括跨设备传输的远端剪贴板数据。 适用于应用在粘贴数据前需要检测剪贴板内容是否包含特定类型的数据(如URL、邮箱、电话号码等)，以便进行相应处理或提供智能提示的场景。

**起始版本：** 13

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [patterns](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodlist-patternoptions-i.md) | Array & lt;Pattern & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Pattern & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getChangeCount

```TypeScript
getChangeCount(): number
```

获取剪贴板内容的变化次数。执行成功时返回剪贴板内容的变化次数，否则返回0。 当剪贴板内容过期或调用[clearDataSync](#cleardatasync)等接口导致剪贴板内容为空时，内容变化次数不会因此改变。 系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被记录为多次更改，每次复制均会导致内容变化次数增加。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| number |

## getData

```TypeScript
getData(callback: AsyncCallback<PasteData>): void
```

读取系统剪贴板内容，使用callback异步回调。将剪贴板数据封装为PasteData对象返回。调用此方法后，系统将从剪贴板服务读取当前内容，通过callback返回PasteData对象。 读取成功后，应用可以通过PasteData对象的方法获取具体的数据内容（如文本、HTML、URI等）。适用于需要异步读取剪贴板内容的场景，如UI响应优先、避免阻塞主线程。 与[getDataSync](#getdatasync)相比，getData不会阻塞UI线程，适合处理大量数据或远端数据。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.READ_PASTEBOARD

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [27787277](../errorcode-pasteboard.md#27787277-另外一个复制或粘贴正在进行) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getData

```TypeScript
getData(): Promise<PasteData>
```

读取系统剪贴板内容，将剪贴板数据封装为PasteData对象返回，使用Promise异步回调。适用于需要异步读取剪贴板内容的场景，如UI响应优先、避免阻塞主线程。 适用于应用需要使用标准化数据结构[UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md)读取剪贴板数据的场景。

**起始版本：** 9

**需要权限：** 
- API版本12+：ohos.permission.READ_PASTEBOARD

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [27787277](../errorcode-pasteboard.md#27787277-另外一个复制或粘贴正在进行) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getDataSource

```TypeScript
getDataSource(): string
```

获取剪贴板数据的来源应用名称。适用于安全审计、数据追踪或向用户提示数据来源等场景。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |

## getDataSync

```TypeScript
getDataSync(): PasteData
```

读取系统剪贴板内容，此接口为同步接口。适用于应用需要在关键业务流程中同步获取剪贴板数据，或需要立即处理剪贴板内容的场景。 避免在UI线程调用此接口，以免阻塞界面；处理大量数据或远端数据时，建议使用异步接口[getData](arkts-basicservices-pasteboard-pastedatarecord-i.md#getdata)。

**起始版本：** 11

**需要权限：** 
- API版本12+：ohos.permission.READ_PASTEBOARD

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getDataWithProgress

```TypeScript
getDataWithProgress(params: GetDataParams): Promise<PasteData>
```

获取剪贴板的内容和进度，使用Promise异步回调，不支持对文件夹的拷贝。 对于大文件拷贝操作，建议设置进度监听以跟踪拷贝进度，避免在UI线程长时间等待；建议合理设置目标路径以确保有足够的存储空间。 适用于大文件粘贴场景。在此场景下，可通过此回调显示拷贝进度，或监听拷贝过程以便在必要时取消操作。

**起始版本：** 15

**需要权限：** ohos.permission.READ_PASTEBOARD

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [GetDataParams](arkts-basicservices-pasteboard-getdataparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900003](../errorcode-pasteboard.md#12900003-另外一个复制或粘贴正在进行) |
| [12900007](../errorcode-pasteboard.md#12900007-文件拷贝失败) |
| [12900008](../errorcode-pasteboard.md#12900008-启动进度条hap失败) |
| [12900009](../errorcode-pasteboard.md#12900009-进度上报异常) |
| [12900010](../errorcode-pasteboard.md#12900010-获取粘贴数据失败) |

## getMimeTypes

```TypeScript
getMimeTypes(): Promise<Array<string>>
```

读取剪贴板中存在的MIME类型，使用Promise异步回调。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getPasteData

```TypeScript
getPasteData(callback: AsyncCallback<PasteData>): void
```

读取系统剪贴板内容，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getData](#getdata)(callback: AsyncCallback&lt;PasteData&gt;)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getPasteData

```TypeScript
getPasteData(): Promise<PasteData>
```

读取系统剪贴板内容，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getData](#getdata)()

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; |

## getUnifiedData

```TypeScript
getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>
```

读取系统剪贴板内容，使用Promise异步回调。 适用于需要使用标准化数据结构[UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md)进行跨应用数据交换的场景。 当应用需要与其他支持UnifiedData的应用进行数据共享，或需要处理复杂的多类型数据时，使用本接口。 与[getData](#getdata)相比，getUnifiedData提供了更标准化的数据格式。

**起始版本：** 12

**需要权限：** ohos.permission.READ_PASTEBOARD

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;unifiedDataChannel.UnifiedData & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [27787277](../errorcode-pasteboard.md#27787277-另外一个复制或粘贴正在进行) |

## getUnifiedDataSync

```TypeScript
getUnifiedDataSync(): unifiedDataChannel.UnifiedData
```

读取系统剪贴板内容，此接口为同步接口。适用于需要同步使用标准化数据结构UnifiedData进行跨应用数据交换的场景。 当应用需要在关键业务流程中立即获取剪贴板数据，且需要与其他支持UnifiedData的应用进行数据共享时使用。 由于获取剪贴板中数据的时延受数据量大小与网络环境的影响，调用此接口可能耗时较长，建议开发者在非UI线程调用。

**起始版本：** 12

**需要权限：** ohos.permission.READ_PASTEBOARD

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| unifiedDataChannel.UnifiedData |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |

## hasData

```TypeScript
hasData(callback: AsyncCallback<boolean>): void
```

判断系统剪贴板中是否有内容，使用callback异步回调。适用于需要异步判断剪贴板是否有内容且不阻塞主线程的场景，如UI响应优先的交互流程。 与同步接口[hasDataSync](#hasdatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## hasData

```TypeScript
hasData(): Promise<boolean>
```

判断系统剪贴板中是否有内容，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## hasDataSync

```TypeScript
hasDataSync(): boolean
```

判断系统剪贴板中是否有内容，此接口为同步接口。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |

## hasDataType

```TypeScript
hasDataType(mimeType: string): boolean
```

检查剪贴板内容中是否有指定类型的数据。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |

## hasPasteData

```TypeScript
hasPasteData(callback: AsyncCallback<boolean>): void
```

判断系统剪贴板中是否有内容，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [hasData](#hasdata)(callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## hasPasteData

```TypeScript
hasPasteData(): Promise<boolean>
```

判断系统剪贴板中是否有内容，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [hasData](#hasdata)()

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## hasRemoteData

```TypeScript
hasRemoteData(): boolean
```

判断剪贴板数据是否在远端设备上。由于数据跨端传输耗时较大，如果剪贴板数据在远端设备上，不建议在UI线程执行检查剪贴板数据中是否包含自定义数据类型，或读取剪贴板数据。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| boolean |

## isRemoteData

```TypeScript
isRemoteData(): boolean
```

判断剪贴板中的数据是否来自其他设备。由于数据跨端传输耗时较大，如果剪贴板数据在远端设备上，不建议在UI线程执行检查剪贴板数据中是否包含自定义数据类型，或读取剪贴板数据。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |

## off('update')

```TypeScript
off(type: 'update', callback?: () => void): void
```

取消订阅系统剪贴板内容变化事件。  
- 与on('update')方法配合使用，取消订阅的是通过on('update')订阅的事件监听。  
- 必须在已订阅的情况下才能调用。  
- 如果callback参数未填，清除本应用的所有监听回调；否则清除指定监听回调。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'update' | 是 |
| callback | () = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## offRemoteUpdate

```TypeScript
offRemoteUpdate(callback?: UpdateCallback): void
```

取消订阅跨设备剪贴板内容变化事件。  
- 与onRemoteUpdate()方法配合使用，取消订阅的是通过onRemoteUpdate()订阅的事件监听。  
- 必须在已订阅的情况下才能调用。  
- 如果callback参数未填，清除本应用的所有远端监听回调；否则清除指定远端监听回调。

**起始版本：** 22

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | 否 |

## on('update')

```TypeScript
on(type: 'update', callback: () => void): void
```

订阅系统剪贴板内容变化事件，当系统剪贴板中内容变化时触发用户程序的回调。调用此方法后，系统将在剪贴板服务中注册监听器，剪贴板内容被写入、清空或修改时触发回调。 可注册多个监听器，需在适当时机调用off取消监听以释放资源。当应用需要实时响应剪贴板内容变化时使用，如自动检测剪贴板中的特定格式数据、实现智能粘贴建议等场景。  
- 订阅后必须在不再需要监听时调用off('update')取消订阅。  
- 未取消订阅会导致回调函数持续监听剪贴板变化，可能造成内存泄漏或多次回调触发。  
- 建议在组件/页面销毁时取消订阅。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'update' | 是 |
| callback | () = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onRemoteUpdate

```TypeScript
onRemoteUpdate(callback: UpdateCallback): void
```

订阅跨设备剪贴板内容变化事件，当远端设备系统剪贴板中内容变化时触发用户程序的回调。  
- 订阅后必须在不再需要监听时调用  
[offRemoteUpdate](#offremoteupdate) 取消订阅。  
- 未取消订阅会导致回调函数持续监听远端变化，造成内存泄漏。  
- 建议在组件/页面销毁时取消订阅。

**起始版本：** 22

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | 是 |

## removeAppShareOptions

```TypeScript
removeAppShareOptions(): void
```

删除应用全局的可粘贴的范围。适用于应用需要取消之前设置的粘贴范围限制，恢复剪贴板数据默认粘贴范围的场景。  
- 与setAppShareOptions()方法（应用设置本应用剪贴板数据的可粘贴范围）配合使用。  
- 删除的是通过setAppShareOptions()设置的分享范围。  
- 必须在已设置分享范围的情况下才能调用。

**起始版本：** 14

**需要权限：** 
- API版本14+：ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setAppShareOptions

```TypeScript
setAppShareOptions(shareOptions: ShareOption): void
```

应用设置本应用剪贴板数据的可粘贴范围。适用于应用需要全局限制本应用产生的剪贴板数据的粘贴范围，如金融类应用需要保护用户敏感信息的场景。  
- 与removeAppShareOptions()方法（删除应用全局的可粘贴的范围）配合使用。  
- 需要删除已设置的分享范围时，调用removeAppShareOptions()。  
- 在何处设置就在何处删除，确保分享范围设置和删除的一致性。

**起始版本：** 14

**需要权限：** 
- API版本14+：ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [shareOptions](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) | [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900006](../errorcode-pasteboard.md#12900006-设置已存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setData

```TypeScript
setData(data: PasteData, callback: AsyncCallback<void>): void
```

将数据写入系统剪贴板，使用callback异步回调。调用此方法后，系统会将PasteData对象写入到系统剪贴板中。写入成功后，其他应用可以读取该剪贴板数据。 写入的数据会替换剪贴板中已有的内容。适用于需要异步写入剪贴板内容的场景，如UI响应优先、避免阻塞主线程。 与[setDataSync](#setdatasync)相比，setData不会阻塞UI线程。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [27787277](../errorcode-pasteboard.md#27787277-另外一个复制或粘贴正在进行) |
| [27787278](../errorcode-pasteboard.md#27787278-禁止复制) |

## setData

```TypeScript
setData(data: PasteData): Promise<void>
```

将数据写入系统剪贴板，使用Promise异步回调。适用于需要异步写入剪贴板且不阻塞主线程的场景，如UI响应优先的交互流程。 与同步接口[setDataSync](#setdatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [27787277](../errorcode-pasteboard.md#27787277-另外一个复制或粘贴正在进行) |
| [27787278](../errorcode-pasteboard.md#27787278-禁止复制) |

## setDataSync

```TypeScript
setDataSync(data: PasteData): void
```

将数据写入系统剪贴板，此接口为同步接口。适用于应用需要在关键业务流程中同步完成剪贴板数据写入，或需要立即确认写入结果的场景。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |

## setPasteData

```TypeScript
setPasteData(data: PasteData, callback: AsyncCallback<void>): void
```

将数据写入系统剪贴板，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setData](#setdata)(data: PasteData, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setPasteData

```TypeScript
setPasteData(data: PasteData): Promise<void>
```

将数据写入系统剪贴板，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setData](#setdata)(data: PasteData)

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setUnifiedData

```TypeScript
setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>
```

将数据写入系统剪贴板，使用Promise异步回调。适用于需要异步写入剪贴板且不阻塞主线程的场景，如UI响应优先的交互流程。 与同步接口[setUnifiedDataSync](#setunifieddatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [27787277](../errorcode-pasteboard.md#27787277-另外一个复制或粘贴正在进行) |
| [27787278](../errorcode-pasteboard.md#27787278-禁止复制) |

## setUnifiedDataSync

```TypeScript
setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void
```

将数据写入系统剪贴板，此接口为同步接口。适用于需要同步使用标准化数据结构UnifiedData进行跨应用数据交换的场景。当应用需要在关键业务流程中立即写入剪贴板数据， 且需要与其他支持[UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md)的应用进行数据共享时使用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12900005](../errorcode-pasteboard.md#12900005-请求超时) |
