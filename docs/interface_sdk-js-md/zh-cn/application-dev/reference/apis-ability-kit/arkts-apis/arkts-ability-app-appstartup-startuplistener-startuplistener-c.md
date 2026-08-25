# StartupListener

本模块提供[应用启动框架](../../../application-models/app-startup.md)任务监听器的定义。

**起始版本：** 12

**系统能力：** SystemCapability.Ability.AppStartup

## 导入模块

```TypeScript
import { StartupListener } from 'kits/@kit.AbilityKit';
```

## onCompleted

```TypeScript
onCompleted?(error: BusinessError<void>): void
```

在所有启动任务完成时调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| error | [BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | 是 |
