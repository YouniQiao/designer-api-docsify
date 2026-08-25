# AudioViewPicker

音频选择器对象，用来支撑选择和保存音频类文件等用户场景。在使用前，需要先创建AudioViewPicker实例。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

## 导入模块

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

创建AudioViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

## constructor

```TypeScript
constructor(context: Context)
```

创建AudioViewPicker对象，推荐使用该构造函数，获取context参考 [getHostContext](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#gethostcontext)。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

## save

```TypeScript
save(option?: AudioSaveOptions): Promise<Array<string>>
```

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中）， 用户可以保存一个或多个音频文件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [AudioSaveOptions](arkts-corefile-picker-audiosaveoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## save

```TypeScript
save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中）， 用户可以保存一个或多个音频文件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [AudioSaveOptions](arkts-corefile-picker-audiosaveoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起audioPicker界面（目前拉起的是documentPicker，audioPicker在规划中）， 用户可以保存一个或多个音频文件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## select

```TypeScript
select(option?: AudioSelectOptions): Promise<Array<string>>
```

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [AudioSelectOptions](arkts-corefile-picker-audioselectoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## select

```TypeScript
select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void
```

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [AudioSelectOptions](arkts-corefile-picker-audioselectoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## select

```TypeScript
select(callback: AsyncCallback<Array<string>>): void
```

通过选择模式拉起audioPicker界面，用户可以选择一个或多个音频文件。使用callback异步回调。 **系统能力**：SystemCapability.FileManagement.UserFileService

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |
