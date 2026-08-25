# deletePreferences

## 导入模块

```TypeScript
import { preferences } from 'kits/@kit.ArkData';
```

## deletePreferences

```TypeScript
function deletePreferences(context: Context, name: string, callback: AsyncCallback<void>): void
```

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。通过name进行参数设置，使用callback异步回调。调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。不支持该接口与其他preference接口并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500010](../errorcode-preferences.md#15500010-删除用户首选项持久化文件失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |


## deletePreferences

```TypeScript
function deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void
```

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。通过Options进行参数设置，使用callback异步回调。调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。不支持该接口与其他preference接口并发调用。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| options | [Options](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [15500010](../errorcode-preferences.md#15500010-删除用户首选项持久化文件失败) |
| [15501001](../errorcode-preferences.md#15501001-上下文环境非stage模型) |
| [15501002](../errorcode-preferences.md#15501002-options中传入的datagroupid参数非法) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |


## deletePreferences

```TypeScript
function deletePreferences(context: Context, name: string): Promise<void>
```

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。通过name进行参数设置，使用Promise异步回调。调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。不支持该接口与其他preference接口并发调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500010](../errorcode-preferences.md#15500010-删除用户首选项持久化文件失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |


## deletePreferences

```TypeScript
function deletePreferences(context: Context, options: Options): Promise<void>
```

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。通过Options进行参数设置，使用Promise异步回调。调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。不支持该接口与其他preference接口并发调用。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| options | [Options](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [15500010](../errorcode-preferences.md#15500010-删除用户首选项持久化文件失败) |
| [15501001](../errorcode-preferences.md#15501001-上下文环境非stage模型) |
| [15501002](../errorcode-preferences.md#15501002-options中传入的datagroupid参数非法) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |
