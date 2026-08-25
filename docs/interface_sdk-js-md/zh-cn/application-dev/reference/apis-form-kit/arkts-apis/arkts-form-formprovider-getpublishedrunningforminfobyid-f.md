# getPublishedRunningFormInfoById

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedRunningFormInfoById

```TypeScript
function getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>
```

获取当前应用已加桌的指定卡片信息，使用Promise异步回调。适用于卡片管理、调试等场景，例如查看指定卡片的位置信息和尺寸信息。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;formInfo.RunningFormInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |
