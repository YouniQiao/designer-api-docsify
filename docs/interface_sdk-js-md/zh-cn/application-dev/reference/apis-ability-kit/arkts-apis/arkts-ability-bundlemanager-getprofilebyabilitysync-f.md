# getProfileByAbilitySync

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getProfileByAbilitySync

```TypeScript
function getProfileByAbilitySync(moduleName: string, abilityName: string, metadataName?: string): Array<string>
```

以同步方法根据给定的moduleName、abilityName和metadataName（module.json5中 [metadata标签](../../../quick-start/module-configuration-file.md#metadata标签)下的name）获取自身相应配置文件的json格式字符串，返回对象为string数 组。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| abilityName | string | 是 |
| metadataName | string | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700024](../errorcode-bundle.md#17700024-没有相应的配置文件) |
| [17700029](../errorcode-bundle.md#17700029-指定的ability被禁用) |
