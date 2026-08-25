# sendableResourceToResource

## 导入模块

```TypeScript
import { sendableResourceManager } from 'kits/@kit.LocalizationKit';
```

## sendableResourceToResource

```TypeScript
export function sendableResourceToResource(resource: SendableResource): Resource
```

将跨线程传输的SendableResource对象转换为Resource对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Resource](arkts-localization-resource-resource-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
