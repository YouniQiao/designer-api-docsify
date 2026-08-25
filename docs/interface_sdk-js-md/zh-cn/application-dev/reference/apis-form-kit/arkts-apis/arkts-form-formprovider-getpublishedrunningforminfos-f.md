# getPublishedRunningFormInfos

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedRunningFormInfos

```TypeScript
function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>
```

获取所有已加桌的卡片信息，使用Promise异步回调。适用于卡片管理、批量操作、统计等场景，例如查看应用所有已添加到桌面的卡片信息、批量更新卡片状态等。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;formInfo.RunningFormInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
