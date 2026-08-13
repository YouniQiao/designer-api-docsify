# removePreferencesFromCache

## removePreferencesFromCache

```TypeScript
function removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void
```

从缓存中移除指定的Preferences实例，通过name进行参数设置，使用callback异步回调。 应用首次调用[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用 [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次 getPreferences将会重新读取持久化文件，生成新的Preferences实例。 调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。 若使用[GSKV存储模式](../../../database/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上 减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-preferences-function removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void--><!--Device-preferences-function removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## 示例

FA模型示例：

```TypeScript
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
preferences.removePreferencesFromCache(context, 'myStore', (err: BusinessError) => {
  if (err) {
    console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
    return;
  }
  console.info("Succeeded in removing preferences.");
})
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    preferences.removePreferencesFromCache(this.context, 'myStore', (err: BusinessError) => {
      if (err) {
        console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
        return;
      }
      console.info("Succeeded in removing preferences.");
    })
  }
}
```


## removePreferencesFromCache

```TypeScript
function removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void
```

从缓存中移除指定的Preferences实例，通过Options进行参数设置，使用callback异步回调。 应用首次调用[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用 [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次 getPreferences将会重新读取持久化文件，生成新的Preferences实例。 调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。 若使用[GSKV存储模式](../../../database/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上 减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-preferences-function removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void--><!--Device-preferences-function removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [15501001](../errorcode-preferences.md#15501001-上下文环境非stage模型) |
| [15501002](../errorcode-preferences.md#15501002-options中传入的datagroupid参数非法) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## 示例

FA模型示例：

```TypeScript
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let options: preferences.Options = { name: 'myStore' };
preferences.removePreferencesFromCache(context, options, (err: BusinessError) => {
  if (err) {
    console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
    return;
  }
  console.info("Succeeded in removing preferences.");
})
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    preferences.removePreferencesFromCache(this.context, options, (err: BusinessError) => {
      if (err) {
        console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
        return;
      }
      console.info("Succeeded in removing preferences.");
    })
  }
}
```


## removePreferencesFromCache

```TypeScript
function removePreferencesFromCache(context: Context, name: string): Promise<void>
```

从缓存中移除指定的Preferences实例，通过name进行参数设置，使用Promise异步回调。 应用首次调用[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用 [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次 getPreferences将会重新读取持久化文件，生成新的Preferences实例。 调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。 若使用[GSKV存储模式](../../../database/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上 减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-preferences-function removePreferencesFromCache(context: Context, name: string): Promise<void>--><!--Device-preferences-function removePreferencesFromCache(context: Context, name: string): Promise<void>-End-->

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
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## 示例

FA模型示例：

```TypeScript
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let sp = preferences.removePreferencesFromCache(context, 'myStore');
sp.then(() => {
  console.info("Succeeded in removing preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
})
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let sp = preferences.removePreferencesFromCache(this.context, 'myStore');
    sp.then(() => {
      console.info("Succeeded in removing preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
    })
  }
}
```


## removePreferencesFromCache

```TypeScript
function removePreferencesFromCache(context: Context, options: Options): Promise<void>
```

从缓存中移除指定的Preferences实例，通过Options进行参数设置，使用Promise异步回调。 应用首次调用[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用 [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次 getPreferences将会重新读取持久化文件，生成新的Preferences实例。 调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。 若使用[GSKV存储模式](../../../database/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上 减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-preferences-function removePreferencesFromCache(context: Context, options: Options): Promise<void>--><!--Device-preferences-function removePreferencesFromCache(context: Context, options: Options): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [15501001](../errorcode-preferences.md#15501001-上下文环境非stage模型) |
| [15501002](../errorcode-preferences.md#15501002-options中传入的datagroupid参数非法) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## 示例

FA模型示例：

```TypeScript
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let options: preferences.Options = { name: 'myStore' };
let sp = preferences.removePreferencesFromCache(context, options);
sp.then(() => {
  console.info("Succeeded in removing preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
})
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    let sp = preferences.removePreferencesFromCache(this.context, options);
    sp.then(() => {
      console.info("Succeeded in removing preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to remove preferences. code =" + err.code + ", message = " + err.message);
    })
  }
}
```
