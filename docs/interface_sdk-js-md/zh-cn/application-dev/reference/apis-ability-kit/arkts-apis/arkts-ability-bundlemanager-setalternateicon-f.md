# setAlternateIcon

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## setAlternateIcon

```TypeScript
function setAlternateIcon(alternateIconName: string): Promise<void>
```

根据给定的备用图标名称设置调用方自身的备用图标。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alternateIconName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17700308](../errorcode-bundle.md#17700308-备用图标名称没有在配置文件中配置) |
| [17700309](../errorcode-bundle.md#17700309-当前没有设置备用图标) |
| [17700310](../errorcode-bundle.md#17700310-设置备用图标失败) |
