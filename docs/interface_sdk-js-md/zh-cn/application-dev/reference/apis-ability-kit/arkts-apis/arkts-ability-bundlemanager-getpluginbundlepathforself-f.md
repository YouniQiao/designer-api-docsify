# getPluginBundlePathForSelf

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getPluginBundlePathForSelf

```TypeScript
function getPluginBundlePathForSelf(pluginBundleName: string): string
```

获取指定插件在当前[应用沙箱](../../../file-management/app-sandbox-directory.md)内的安装路径。

**起始版本：** 22

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
