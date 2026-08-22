# getCfgDirList（系统接口）

## 导入模块

```TypeScript
import { configPolicy } from '@kit.BasicServicesKit';
```

## getCfgDirList

```TypeScript
function getCfgDirList(callback: AsyncCallback<Array<string>>): void
```

获取配置层级目录列表，按优先级从低到高。使用callback异步回调。

**起始版本：** 23

<!--Device-configPolicy-function getCfgDirList(callback: AsyncCallback<Array<string>>): void--><!--Device-configPolicy-function getCfgDirList(callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 | 回调函数。当获取配置层级目录列表成功，err为undefined， data为获取到的配置层级目录列表；否则err为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br>1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      configPolicy.getCfgDirList((error: BusinessError, value: Array<string>) => {
        if (error == null) {
          console.info('value is ' + value);
        } else {
          console.error('error: ' + error.code + ', ' + error.message);
        }
      });
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
      configPolicy.getCfgDirList((error: BusinessError | null, value: Array<string> | undefined) => {
        if (error == null) {
          console.info('value is ' + value);
        } else {
          console.error('error: ' + error.code + ', ' + error.message);
        }
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error('error: ' + code + ', ' + message);
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { configPolicy, BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      configPolicy.getCfgDirList().then((value: Array<string>) => {
        console.info('value is ' + value);
      }).catch((error: BusinessError) => {
        console.error('getCfgDirList promise error: ' + error.code + ', ' + error.message);
      });
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
      configPolicy.getCfgDirList().then((value: Array<string>) => {
        console.info('value is ' + value);
      }).catch((error: Error) => {
        console.error('getCfgDirList promise error: ' + error);
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error('error: ' + code + ', ' + message);
    }
  }
}
```


## getCfgDirList

```TypeScript
function getCfgDirList(): Promise<Array<string>>
```

获取配置层级目录列表，按优先级从低到高。使用Promise异步回调。

**起始版本：** 23

<!--Device-configPolicy-function getCfgDirList(): Promise<Array<string>>--><!--Device-configPolicy-function getCfgDirList(): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise对象，返回配置层级目录列表。 |

**示例**

参见 [getCfgDirList](#getcfgdirlist)

