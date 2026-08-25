# resourceToSendableResource

## 导入模块

```TypeScript
import { sendableResourceManager } from 'kits/@kit.LocalizationKit';
```

## resourceToSendableResource

```TypeScript
export function resourceToSendableResource(resource: Resource): SendableResource
```

将Resource对象转换为可用于跨线程传输的SendableResource对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resource | [Resource](arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
