# getCfgDirListSync（系统接口）

## 导入模块

```TypeScript
import { configPolicy } from '@kit.BasicServicesKit';
```

## getCfgDirListSync

```TypeScript
function getCfgDirListSync(): Array<string>
```

获取配置层级目录列表，按优先级从低到高。

**起始版本：** 23

<!--Device-configPolicy-function getCfgDirListSync(): Array<string>--><!--Device-configPolicy-function getCfgDirListSync(): Array<string>-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 返回配置层级目录列表。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let result: Array<string> = configPolicy.getCfgDirListSync();
      console.info('result is ' + result);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error('error: ' + code + ', ' + message);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let result: Array<string> = configPolicy.getCfgDirListSync();
      console.info('result is ' + result);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error('error: ' + code + ', ' + message);
    }
  }
}
```

