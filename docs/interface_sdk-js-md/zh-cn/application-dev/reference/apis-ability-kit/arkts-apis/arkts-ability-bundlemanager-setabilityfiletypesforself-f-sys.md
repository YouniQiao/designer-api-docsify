# setAbilityFileTypesForSelf（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## setAbilityFileTypesForSelf

```TypeScript
function setAbilityFileTypesForSelf(moduleName: string, abilityName: string, fileTypes: Array<string>): void
```

设置当前应用支持打开的文件类型。

**起始版本：** 22

**需要权限：** ohos.permission.MANAGE_SELF_SKILLS

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700351](../errorcode-bundle.md#17700351-无效的文件类型) |
