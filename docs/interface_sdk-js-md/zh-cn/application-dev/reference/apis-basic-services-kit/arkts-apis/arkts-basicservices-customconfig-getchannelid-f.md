# getChannelId

## 导入模块

```TypeScript
import { customConfig } from '@kit.BasicServicesKit';
```

## getChannelId

```TypeScript
function getChannelId(): string
```

获取应用的预装渠道号。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Customization.CustomConfig

**返回值：**

| 类型 |
| --- |
| string |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { customConfig } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let channelId: string = customConfig.getChannelId();
    console.info('app channelId is ' + channelId);
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { customConfig } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let channelId: string = customConfig.getChannelId();
    console.info('app channelId is ' + channelId);
  }
}
```
