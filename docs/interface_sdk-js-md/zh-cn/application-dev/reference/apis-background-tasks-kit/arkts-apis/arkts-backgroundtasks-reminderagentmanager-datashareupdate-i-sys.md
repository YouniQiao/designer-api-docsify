# DataShareUpdate（系统接口）

更新数据库需要的参数信息。数据提供方需要在module.json5中的proxyData节点定义要共享的表的标识，读写权限和基本信息。配置方式请见 [数据提供方应用的开发](../../../database/share-data-by-silent-access-sys.md#数据提供方应用的开发)。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.ReminderAgent

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## equalTo

```TypeScript
equalTo: Record<string, double | string | boolean>
```

指示筛选条件，当前仅支持通过等于筛选。

**类型：** ArkTS-Dyn: Record&lt;string, number \| string \| boolean&gt;  <br>ArkTS-Sta：Record&lt;string, double \| string \| boolean&gt;

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.ReminderAgent

**系统接口：** 此接口为系统接口。

## uri

```TypeScript
uri: string
```

数据使用的URI，是跨应用数据访问的唯一标识。

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.ReminderAgent

**系统接口：** 此接口为系统接口。

## value

```TypeScript
value: ValuesBucket
```

指示要更新的数据。

**类型：** [ValuesBucket](../../apis-arkdata/arkts-apis/arkts-arkdata-valuesbucket-t.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.ReminderAgent

**系统接口：** 此接口为系统接口。
