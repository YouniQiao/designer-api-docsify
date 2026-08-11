# copy

## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>
```

拷贝文件或目录，使用promise异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**起始版本：** 11

<!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>--><!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcUri | string | 是 |
| destUri | string | 是 |
| options | [CopyOptions](../../apis-arkui/arkts-apis/arkts-arkui-copyoptions-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900038 |
| 13900034 |
| 13900044 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |


## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void
```

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**起始版本：** 11

<!--Device-unnamed-declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcUri | string | 是 |
| destUri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900038 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |


## copy

```TypeScript
declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void
```

拷贝文件或者目录，使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**起始版本：** 11

<!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcUri | string | 是 |
| destUri | string | 是 |
| options | [CopyOptions](../../apis-arkui/arkts-apis/arkts-arkui-copyoptions-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 13900038 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900021 |
| 13900022 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900030 |
| 13900031 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |
