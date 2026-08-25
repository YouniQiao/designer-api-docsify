# openFormManager

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## openFormManager

```TypeScript
function openFormManager(want: Want): void
```

打开当前应用的卡片管理页面。适用于卡片管理场景，例如预览当前应用所有可以加桌的卡片、添加卡片到负一屏或桌面等。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
