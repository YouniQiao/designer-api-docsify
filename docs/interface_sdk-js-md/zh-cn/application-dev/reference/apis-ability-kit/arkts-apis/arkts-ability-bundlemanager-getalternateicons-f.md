# getAlternateIcons

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAlternateIcons

```TypeScript
function getAlternateIcons(): Promise<Array<AlternateIconInfo>>
```

查询当前应用在app.json5中[alternateIcons标签](../../../quick-start/app-configuration-file.md#alternateicons标签)配置的备用图标信息。使用 Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;AlternateIconInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17700311](../errorcode-bundle.md#17700311-查询备用图标失败) |
