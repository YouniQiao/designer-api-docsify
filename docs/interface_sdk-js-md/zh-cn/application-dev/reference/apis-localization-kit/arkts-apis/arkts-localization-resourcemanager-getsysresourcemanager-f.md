# getSysResourceManager

## 导入模块

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## getSysResourceManager

```TypeScript
export function getSysResourceManager(): ResourceManager
```

获取系统资源管理对象，用于访问系统预置的资源。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 |
| --- |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [9001009](../errorcode-resource-manager.md#9001009-获取系统资源管理对象失败) |
