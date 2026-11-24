# AppInfo

```TypeScript
interface AppInfo
```

表示应用信息。

**起始版本：** 26.1.0

<!--Device-abilityToolAccessCtrl-interface AppInfo--><!--Device-abilityToolAccessCtrl-interface AppInfo-End-->

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## bundleName

```TypeScript
bundleName: string
```

应用包名，用于唯一标识一个应用。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AppInfo-bundleName: string--><!--Device-AppInfo-bundleName: string-End-->

**系统能力：** SystemCapability.Security.Asset

## index

```TypeScript
index: number
```

应用分身索引。0表示主应用，大于0表示对应的分身应用。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AppInfo-index: number--><!--Device-AppInfo-index: number-End-->

**系统能力：** SystemCapability.Security.Asset
