# removePreferencesFromCacheSync

## removePreferencesFromCacheSync

```TypeScript
function removePreferencesFromCacheSync(context: Context, name: string): void
```

从缓存中移除指定的Preferences实例，通过name进行参数设置，此为同步接口。

应用首次调用[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用  
[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../../../database/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-preferences-function removePreferencesFromCacheSync(context: Context, name: string): void--><!--Device-preferences-function removePreferencesFromCacheSync(context: Context, name: string): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [15500000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500000-内部错误) |

## 示例

FA模型示例：

```TypeScript
// 获取context
import { featureAbility } from '@kit.AbilityKit';

let context = featureAbility.getContext();
preferences.removePreferencesFromCacheSync(context, 'myStore');
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    preferences.removePreferencesFromCacheSync(this.context, 'myStore');
  }
}
```


## removePreferencesFromCacheSync

```TypeScript
function removePreferencesFromCacheSync(context: Context, options: Options): void
```

从缓存中移除指定的Preferences实例，通过Options进行参数设置，此为同步接口。

应用首次调用[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用  
[getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../../../database/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-preferences-function removePreferencesFromCacheSync(context: Context, options: Options): void--><!--Device-preferences-function removePreferencesFromCacheSync(context: Context, options: Options): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [15501001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501001-上下文环境非stage模型) |
| [15501002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-preferences.md#15501002-options中传入的datagroupid参数非法) |
| [15500000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-preferences.md#15500000-内部错误) |

## 示例

FA模型示例：

```TypeScript
// 获取context
import { featureAbility } from '@kit.AbilityKit';

let context = featureAbility.getContext();
let options: preferences.Options = { name: 'myStore' };
preferences.removePreferencesFromCacheSync(context, options);
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    preferences.removePreferencesFromCacheSync(this.context, options);
  }
}
```
