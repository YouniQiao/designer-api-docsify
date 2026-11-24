# CliCmdInfo

```TypeScript
interface CliCmdInfo
```

表示CLI（Command Line Interface，命令行界面）命令信息。

**起始版本：** 26.0.0

<!--Device-abilityToolAccessCtrl-interface CliCmdInfo--><!--Device-abilityToolAccessCtrl-interface CliCmdInfo-End-->

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## cliCmdName

```TypeScript
cliCmdName: string
```

CLI命令名称，用于指定CLI命令。需传入系统支持的CLI命令名称，如'ohos-batteryManager'。长度不超过512字节，不能为空。

**类型：** string

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-CliCmdInfo-cliCmdName: string--><!--Device-CliCmdInfo-cliCmdName: string-End-->

**系统能力：** SystemCapability.Security.Asset

## subCliCmdName

```TypeScript
subCliCmdName: string
```

CLI子命令名称，用于指定CLI子命令。需传入指定CLI命令支持的子命令名称，如'total-energy'。长度不超过512字节，可为空字符串。

**类型：** string

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-CliCmdInfo-subCliCmdName: string--><!--Device-CliCmdInfo-subCliCmdName: string-End-->

**系统能力：** SystemCapability.Security.Asset
