# setAbilityFileTypesForSelf（系统接口）

## 导入模块

```TypeScript
```

## setAbilityFileTypesForSelf

```TypeScript
function setAbilityFileTypesForSelf(moduleName: string, abilityName: string, fileTypes: Array<string>): void
```

设置当前应用支持打开的文件类型。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_SELF_SKILLS

<!--Device-bundleManager-function setAbilityFileTypesForSelf(moduleName: string, abilityName: string, fileTypes: Array<string>): void--><!--Device-bundleManager-function setAbilityFileTypesForSelf(moduleName: string, abilityName: string, fileTypes: Array<string>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| abilityName | string | 是 |
| fileTypes | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17700351](../errorcode-bundle.md#17700351-无效的文件类型) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |

**示例**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let moduleName: string = "entry";
let abilityName: string = "EntryAbility";
let fileTypes: Array<string> = ["general.png", "general.jpeg"];

try {
  bundleManager.setAbilityFileTypesForSelf(moduleName, abilityName, fileTypes);
  hilog.info(0x0000, 'testTag', 'setAbilityFileTypesForSelf successfully');
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'setAbilityFileTypesForSelf failed. Cause: %{public}s', message);
}
```
