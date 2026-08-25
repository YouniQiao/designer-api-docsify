# GroupConfig

下载任务分组配置选项。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

## 导入模块

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## gauge

```TypeScript
gauge?: boolean
```

后台任务的进度通知策略。  
- true，显示进度、成功、失败通知。 - false，仅显示成功、失败通知。  
默认为false。

**类型：** boolean

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

## notification

```TypeScript
notification: Notification
```

通知栏自定义设置。默认值为`{}`

**类型：** Notification

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent
